import ssl
import unittest
from unittest.mock import patch

from com.alipay.ams.api.net import default_http_rpc


class DefaultHttpRpcTlsTest(unittest.TestCase):
    def test_connection_validates_chain_and_hostname(self):
        with patch.object(default_http_rpc.http_client, 'HTTPSConnection') as connect:
            getattr(default_http_rpc, "__get_http_connection")('https://gateway.example/test')
            options = connect.call_args.kwargs
            self.assertEqual(options['host'], 'gateway.example')
            self.assertEqual(options['context'].verify_mode, ssl.CERT_REQUIRED)
            self.assertTrue(options['context'].check_hostname)

    def test_context_failure_does_not_fall_back(self):
        with patch.object(default_http_rpc.ssl, 'create_default_context',
                          side_effect=ssl.SSLError('test configuration failure')):
            with patch.object(default_http_rpc.http_client, 'HTTPSConnection') as connect:
                with self.assertRaises(ssl.SSLError):
                    getattr(default_http_rpc, "__get_http_connection")('https://gateway.example/test')
                connect.assert_not_called()


if __name__ == '__main__':
    unittest.main()

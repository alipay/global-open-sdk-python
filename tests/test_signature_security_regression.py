import base64
import unittest
import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa as crypto_rsa
from com.alipay.ams.api.tools import signature_tool
from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.exception.exception import AlipayApiException


class SignatureSecurityRegressionTest(unittest.TestCase):
    def test_signatures_and_response_rules(self):
        key = crypto_rsa.generate_private_key(public_exponent=65537, key_size=2048)
        private = base64.b64encode(key.private_bytes(serialization.Encoding.DER,
            serialization.PrivateFormat.PKCS8, serialization.NoEncryption())).decode()
        public = base64.b64encode(key.public_key().public_bytes(serialization.Encoding.DER,
            serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
        client = DefaultAlipayClient('https://localhost', 'local-test', private, public)
        check = getattr(client, '_DefaultAlipayClient__assert_response_verified')
        for path in ['/ams/api/v1/payments/pay', '/ams/api/v1/payments/createPaymentSession']:
            body = '{"result":{"resultStatus":"S"}}'
            time = '2026-10-22T00:00:00Z'
            signature = signature_tool.sign('POST', path, 'local-test', time, body, private)
            self.assertTrue(signature_tool.verify('POST', path, 'local-test', time, body, signature, public))
            with self.assertRaises(rsa.VerificationError):
                signature_tool.verify('POST', path, 'local-test', time, body + ' ', signature, public)
            check('POST', path, 'local-test', time, body, signature)
            for response_time, sig in [(None, None), (time, None), (None, signature)]:
                with self.assertRaises(AlipayApiException):
                    check('POST', path, 'local-test', response_time, body, sig)
            for status in ['F', 'U']:
                check('POST', path, 'local-test', None, '{"result":{"resultStatus":"'+status+'"}}', None)

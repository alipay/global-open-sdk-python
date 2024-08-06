from com.alipay.ams.api.exception.exception import AlipayApiException

from com.alipay.ams.api.tools.signature_tool import verify


def check_signature(http_method, path, client_id, req_time_str, req_body, signature, alipay_public_key):
    if signature and 'signature=' in signature:
        signature = signature.split('signature=')[1]
        return verify(http_method, path, client_id, req_time_str, req_body, signature, alipay_public_key)
    raise AlipayApiException('signature invalid:' + str(signature))

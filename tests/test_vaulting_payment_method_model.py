import json
import unittest
from com.alipay.ams.api.model.vaulting_request_payment_method_detail import VaultingRequestPaymentMethodDetail
from com.alipay.ams.api.model.payment_method_detail import PaymentMethodDetail
from com.alipay.ams.api.request.pay.alipay_vaulting_payment_method_request import AlipayVaultingPaymentMethodRequest
from com.alipay.ams.api.response.pay.alipay_vaulting_payment_method_response import AlipayVaultingPaymentMethodResponse
from com.alipay.ams.api.response.pay.alipay_vaulting_query_response import AlipayVaultingQueryResponse


class VaultingPaymentMethodModelTest(unittest.TestCase):
    def test_metadata_serialization_and_original_response_types(self):
        metadata = {"recurringType": "UNSCHEDULED", "enabled": False, "count": 0, "items": []}
        detail = VaultingRequestPaymentMethodDetail()
        detail.payment_method_type = "CARD"
        detail.payment_method_meta_data = metadata
        request = AlipayVaultingPaymentMethodRequest()
        request.payment_method_detail = detail
        encoded = json.loads(request.to_ams_json())
        self.assertEqual(encoded["paymentMethodDetail"]["paymentMethodMetaData"], metadata)
        for response_type in [AlipayVaultingPaymentMethodResponse, AlipayVaultingQueryResponse]:
            response = response_type(json.dumps({"paymentMethodDetail": {"paymentMethodType": "CARD"}}))
            self.assertIsInstance(response.payment_method_detail, PaymentMethodDetail)
            self.assertFalse(hasattr(response.payment_method_detail, "payment_method_meta_data"))

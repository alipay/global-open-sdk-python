import json


class AcquirerInfo:

    def __init__(self):
        self.__acquirer_name = None
        self.__reference_request_id = None
        self.__acquirer_transaction_id = None
        self.__acquirer_merchant_id = None
        self.__acquirer_result_code = None
        self.__acquirer_result_message = None

    @property
    def acquirer_name(self):
        return self.__acquirer_name

    @acquirer_name.setter
    def acquirer_name(self, acquirer_name):
        self.__acquirer_name = acquirer_name

    @property
    def reference_request_id(self):
        return self.__reference_request_id

    @reference_request_id.setter
    def reference_request_id(self, reference_request_id):
        self.__reference_request_id = reference_request_id

    @property
    def acquirer_transaction_id(self):
        return self.__acquirer_transaction_id

    @acquirer_transaction_id.setter
    def acquirer_transaction_id(self, acquirer_transaction_id):
        self.__acquirer_transaction_id = acquirer_transaction_id

    @property
    def acquirer_merchant_id(self):
        return self.__acquirer_merchant_id

    @acquirer_merchant_id.setter
    def acquirer_merchant_id(self, acquirer_merchant_id):
        self.__acquirer_merchant_id = acquirer_merchant_id

    @property
    def acquirer_result_code(self):
        return self.__acquirer_result_code

    @acquirer_result_code.setter
    def acquirer_result_code(self, acquirer_result_code):
        self.__acquirer_result_code = acquirer_result_code

    @property
    def acquirer_result_message(self):
        return self.__acquirer_result_message

    @acquirer_result_message.setter
    def acquirer_result_message(self, acquirer_result_message):
        self.__acquirer_result_message = acquirer_result_message

    def parse_rsp_body(self, result_body):
        if type(result_body) == str:
            payment_result_info_body = json.loads(result_body)

        if 'acquirerName' in result_body:
            self.__acquirer_name = result_body['acquirerName']

        if 'referenceRequestId' in result_body:
            self.__reference_request_id = result_body['referenceRequestId']

        if 'acquirerTransactionId' in result_body:
            self.__acquirer_transaction_id = result_body['acquirerTransactionId']

        if 'acquirerMerchantId' in result_body:
            self.__acquirer_merchant_id = result_body['acquirerMerchantId']

        if 'acquirerResultCode' in result_body:
            self.__acquirer_result_code = result_body['acquirerResultCode']

        if 'acquirerResultMessage' in result_body:
            self.__acquirer_result_message = result_body['acquirerResultMessage']





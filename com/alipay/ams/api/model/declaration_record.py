import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.customs_info import CustomsInfo
from com.alipay.ams.api.model.merchant_customs_info import MerchantCustomsInfo


class DeclarationRecord(object):

    def __init__(self):
        self.__declaration_request_id = None
        self.__customs_payment_id = None
        self.__customs_order_id = None
        self.__customs = None  # type: CustomsInfo
        self.__merchant_customs_info = None  # type: MerchantCustomsInfo
        self.__declaration_amount = None  # type: Amount
        self.__split_order = None
        self.__declaration_request_status = None
        self.__last_modified_time = None
        self.__customs_declaration_result_code = None
        self.__customs_declaration_result_desc = None
        self.__customs_declaration_return_time = None

    @property
    def declaration_request_id(self):
        return self.__declaration_request_id

    @declaration_request_id.setter
    def declaration_request_id(self, value):
        self.__declaration_request_id = value

    @property
    def customs_payment_id(self):
        return self.__customs_payment_id

    @customs_payment_id.setter
    def customs_payment_id(self, value):
        self.__customs_payment_id = value

    @property
    def customs_order_id(self):
        return self.__customs_order_id

    @customs_order_id.setter
    def customs_order_id(self, value):
        self.__customs_order_id = value

    @property
    def customs(self):
        return self.__customs

    @customs.setter
    def customs(self, value):
        self.__customs = value

    @property
    def merchant_customs_info(self):
        return self.__merchant_customs

    @merchant_customs_info.setter
    def merchant_customs_info(self, value):
        self.__merchant_customs = value

    @property
    def declaration_amount(self):
        return self.__declaration_amount

    @declaration_amount.setter
    def declaration_amount(self, value):
        self.__declaration_amount = value

    @property
    def split_order(self):
        return self.__split_order

    @split_order.setter
    def split_order(self, value):
        self.__split_order = value

    @property
    def declaration_request_status(self):
        return self.__declaration_request_status

    @declaration_request_status.setter
    def declaration_request_status(self, value):
        self.__declaration_request_status = value

    @property
    def last_modified_time(self):
        return self.__last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, value):
        self.__last_modified_time = value

    @property
    def customs_declaration_result_code(self):
        return self.__customs_declaration_result_code

    @customs_declaration_result_code.setter
    def customs_declaration_result_code(self, value):
        self.__customs_dec = value

    @property
    def customs_declaration_result_desc(self):
        return self.__customs_declaration_result_desc

    @customs_declaration_result_desc.setter
    def customs_declaration_result_desc(self, value):
        self.__customs_declaration_result_desc = value

    @property
    def customs_declaration_return_time(self):
        return self.__customs_declaration_return_time

    @customs_declaration_return_time.setter
    def customs_declaration_return_time(self, value):
        self.__customs_declaration_return_time = value

    def to_ams_dict(self):
        params = dict()
        if self.declaration_request_id is not None:
            params['declarationRequestId'] = self.declaration_request_id
        if self.customs_payment_id is not None:
            params['customsPaymentId'] = self.customs_payment_id
        if self.customs_order_id is not None:
            params['customsOrderId'] = self.customs_order_id
        if self.customs is not None:
            params['customs'] = self.customs.to_ams_dict()
        if self.merchant_customs_info is not None:
            params['merchantCustomsInfo'] = self.merchant_customs_info.to_ams_dict()
        if self.declaration_amount is not None:
            params['declarationAmount'] = self.declaration_amount.to_ams_dict()
        if self.split_order is not None:
            params['splitOrder'] = self.split_order
        if self.declaration_request_status is not None:
            params['declarationRequestStatus'] = self.declaration_request_status
        if self.last_modified_time is not None:
            params['lastModifiedTime'] = self.last_modified_time
        if self.customs_declaration_result_code is not None:
            params['customsDeclarationResultCode'] = self.customs_declaration_result_code
        if self.customs_declaration_result_desc is not None:
            params['customsDeclarationResultDesc'] = self.customs_declaration_result_desc
        if self.customs_declaration_return_time is not None:
            params['customsDeclarationReturnTime'] = self.customs_declaration_return_time
        return params

    def parse_rsp_body(self, declaration_record_body):
        if type(declaration_record_body) == str:
            declaration_record_body = json.loads(declaration_record_body)

        if 'declarationRequestId' in declaration_record_body:
            self.declaration_request_id = declaration_record_body['declarationRequestId']
        if 'customsPaymentId' in declaration_record_body:
            self.customs_payment_id = declaration_record_body['customsPaymentId']
        if 'customsOrderId' in declaration_record_body:
            self.customs_order_id = declaration_record_body['customsOrderId']
        if 'customs' in declaration_record_body:
            self.customs = CustomsInfo()
            self.customs.parse_rsp_body(declaration_record_body['customs'])
        if 'merchantCustomsInfo' in declaration_record_body:
            self.merchant_customs_info = MerchantCustomsInfo()
            self.merchant_customs_info.parse_rsp_body(declaration_record_body['merchantCustomsInfo'])
        if 'declarationAmount' in declaration_record_body:
            self.declaration_amount = Amount()
            self.declaration_amount.parse_rsp_body(declaration_record_body['declarationAmount'])
        if 'splitOrder' in declaration_record_body:
            self.split_order = declaration_record_body['splitOrder']
        if 'declarationRequestStatus' in declaration_record_body:
            self.declaration_request_status = declaration_record_body['declarationRequestStatus']
        if 'lastModifiedTime' in declaration_record_body:
            self.last_modified_time = declaration_record_body['lastModifiedTime']
        if 'customsDeclarationResultCode' in declaration_record_body:
            self.customs_declaration_result_code = declaration_record_body['customsDeclarationResultCode']
        if 'customsDeclarationResultDesc' in declaration_record_body:
            self.customs_declaration_result_desc = declaration_record_body['customsDeclarationResultDesc']
        if 'customsDeclarationReturnTime' in declaration_record_body:
            self.customs_declaration_return_time = declaration_record_body['customsDeclarationReturnTime']

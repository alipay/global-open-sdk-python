import json

from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.payment_method import PaymentMethod


class TransferToDetail:
    def __init__(self):
        self.__transfer_to_method = None  # type: PaymentMethod
        self.__transfer_to_currency = None
        self.__fee_Amount = None  # type: Amount
        self.__actual_transfer_to_amount = None  # type: Amount
        self.__purpose_code = None
        self.__transfer_notify_url = None
        self.__transfer_remark = None

    @property
    def transfer_to_method(self):
        return self.__transfer_to_method

    @transfer_to_method.setter
    def transfer_to_method(self, value):
        self.__transfer_to_method = value

    @property
    def transfer_to_currency(self):
        return self.__transfer_to_currency

    @transfer_to_currency.setter
    def transfer_to_currency(self, value):
        self.__transfer_to_currency = value

    @property
    def fee_Amount(self):
        return self.__fee_Amount

    @fee_Amount.setter
    def fee_Amount(self, value):
        self.__fee_Amount = value

    @property
    def actual_transfer_to_amount(self):
        return self.__actual_transfer_to_amount

    @actual_transfer_to_amount.setter
    def actual_transfer_to_amount(self, value):
        self.__actual_transfer_to_amount = value

    @property
    def purpose_code(self):
        return self.__purpose_code

    @purpose_code.setter
    def purpose_code(self, value):
        self.__purpose_code = value

    @property
    def transfer_notify_url(self):
        return self.__transfer_notify_url

    @transfer_notify_url.setter
    def transfer_notify_url(self, value):
        self.__transfer_notify_url = value

    @property
    def transfer_remark(self):
        return self.__transfer_remark

    @transfer_remark.setter
    def transfer_remark(self, value):
        self.__transfer_remark = value

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transfer_to_method") and self.transfer_to_method:
            params['transferToMethod'] = self.transfer_to_method.to_ams_dict()
        if hasattr(self, "transfer_to_currency") and self.transfer_to_currency:
            params['transferToCurrency'] = self.transfer_to_currency
        if hasattr(self, "fee_Amount") and self.fee_Amount:
            params['feeAmount'] = self.fee_Amount.to_ams_dict()
        if hasattr(self, "actual_transfer_to_amount") and self.actual_transfer_to_amount:
            params['actualTransferToAmount'] = self.actual_transfer_to_amount.to_ams_dict()
        if hasattr(self, "purpose_code") and self.purpose_code:
            params['purposeCode'] = self.purpose_code
        if hasattr(self, "transfer_notify_url") and self.transfer_notify_url:
            params['transferNotifyUrl'] = self.transfer_notify_url
        if hasattr(self, "transfer_remark") and self.transfer_remark:
            params['transferRemark'] = self.transfer_remark
        return params

    def parse_rsp_body(self, response_body):
        if type(response_body) == str:
            response_body = json.loads(response_body)

        if 'transferToMethod' in response_body:
            self.transfer_to_method.parse_rsp_body(response_body['transferToMethod'])
        if 'transferToCurrency' in response_body:
            self.transfer_to_currency = response_body['transferToCurrency']
        if 'feeAmount' in response_body:
            self.fee_Amount.parse_rsp_body(response_body['feeAmount'])
        if 'actualTransferToAmount' in response_body:
            self.actual_transfer_to_amount.parse_rsp_body(response_body['actualTransferToAmount'])
        if 'purposeCode' in response_body:
            self.purpose_code = response_body['purposeCode']
        if 'transferNotifyUrl' in response_body:
            self.transfer_notify_url = response_body['transferNotifyUrl']
        if 'transferRemark' in response_body:
            self.transfer_remark = response_body['transferRemark']
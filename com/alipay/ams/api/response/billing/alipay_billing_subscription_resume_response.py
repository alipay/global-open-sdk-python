import json
from com.alipay.ams.api.model.result_info import ResultInfo



from com.alipay.ams.api.response.alipay_response import AlipayResponse

class AlipayBillingSubscriptionResumeResponse(AlipayResponse):
    def __init__(self, rsp_body):
        super(AlipayResponse, self).__init__() 

        self.__result = None  # type: ResultInfo
        self.__subscription_id = None  # type: str
        self.__status = None  # type: str
        self.__billing_cycle_anchor = None  # type: str
        self.__proration_invoice_id = None  # type: str
        self.__proration_date = None  # type: str
        self.parse_rsp_body(rsp_body) 


    @property
    def result(self):
        """Gets the result of this AlipayBillingSubscriptionResumeResponse.
        
        """
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value
    @property
    def subscription_id(self):
        """
        The subscription ID. Maximum length: 64 characters.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def status(self):
        """
        The current status. Maximum length: 20 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def billing_cycle_anchor(self):
        """
        The billing cycle anchor. Note: See documentation for details.
        """
        return self.__billing_cycle_anchor

    @billing_cycle_anchor.setter
    def billing_cycle_anchor(self, value):
        self.__billing_cycle_anchor = value
    @property
    def proration_invoice_id(self):
        """
        The proration invoice id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__proration_invoice_id

    @proration_invoice_id.setter
    def proration_invoice_id(self, value):
        self.__proration_invoice_id = value
    @property
    def proration_date(self):
        """
        The proration date. Note: See documentation for details.
        """
        return self.__proration_date

    @proration_date.setter
    def proration_date(self, value):
        self.__proration_date = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "result") and self.result is not None:
            params['result'] = self.result
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "billing_cycle_anchor") and self.billing_cycle_anchor is not None:
            params['billingCycleAnchor'] = self.billing_cycle_anchor
        if hasattr(self, "proration_invoice_id") and self.proration_invoice_id is not None:
            params['prorationInvoiceId'] = self.proration_invoice_id
        if hasattr(self, "proration_date") and self.proration_date is not None:
            params['prorationDate'] = self.proration_date
        return params


    def parse_rsp_body(self, response_body):
        response_body = super(AlipayBillingSubscriptionResumeResponse, self).parse_rsp_body(response_body)
        if 'result' in response_body:
            self.__result = ResultInfo()
            self.__result.parse_rsp_body(response_body['result'])
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'billingCycleAnchor' in response_body:
            self.__billing_cycle_anchor = response_body['billingCycleAnchor']
        if 'prorationInvoiceId' in response_body:
            self.__proration_invoice_id = response_body['prorationInvoiceId']
        if 'prorationDate' in response_body:
            self.__proration_date = response_body['prorationDate']

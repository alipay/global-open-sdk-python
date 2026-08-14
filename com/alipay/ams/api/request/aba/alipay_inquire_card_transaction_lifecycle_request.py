import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInquireCardTransactionLifecycleRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInquireCardTransactionLifecycleRequest, self).__init__("/ams/api/v1/aba/cards/inquireCardTransactionLifecycle") 

        self.__start_time = None  # type: str
        self.__end_time = None  # type: str
        self.__asset_id_list = None  # type: [str]
        self.__transaction_currency_list = None  # type: [str]
        self.__lifecycle_id_list = None  # type: [str]
        self.__page_size = None  # type: int
        self.__page_number = None  # type: int
        

    @property
    def start_time(self):
        """
        The optional lower bound for the lifecycle time anchor in ISO 8601 format. The maximum supported time range is 100 days.
        """
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value
    @property
    def end_time(self):
        """
        The optional upper bound for the lifecycle time anchor in ISO 8601 format. The maximum supported time range is 100 days.
        """
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value
    @property
    def asset_id_list(self):
        """
        The card asset IDs to include. Values within the array are combined using OR.
        """
        return self.__asset_id_list

    @asset_id_list.setter
    def asset_id_list(self, value):
        self.__asset_id_list = value
    @property
    def transaction_currency_list(self):
        """
        The ISO 4217 transaction currencies to include. Values within the array are combined using OR.
        """
        return self.__transaction_currency_list

    @transaction_currency_list.setter
    def transaction_currency_list(self, value):
        self.__transaction_currency_list = value
    @property
    def lifecycle_id_list(self):
        """
        The lifecycle IDs to include. Values within the array are combined using OR.
        """
        return self.__lifecycle_id_list

    @lifecycle_id_list.setter
    def lifecycle_id_list(self, value):
        self.__lifecycle_id_list = value
    @property
    def page_size(self):
        """
        The number of items per page. No default is applied.
        """
        return self.__page_size

    @page_size.setter
    def page_size(self, value):
        self.__page_size = value
    @property
    def page_number(self):
        """
        The one-based page number. No default is applied.
        """
        return self.__page_number

    @page_number.setter
    def page_number(self, value):
        self.__page_number = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "start_time") and self.start_time is not None:
            params['startTime'] = self.start_time
        if hasattr(self, "end_time") and self.end_time is not None:
            params['endTime'] = self.end_time
        if hasattr(self, "asset_id_list") and self.asset_id_list is not None:
            params['assetIdList'] = self.asset_id_list
        if hasattr(self, "transaction_currency_list") and self.transaction_currency_list is not None:
            params['transactionCurrencyList'] = self.transaction_currency_list
        if hasattr(self, "lifecycle_id_list") and self.lifecycle_id_list is not None:
            params['lifecycleIdList'] = self.lifecycle_id_list
        if hasattr(self, "page_size") and self.page_size is not None:
            params['pageSize'] = self.page_size
        if hasattr(self, "page_number") and self.page_number is not None:
            params['pageNumber'] = self.page_number
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'startTime' in response_body:
            self.__start_time = response_body['startTime']
        if 'endTime' in response_body:
            self.__end_time = response_body['endTime']
        if 'assetIdList' in response_body:
            self.__asset_id_list = response_body['assetIdList']
        if 'transactionCurrencyList' in response_body:
            self.__transaction_currency_list = response_body['transactionCurrencyList']
        if 'lifecycleIdList' in response_body:
            self.__lifecycle_id_list = response_body['lifecycleIdList']
        if 'pageSize' in response_body:
            self.__page_size = response_body['pageSize']
        if 'pageNumber' in response_body:
            self.__page_number = response_body['pageNumber']

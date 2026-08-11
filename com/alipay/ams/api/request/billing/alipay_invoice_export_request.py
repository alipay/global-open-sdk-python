import json



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayInvoiceExportRequest(AlipayRequest):
    def __init__(self):
        super(AlipayInvoiceExportRequest, self).__init__("/ams/api/v1/billing/invoice/export") 

        self.__customer_id = None  # type: str
        self.__status = None  # type: str
        self.__subscription_id = None  # type: str
        self.__invoice_ids = None  # type: [str]
        self.__start_date = None  # type: str
        self.__end_date = None  # type: str
        self.__file_format = None  # type: str
        self.__language = None  # type: str
        self.__download_type = None  # type: str
        self.__column_preset = None  # type: str
        

    @property
    def customer_id(self):
        """
        Filter by customer ID. Returns only invoices belonging to this customer. Can be null (no filter).
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def status(self):
        """
        Filter by invoice status. Allowed values: &#x60;DRAFT&#x60;, &#x60;OPEN&#x60;, &#x60;PAID&#x60;, &#x60;UNCOLLECTIBLE&#x60;, &#x60;VOID&#x60;. Can be null (no filter).
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def subscription_id(self):
        """
        Filter invoices by associated subscription ID. Returns only invoices linked to this subscription. Can be null (no filter).
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def invoice_ids(self):
        """
        Filter by exact list of invoice IDs. Max 1000 elements. When provided, other filters (&#x60;status&#x60;, &#x60;customerId&#x60;, &#x60;subscriptionId&#x60;, &#x60;startDate&#x60;, &#x60;endDate&#x60;) are ignored. Can be null (no filter).
        """
        return self.__invoice_ids

    @invoice_ids.setter
    def invoice_ids(self, value):
        self.__invoice_ids = value
    @property
    def start_date(self):
        """
        Date range start for invoice creation time (ISO 8601 format, e.g., &#x60;2026-04-01T00:00:00+00:00&#x60;). Can be null (no lower bound).
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value
    @property
    def end_date(self):
        """
        Date range end for invoice creation time (ISO 8601 format, e.g., &#x60;2026-04-30T23:59:59+00:00&#x60;). Can be null (no upper bound).
        """
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value
    @property
    def file_format(self):
        """
        Output file format. Allowed values: &#x60;csv&#x60; (default), &#x60;xlsx&#x60;. Can be null (defaults to &#x60;csv&#x60;).
        """
        return self.__file_format

    @file_format.setter
    def file_format(self, value):
        self.__file_format = value
    @property
    def language(self):
        """
        BCP-47 language code for localized column headers (e.g., &#x60;en&#x60;, &#x60;zh&#x60;). Can be null (defaults to &#x60;en&#x60;).
        """
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value
    @property
    def download_type(self):
        """
        Type of entity to export. Must be &#x60;INVOICE&#x60;. Required - no default.
        """
        return self.__download_type

    @download_type.setter
    def download_type(self, value):
        self.__download_type = value
    @property
    def column_preset(self):
        """
        Column selection preset. Allowed values: &#x60;DEFAULT&#x60; (standard columns), &#x60;ALL&#x60; (all available columns). Can be null (defaults to &#x60;DEFAULT&#x60;).
        """
        return self.__column_preset

    @column_preset.setter
    def column_preset(self, value):
        self.__column_preset = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "invoice_ids") and self.invoice_ids is not None:
            params['invoiceIds'] = self.invoice_ids
        if hasattr(self, "start_date") and self.start_date is not None:
            params['startDate'] = self.start_date
        if hasattr(self, "end_date") and self.end_date is not None:
            params['endDate'] = self.end_date
        if hasattr(self, "file_format") and self.file_format is not None:
            params['fileFormat'] = self.file_format
        if hasattr(self, "language") and self.language is not None:
            params['language'] = self.language
        if hasattr(self, "download_type") and self.download_type is not None:
            params['downloadType'] = self.download_type
        if hasattr(self, "column_preset") and self.column_preset is not None:
            params['columnPreset'] = self.column_preset
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'invoiceIds' in response_body:
            self.__invoice_ids = response_body['invoiceIds']
        if 'startDate' in response_body:
            self.__start_date = response_body['startDate']
        if 'endDate' in response_body:
            self.__end_date = response_body['endDate']
        if 'fileFormat' in response_body:
            self.__file_format = response_body['fileFormat']
        if 'language' in response_body:
            self.__language = response_body['language']
        if 'downloadType' in response_body:
            self.__download_type = response_body['downloadType']
        if 'columnPreset' in response_body:
            self.__column_preset = response_body['columnPreset']

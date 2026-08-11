import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class Invoice:
    def __init__(self):
        
        self.__invoice_id = None  # type: str
        self.__subscription_id = None  # type: str
        self.__customer_id = None  # type: str
        self.__customer_first_name = None  # type: str
        self.__customer_last_name = None  # type: str
        self.__customer_email = None  # type: str
        self.__reason = None  # type: str
        self.__status = None  # type: str
        self.__total_amount = None  # type: Amount
        self.__paid_amount = None  # type: Amount
        self.__remain_amount = None  # type: Amount
        self.__currency = None  # type: str
        self.__period_start = None  # type: str
        self.__period_end = None  # type: str
        self.__due_date = None  # type: str
        self.__gmt_create = None  # type: str
        self.__gmt_update = None  # type: str
        self.__description = None  # type: str
        self.__pdf_file_url = None  # type: str
        

    @property
    def invoice_id(self):
        """
        System-generated invoice ID. Format: &#x60;inv_&#x60; + 10-char alphanumeric. Cannot be null.
        """
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value
    @property
    def subscription_id(self):
        """
        Associated subscription ID. May be null for standalone manual invoices. Can be null.
        """
        return self.__subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self.__subscription_id = value
    @property
    def customer_id(self):
        """
        Customer ID this invoice belongs to. Cannot be null.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def customer_first_name(self):
        """
        Customer&#39;s first name. Populated from the customer record at invoice creation time. Displayed on merchant portal list view. Can be null.
        """
        return self.__customer_first_name

    @customer_first_name.setter
    def customer_first_name(self, value):
        self.__customer_first_name = value
    @property
    def customer_last_name(self):
        """
        Customer&#39;s last name. Populated from the customer record at invoice creation time. Displayed on merchant portal list view. Can be null.
        """
        return self.__customer_last_name

    @customer_last_name.setter
    def customer_last_name(self, value):
        self.__customer_last_name = value
    @property
    def customer_email(self):
        """
        Customer&#39;s email address. Populated from the customer record at invoice creation time. Displayed on merchant portal list view. Can be null.
        """
        return self.__customer_email

    @customer_email.setter
    def customer_email(self, value):
        self.__customer_email = value
    @property
    def reason(self):
        """
        Invoice creation reason: &#x60;SUBSCRIPTION_CREATION&#x60;, &#x60;SUBSCRIPTION_RECURRENCE&#x60;, &#x60;SUBSCRIPTION_UPDATE&#x60;. Cannot be null.
        """
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value
    @property
    def status(self):
        """
        Current invoice status: &#x60;DRAFT&#x60;, &#x60;OPEN&#x60;, &#x60;PAID&#x60;, &#x60;UNCOLLECTIBLE&#x60;, &#x60;VOID&#x60;. Cannot be null.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def total_amount(self):
        """Gets the total_amount of this Invoice.
        
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value
    @property
    def paid_amount(self):
        """Gets the paid_amount of this Invoice.
        
        """
        return self.__paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self.__paid_amount = value
    @property
    def remain_amount(self):
        """Gets the remain_amount of this Invoice.
        
        """
        return self.__remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self.__remain_amount = value
    @property
    def currency(self):
        """
        Three-letter ISO currency code in uppercase (e.g., &#x60;\&quot;USD\&quot;&#x60;). The invoice currency. Cannot be null.
        """
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value
    @property
    def period_start(self):
        """
        Billing period start timestamp (ISO 8601). Cannot be null.
        """
        return self.__period_start

    @period_start.setter
    def period_start(self, value):
        self.__period_start = value
    @property
    def period_end(self):
        """
        Billing period end timestamp (ISO 8601). Cannot be null.
        """
        return self.__period_end

    @period_end.setter
    def period_end(self, value):
        self.__period_end = value
    @property
    def due_date(self):
        """
        Payment due date (ISO 8601). Cannot be null.
        """
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value
    @property
    def gmt_create(self):
        """
        ISO 8601 timestamp of invoice creation. Cannot be null.
        """
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self.__gmt_create = value
    @property
    def gmt_update(self):
        """
        ISO 8601 timestamp of last invoice update. Cannot be null.
        """
        return self.__gmt_update

    @gmt_update.setter
    def gmt_update(self, value):
        self.__gmt_update = value
    @property
    def description(self):
        """
        Invoice description text. Can be null.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def pdf_file_url(self):
        """
        URL of the generated PDF file for download. Can be null (PDF not yet generated).
        """
        return self.__pdf_file_url

    @pdf_file_url.setter
    def pdf_file_url(self, value):
        self.__pdf_file_url = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "invoice_id") and self.invoice_id is not None:
            params['invoiceId'] = self.invoice_id
        if hasattr(self, "subscription_id") and self.subscription_id is not None:
            params['subscriptionId'] = self.subscription_id
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "customer_first_name") and self.customer_first_name is not None:
            params['customerFirstName'] = self.customer_first_name
        if hasattr(self, "customer_last_name") and self.customer_last_name is not None:
            params['customerLastName'] = self.customer_last_name
        if hasattr(self, "customer_email") and self.customer_email is not None:
            params['customerEmail'] = self.customer_email
        if hasattr(self, "reason") and self.reason is not None:
            params['reason'] = self.reason
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "total_amount") and self.total_amount is not None:
            params['totalAmount'] = self.total_amount
        if hasattr(self, "paid_amount") and self.paid_amount is not None:
            params['paidAmount'] = self.paid_amount
        if hasattr(self, "remain_amount") and self.remain_amount is not None:
            params['remainAmount'] = self.remain_amount
        if hasattr(self, "currency") and self.currency is not None:
            params['currency'] = self.currency
        if hasattr(self, "period_start") and self.period_start is not None:
            params['periodStart'] = self.period_start
        if hasattr(self, "period_end") and self.period_end is not None:
            params['periodEnd'] = self.period_end
        if hasattr(self, "due_date") and self.due_date is not None:
            params['dueDate'] = self.due_date
        if hasattr(self, "gmt_create") and self.gmt_create is not None:
            params['gmtCreate'] = self.gmt_create
        if hasattr(self, "gmt_update") and self.gmt_update is not None:
            params['gmtUpdate'] = self.gmt_update
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "pdf_file_url") and self.pdf_file_url is not None:
            params['pdfFileUrl'] = self.pdf_file_url
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'invoiceId' in response_body:
            self.__invoice_id = response_body['invoiceId']
        if 'subscriptionId' in response_body:
            self.__subscription_id = response_body['subscriptionId']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'customerFirstName' in response_body:
            self.__customer_first_name = response_body['customerFirstName']
        if 'customerLastName' in response_body:
            self.__customer_last_name = response_body['customerLastName']
        if 'customerEmail' in response_body:
            self.__customer_email = response_body['customerEmail']
        if 'reason' in response_body:
            self.__reason = response_body['reason']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'totalAmount' in response_body:
            self.__total_amount = Amount()
            self.__total_amount.parse_rsp_body(response_body['totalAmount'])
        if 'paidAmount' in response_body:
            self.__paid_amount = Amount()
            self.__paid_amount.parse_rsp_body(response_body['paidAmount'])
        if 'remainAmount' in response_body:
            self.__remain_amount = Amount()
            self.__remain_amount.parse_rsp_body(response_body['remainAmount'])
        if 'currency' in response_body:
            self.__currency = response_body['currency']
        if 'periodStart' in response_body:
            self.__period_start = response_body['periodStart']
        if 'periodEnd' in response_body:
            self.__period_end = response_body['periodEnd']
        if 'dueDate' in response_body:
            self.__due_date = response_body['dueDate']
        if 'gmtCreate' in response_body:
            self.__gmt_create = response_body['gmtCreate']
        if 'gmtUpdate' in response_body:
            self.__gmt_update = response_body['gmtUpdate']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'pdfFileUrl' in response_body:
            self.__pdf_file_url = response_body['pdfFileUrl']

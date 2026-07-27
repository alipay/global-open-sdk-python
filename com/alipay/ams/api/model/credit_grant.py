import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.available_amount import AvailableAmount
from com.alipay.ams.api.model.applicability import Applicability




class CreditGrant:
    def __init__(self):
        
        self.__credit_grant_id = None  # type: str
        self.__credit_grant_name = None  # type: str
        self.__customer_id = None  # type: str
        self.__status = None  # type: str
        self.__amount = None  # type: Amount
        self.__available_amount = None  # type: AvailableAmount
        self.__applicability = None  # type: Applicability
        self.__priority = None  # type: int
        self.__category = None  # type: str
        self.__effective_date_time = None  # type: str
        self.__expiry_date_time = None  # type: str
        self.__created_date_time = None  # type: str
        self.__updated_date_time = None  # type: str
        

    @property
    def credit_grant_id(self):
        """
        The credit grant ID. Maximum length: 64 characters.
        """
        return self.__credit_grant_id

    @credit_grant_id.setter
    def credit_grant_id(self, value):
        self.__credit_grant_id = value
    @property
    def credit_grant_name(self):
        """
        The credit grant name. Maximum length: 255 characters.
        """
        return self.__credit_grant_name

    @credit_grant_name.setter
    def credit_grant_name(self, value):
        self.__credit_grant_name = value
    @property
    def customer_id(self):
        """
        The unique ID assigned by Antom to identify a customer. Maximum length: 64 characters.
        """
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        self.__customer_id = value
    @property
    def status(self):
        """
        The current status. Maximum length: 8 characters.
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    @property
    def amount(self):
        """Gets the amount of this CreditGrant.
        
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value
    @property
    def available_amount(self):
        """Gets the available_amount of this CreditGrant.
        
        """
        return self.__available_amount

    @available_amount.setter
    def available_amount(self, value):
        self.__available_amount = value
    @property
    def applicability(self):
        """Gets the applicability of this CreditGrant.
        
        """
        return self.__applicability

    @applicability.setter
    def applicability(self, value):
        self.__applicability = value
    @property
    def priority(self):
        """
        The priority.
        """
        return self.__priority

    @priority.setter
    def priority(self, value):
        self.__priority = value
    @property
    def category(self):
        """
        The category. Maximum length: 16 characters.
        """
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value
    @property
    def effective_date_time(self):
        """
        The effective date time. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__effective_date_time

    @effective_date_time.setter
    def effective_date_time(self, value):
        self.__effective_date_time = value
    @property
    def expiry_date_time(self):
        """
        The expiry date time. Maximum length: 32 characters. Note: See documentation for details.
        """
        return self.__expiry_date_time

    @expiry_date_time.setter
    def expiry_date_time(self, value):
        self.__expiry_date_time = value
    @property
    def created_date_time(self):
        """
        The created date time. Maximum length: 32 characters.
        """
        return self.__created_date_time

    @created_date_time.setter
    def created_date_time(self, value):
        self.__created_date_time = value
    @property
    def updated_date_time(self):
        """
        The updated date time. Maximum length: 32 characters.
        """
        return self.__updated_date_time

    @updated_date_time.setter
    def updated_date_time(self, value):
        self.__updated_date_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_grant_id") and self.credit_grant_id is not None:
            params['creditGrantId'] = self.credit_grant_id
        if hasattr(self, "credit_grant_name") and self.credit_grant_name is not None:
            params['creditGrantName'] = self.credit_grant_name
        if hasattr(self, "customer_id") and self.customer_id is not None:
            params['customerId'] = self.customer_id
        if hasattr(self, "status") and self.status is not None:
            params['status'] = self.status
        if hasattr(self, "amount") and self.amount is not None:
            params['amount'] = self.amount
        if hasattr(self, "available_amount") and self.available_amount is not None:
            params['availableAmount'] = self.available_amount
        if hasattr(self, "applicability") and self.applicability is not None:
            params['applicability'] = self.applicability
        if hasattr(self, "priority") and self.priority is not None:
            params['priority'] = self.priority
        if hasattr(self, "category") and self.category is not None:
            params['category'] = self.category
        if hasattr(self, "effective_date_time") and self.effective_date_time is not None:
            params['effectiveDateTime'] = self.effective_date_time
        if hasattr(self, "expiry_date_time") and self.expiry_date_time is not None:
            params['expiryDateTime'] = self.expiry_date_time
        if hasattr(self, "created_date_time") and self.created_date_time is not None:
            params['createdDateTime'] = self.created_date_time
        if hasattr(self, "updated_date_time") and self.updated_date_time is not None:
            params['updatedDateTime'] = self.updated_date_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditGrantId' in response_body:
            self.__credit_grant_id = response_body['creditGrantId']
        if 'creditGrantName' in response_body:
            self.__credit_grant_name = response_body['creditGrantName']
        if 'customerId' in response_body:
            self.__customer_id = response_body['customerId']
        if 'status' in response_body:
            self.__status = response_body['status']
        if 'amount' in response_body:
            self.__amount = Amount()
            self.__amount.parse_rsp_body(response_body['amount'])
        if 'availableAmount' in response_body:
            self.__available_amount = AvailableAmount()
            self.__available_amount.parse_rsp_body(response_body['availableAmount'])
        if 'applicability' in response_body:
            self.__applicability = Applicability()
            self.__applicability.parse_rsp_body(response_body['applicability'])
        if 'priority' in response_body:
            self.__priority = response_body['priority']
        if 'category' in response_body:
            self.__category = response_body['category']
        if 'effectiveDateTime' in response_body:
            self.__effective_date_time = response_body['effectiveDateTime']
        if 'expiryDateTime' in response_body:
            self.__expiry_date_time = response_body['expiryDateTime']
        if 'createdDateTime' in response_body:
            self.__created_date_time = response_body['createdDateTime']
        if 'updatedDateTime' in response_body:
            self.__updated_date_time = response_body['updatedDateTime']

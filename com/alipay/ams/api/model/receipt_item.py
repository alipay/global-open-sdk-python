import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class ReceiptItem:
    def __init__(self):
        
        self.__item_id = None  # type: str
        self.__description = None  # type: str
        self.__quantity = None  # type: int
        self.__unit_amount = None  # type: Amount
        self.__amount = None  # type: Amount
        self.__usage_amount = None  # type: Amount
        self.__usage_quantity = None  # type: str
        self.__usage_unit = None  # type: str
        self.__discount_amount = None  # type: Amount
        self.__tax_amount = None  # type: Amount
        self.__period_start = None  # type: str
        self.__period_end = None  # type: str
        self.__proration = None  # type: bool
        self.__gmt_create = None  # type: str
        self.__gmt_update = None  # type: str
        

    @property
    def item_id(self):
        """
        The item id. Maximum length: 64 characters.
        """
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        self.__item_id = value
    @property
    def description(self):
        """
        The description. Maximum length: 512 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def quantity(self):
        """
        The quantity.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    @property
    def unit_amount(self):
        """Gets the unit_amount of this ReceiptItem.
        
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
    @property
    def amount(self):
        """Gets the amount of this ReceiptItem.
        
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value
    @property
    def usage_amount(self):
        """Gets the usage_amount of this ReceiptItem.
        
        """
        return self.__usage_amount

    @usage_amount.setter
    def usage_amount(self, value):
        self.__usage_amount = value
    @property
    def usage_quantity(self):
        """
        The usage quantity.
        """
        return self.__usage_quantity

    @usage_quantity.setter
    def usage_quantity(self, value):
        self.__usage_quantity = value
    @property
    def usage_unit(self):
        """
        The usage unit. Maximum length: 32 characters.
        """
        return self.__usage_unit

    @usage_unit.setter
    def usage_unit(self, value):
        self.__usage_unit = value
    @property
    def discount_amount(self):
        """Gets the discount_amount of this ReceiptItem.
        
        """
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self.__discount_amount = value
    @property
    def tax_amount(self):
        """Gets the tax_amount of this ReceiptItem.
        
        """
        return self.__tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self.__tax_amount = value
    @property
    def period_start(self):
        """
        The period start. Maximum length: 24 characters.
        """
        return self.__period_start

    @period_start.setter
    def period_start(self, value):
        self.__period_start = value
    @property
    def period_end(self):
        """
        The period end. Maximum length: 24 characters.
        """
        return self.__period_end

    @period_end.setter
    def period_end(self, value):
        self.__period_end = value
    @property
    def proration(self):
        """
        The proration.
        """
        return self.__proration

    @proration.setter
    def proration(self, value):
        self.__proration = value
    @property
    def gmt_create(self):
        """
        The creation time. Maximum length: 24 characters.
        """
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self.__gmt_create = value
    @property
    def gmt_update(self):
        """
        The gmt update. Maximum length: 24 characters.
        """
        return self.__gmt_update

    @gmt_update.setter
    def gmt_update(self, value):
        self.__gmt_update = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "item_id") and self.item_id is not None:
            params['itemId'] = self.item_id
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        if hasattr(self, "unit_amount") and self.unit_amount is not None:
            params['unitAmount'] = self.unit_amount
        if hasattr(self, "amount") and self.amount is not None:
            params['amount'] = self.amount
        if hasattr(self, "usage_amount") and self.usage_amount is not None:
            params['usageAmount'] = self.usage_amount
        if hasattr(self, "usage_quantity") and self.usage_quantity is not None:
            params['usageQuantity'] = self.usage_quantity
        if hasattr(self, "usage_unit") and self.usage_unit is not None:
            params['usageUnit'] = self.usage_unit
        if hasattr(self, "discount_amount") and self.discount_amount is not None:
            params['discountAmount'] = self.discount_amount
        if hasattr(self, "tax_amount") and self.tax_amount is not None:
            params['taxAmount'] = self.tax_amount
        if hasattr(self, "period_start") and self.period_start is not None:
            params['periodStart'] = self.period_start
        if hasattr(self, "period_end") and self.period_end is not None:
            params['periodEnd'] = self.period_end
        if hasattr(self, "proration") and self.proration is not None:
            params['proration'] = self.proration
        if hasattr(self, "gmt_create") and self.gmt_create is not None:
            params['gmtCreate'] = self.gmt_create
        if hasattr(self, "gmt_update") and self.gmt_update is not None:
            params['gmtUpdate'] = self.gmt_update
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'itemId' in response_body:
            self.__item_id = response_body['itemId']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
        if 'unitAmount' in response_body:
            self.__unit_amount = Amount()
            self.__unit_amount.parse_rsp_body(response_body['unitAmount'])
        if 'amount' in response_body:
            self.__amount = Amount()
            self.__amount.parse_rsp_body(response_body['amount'])
        if 'usageAmount' in response_body:
            self.__usage_amount = Amount()
            self.__usage_amount.parse_rsp_body(response_body['usageAmount'])
        if 'usageQuantity' in response_body:
            self.__usage_quantity = response_body['usageQuantity']
        if 'usageUnit' in response_body:
            self.__usage_unit = response_body['usageUnit']
        if 'discountAmount' in response_body:
            self.__discount_amount = Amount()
            self.__discount_amount.parse_rsp_body(response_body['discountAmount'])
        if 'taxAmount' in response_body:
            self.__tax_amount = Amount()
            self.__tax_amount.parse_rsp_body(response_body['taxAmount'])
        if 'periodStart' in response_body:
            self.__period_start = response_body['periodStart']
        if 'periodEnd' in response_body:
            self.__period_end = response_body['periodEnd']
        if 'proration' in response_body:
            self.__proration = response_body['proration']
        if 'gmtCreate' in response_body:
            self.__gmt_create = response_body['gmtCreate']
        if 'gmtUpdate' in response_body:
            self.__gmt_update = response_body['gmtUpdate']

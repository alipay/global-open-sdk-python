import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class CreditNoteItem:
    def __init__(self):
        
        self.__credit_note_item_id = None  # type: str
        self.__type = None  # type: str
        self.__invoice_item_id = None  # type: str
        self.__description = None  # type: str
        self.__quantity = None  # type: int
        self.__unit_amount = None  # type: Amount
        self.__item_amount = None  # type: Amount
        

    @property
    def credit_note_item_id(self):
        """
        The credit note item ID. Maximum length: 64 characters.
        """
        return self.__credit_note_item_id

    @credit_note_item_id.setter
    def credit_note_item_id(self, value):
        self.__credit_note_item_id = value
    @property
    def type(self):
        """
        The credit note item type. Maximum length: 32 characters.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def invoice_item_id(self):
        """
        The related invoice item ID. Omitted for a custom line item. Maximum length: 64 characters.
        """
        return self.__invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, value):
        self.__invoice_item_id = value
    @property
    def description(self):
        """
        The credit note item description. Maximum length: 256 characters.
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def quantity(self):
        """
        The credited quantity.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    @property
    def unit_amount(self):
        """Gets the unit_amount of this CreditNoteItem.
        
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
    @property
    def item_amount(self):
        """Gets the item_amount of this CreditNoteItem.
        
        """
        return self.__item_amount

    @item_amount.setter
    def item_amount(self, value):
        self.__item_amount = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "credit_note_item_id") and self.credit_note_item_id is not None:
            params['creditNoteItemId'] = self.credit_note_item_id
        if hasattr(self, "type") and self.type is not None:
            params['type'] = self.type
        if hasattr(self, "invoice_item_id") and self.invoice_item_id is not None:
            params['invoiceItemId'] = self.invoice_item_id
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        if hasattr(self, "unit_amount") and self.unit_amount is not None:
            params['unitAmount'] = self.unit_amount
        if hasattr(self, "item_amount") and self.item_amount is not None:
            params['itemAmount'] = self.item_amount
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'creditNoteItemId' in response_body:
            self.__credit_note_item_id = response_body['creditNoteItemId']
        if 'type' in response_body:
            self.__type = response_body['type']
        if 'invoiceItemId' in response_body:
            self.__invoice_item_id = response_body['invoiceItemId']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
        if 'unitAmount' in response_body:
            self.__unit_amount = Amount()
            self.__unit_amount.parse_rsp_body(response_body['unitAmount'])
        if 'itemAmount' in response_body:
            self.__item_amount = Amount()
            self.__item_amount.parse_rsp_body(response_body['itemAmount'])

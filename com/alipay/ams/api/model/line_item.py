import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount




class LineItem:
    def __init__(self):
        
        self.__credit_note_item_id = None  # type: str
        self.__type = None  # type: str
        self.__invoice_item_id = None  # type: str
        self.__description = None  # type: str
        self.__quantity = None  # type: str
        self.__unit_amount = None  # type: Amount
        self.__item_amount = None  # type: Amount
        self.__metadata = None  # type: {str: (str,)}
        

    @property
    def credit_note_item_id(self):
        """
        The credit note item id. Maximum length: 64 characters.
        """
        return self.__credit_note_item_id

    @credit_note_item_id.setter
    def credit_note_item_id(self, value):
        self.__credit_note_item_id = value
    @property
    def type(self):
        """
        The type. Maximum length: 32 characters.
        """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
    @property
    def invoice_item_id(self):
        """
        The invoice item id. Maximum length: 64 characters. Note: See documentation for details.
        """
        return self.__invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, value):
        self.__invoice_item_id = value
    @property
    def description(self):
        """
        The description. Maximum length: 256 characters.
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
        """Gets the unit_amount of this LineItem.
        
        """
        return self.__unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self.__unit_amount = value
    @property
    def item_amount(self):
        """Gets the item_amount of this LineItem.
        
        """
        return self.__item_amount

    @item_amount.setter
    def item_amount(self, value):
        self.__item_amount = value
    @property
    def metadata(self):
        """
        Custom metadata for special use cases.
        """
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value


    

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
        if hasattr(self, "metadata") and self.metadata is not None:
            params['metadata'] = self.metadata
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
        if 'metadata' in response_body:
            self.__metadata = response_body['metadata']

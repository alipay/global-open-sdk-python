import json
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.merchant import Merchant
from com.alipay.ams.api.model.goods import Goods
from com.alipay.ams.api.model.shipping import Shipping
from com.alipay.ams.api.model.buyer import Buyer
from com.alipay.ams.api.model.env import Env
from com.alipay.ams.api.model.transit import Transit
from com.alipay.ams.api.model.lodging import Lodging
from com.alipay.ams.api.model.gaming import Gaming
from com.alipay.ams.api.model.declaration import Declaration




class Order:
    def __init__(self):
        
        self.__reference_order_id = None  # type: str
        self.__order_description = None  # type: str
        self.__order_amount = None  # type: Amount
        self.__order_discount_amount = None  # type: Amount
        self.__sub_total_order_amount = None  # type: Amount
        self.__merchant = None  # type: Merchant
        self.__goods = None  # type: [Goods]
        self.__shipping = None  # type: Shipping
        self.__buyer = None  # type: Buyer
        self.__env = None  # type: Env
        self.__extend_info = None  # type: str
        self.__transit = None  # type: Transit
        self.__lodging = None  # type: Lodging
        self.__gaming = None  # type: Gaming
        self.__need_declaration = None  # type: bool
        self.__declaration = None  # type: Declaration
        self.__order_type = None  # type: str
        

    @property
    def reference_order_id(self):
        """
        The unique ID to identify the order on the merchant side, which is assigned by the merchant that provides services or goods directly to the customer. This field is used for user consumption records display and other further actions such as disputes track or handling of customer complaints.  More information:  Maximum length: 64 characters
        """
        return self.__reference_order_id

    @reference_order_id.setter
    def reference_order_id(self, value):
        self.__reference_order_id = value
    @property
    def order_description(self):
        """
        Summary description of the order, which is used for user consumption records display or other further actions.  More information:  Maximum length: 256 characters
        """
        return self.__order_description

    @order_description.setter
    def order_description(self, value):
        self.__order_description = value
    @property
    def order_amount(self):
        """Gets the order_amount of this Order.
        
        """
        return self.__order_amount

    @order_amount.setter
    def order_amount(self, value):
        self.__order_amount = value
    @property
    def order_discount_amount(self):
        """Gets the order_discount_amount of this Order.
        
        """
        return self.__order_discount_amount

    @order_discount_amount.setter
    def order_discount_amount(self, value):
        self.__order_discount_amount = value
    @property
    def sub_total_order_amount(self):
        """Gets the sub_total_order_amount of this Order.
        
        """
        return self.__sub_total_order_amount

    @sub_total_order_amount.setter
    def sub_total_order_amount(self, value):
        self.__sub_total_order_amount = value
    @property
    def merchant(self):
        """Gets the merchant of this Order.
        
        """
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        self.__merchant = value
    @property
    def goods(self):
        """
        Goods information, including the ID, name, price, and quantity of the goods in the order.   Note: Specify this parameter if you require risk control. Providing this information helps to increase the accuracy of anti-money laundering and fraud detection, and increase payment success rates.  More information:  Maximum size: 100 elements
        """
        return self.__goods

    @goods.setter
    def goods(self, value):
        self.__goods = value
    @property
    def shipping(self):
        """Gets the shipping of this Order.
        
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value):
        self.__shipping = value
    @property
    def buyer(self):
        """Gets the buyer of this Order.
        
        """
        return self.__buyer

    @buyer.setter
    def buyer(self, value):
        self.__buyer = value
    @property
    def env(self):
        """Gets the env of this Order.
        
        """
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value
    @property
    def extend_info(self):
        """
        Extended information data, including information for special use cases.  Note: Specify this field when you need to use the extended information.  
        """
        return self.__extend_info

    @extend_info.setter
    def extend_info(self, value):
        self.__extend_info = value
    @property
    def transit(self):
        """Gets the transit of this Order.
        
        """
        return self.__transit

    @transit.setter
    def transit(self, value):
        self.__transit = value
    @property
    def lodging(self):
        """Gets the lodging of this Order.
        
        """
        return self.__lodging

    @lodging.setter
    def lodging(self, value):
        self.__lodging = value
    @property
    def gaming(self):
        """Gets the gaming of this Order.
        
        """
        return self.__gaming

    @gaming.setter
    def gaming(self, value):
        self.__gaming = value
    @property
    def need_declaration(self):
        """Gets the need_declaration of this Order.
        
        """
        return self.__need_declaration

    @need_declaration.setter
    def need_declaration(self, value):
        self.__need_declaration = value
    @property
    def declaration(self):
        """Gets the declaration of this Order.
        
        """
        return self.__declaration

    @declaration.setter
    def declaration(self, value):
        self.__declaration = value
    @property
    def order_type(self):
        """
        test 
        """
        return self.__order_type

    @order_type.setter
    def order_type(self, value):
        self.__order_type = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "reference_order_id") and self.reference_order_id is not None:
            params['referenceOrderId'] = self.reference_order_id
        if hasattr(self, "order_description") and self.order_description is not None:
            params['orderDescription'] = self.order_description
        if hasattr(self, "order_amount") and self.order_amount is not None:
            params['orderAmount'] = self.order_amount
        if hasattr(self, "order_discount_amount") and self.order_discount_amount is not None:
            params['orderDiscountAmount'] = self.order_discount_amount
        if hasattr(self, "sub_total_order_amount") and self.sub_total_order_amount is not None:
            params['subTotalOrderAmount'] = self.sub_total_order_amount
        if hasattr(self, "merchant") and self.merchant is not None:
            params['merchant'] = self.merchant
        if hasattr(self, "goods") and self.goods is not None:
            params['goods'] = self.goods
        if hasattr(self, "shipping") and self.shipping is not None:
            params['shipping'] = self.shipping
        if hasattr(self, "buyer") and self.buyer is not None:
            params['buyer'] = self.buyer
        if hasattr(self, "env") and self.env is not None:
            params['env'] = self.env
        if hasattr(self, "extend_info") and self.extend_info is not None:
            params['extendInfo'] = self.extend_info
        if hasattr(self, "transit") and self.transit is not None:
            params['transit'] = self.transit
        if hasattr(self, "lodging") and self.lodging is not None:
            params['lodging'] = self.lodging
        if hasattr(self, "gaming") and self.gaming is not None:
            params['gaming'] = self.gaming
        if hasattr(self, "need_declaration") and self.need_declaration is not None:
            params['needDeclaration'] = self.need_declaration
        if hasattr(self, "declaration") and self.declaration is not None:
            params['declaration'] = self.declaration
        if hasattr(self, "order_type") and self.order_type is not None:
            params['orderType'] = self.order_type
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'referenceOrderId' in response_body:
            self.__reference_order_id = response_body['referenceOrderId']
        if 'orderDescription' in response_body:
            self.__order_description = response_body['orderDescription']
        if 'orderAmount' in response_body:
            self.__order_amount = Amount()
            self.__order_amount.parse_rsp_body(response_body['orderAmount'])
        if 'orderDiscountAmount' in response_body:
            self.__order_discount_amount = Amount()
            self.__order_discount_amount.parse_rsp_body(response_body['orderDiscountAmount'])
        if 'subTotalOrderAmount' in response_body:
            self.__sub_total_order_amount = Amount()
            self.__sub_total_order_amount.parse_rsp_body(response_body['subTotalOrderAmount'])
        if 'merchant' in response_body:
            self.__merchant = Merchant()
            self.__merchant.parse_rsp_body(response_body['merchant'])
        if 'goods' in response_body:
            self.__goods = []
            for item in response_body['goods']:
                obj = Goods()
                obj.parse_rsp_body(item)
                self.__goods.append(obj)
        if 'shipping' in response_body:
            self.__shipping = Shipping()
            self.__shipping.parse_rsp_body(response_body['shipping'])
        if 'buyer' in response_body:
            self.__buyer = Buyer()
            self.__buyer.parse_rsp_body(response_body['buyer'])
        if 'env' in response_body:
            self.__env = Env()
            self.__env.parse_rsp_body(response_body['env'])
        if 'extendInfo' in response_body:
            self.__extend_info = response_body['extendInfo']
        if 'transit' in response_body:
            self.__transit = Transit()
            self.__transit.parse_rsp_body(response_body['transit'])
        if 'lodging' in response_body:
            self.__lodging = Lodging()
            self.__lodging.parse_rsp_body(response_body['lodging'])
        if 'gaming' in response_body:
            self.__gaming = Gaming()
            self.__gaming.parse_rsp_body(response_body['gaming'])
        if 'needDeclaration' in response_body:
            self.__need_declaration = response_body['needDeclaration']
        if 'declaration' in response_body:
            self.__declaration = Declaration()
            self.__declaration.parse_rsp_body(response_body['declaration'])
        if 'orderType' in response_body:
            self.__order_type = response_body['orderType']

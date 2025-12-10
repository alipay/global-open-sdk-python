import json
from com.alipay.ams.api.model.payment_method_type_item import PaymentMethodTypeItem




class AvailablePaymentMethod:
    def __init__(self):
        
        self.__payment_method_meta_data = None  # type: {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}
        self.__payment_method_type_list = None  # type: [PaymentMethodTypeItem]
        

    @property
    def payment_method_meta_data(self):
        """
        Additional information required for some specific payment methods.  
        """
        return self.__payment_method_meta_data

    @payment_method_meta_data.setter
    def payment_method_meta_data(self, value):
        self.__payment_method_meta_data = value
    @property
    def payment_method_type_list(self):
        """Gets the payment_method_type_list of this AvailablePaymentMethod.
        
        """
        return self.__payment_method_type_list

    @payment_method_type_list.setter
    def payment_method_type_list(self, value):
        self.__payment_method_type_list = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_method_meta_data") and self.payment_method_meta_data is not None:
            params['paymentMethodMetaData'] = self.payment_method_meta_data
        if hasattr(self, "payment_method_type_list") and self.payment_method_type_list is not None:
            params['paymentMethodTypeList'] = self.payment_method_type_list
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'paymentMethodMetaData' in response_body:
            self.__payment_method_meta_data = response_body['paymentMethodMetaData']
        if 'paymentMethodTypeList' in response_body:
            self.__payment_method_type_list = []
            for item in response_body['paymentMethodTypeList']:
                obj = PaymentMethodTypeItem()
                obj.parse_rsp_body(item)
                self.__payment_method_type_list.append(obj)

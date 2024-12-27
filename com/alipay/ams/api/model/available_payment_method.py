from com.alipay.ams.api.model.payment_method_type_item import PaymentMethodTypeItem


class AvailablePaymentMethod:

    def __init__(self):
        self.__payment_method_type_list = None #type: list[PaymentMethodTypeItem]


    @property
    def payment_method_type_list(self):
        return self.__payment_method_type_list

    @payment_method_type_list.setter
    def payment_method_type_list(self, payment_method_type_list):
        if not isinstance(payment_method_type_list, list):
            raise TypeError("payment_method_type_list should be list[PaymentMethodTypeItem]")

        for item in payment_method_type_list:
            if not isinstance(item, PaymentMethodTypeItem):
                raise TypeError("item should be type of PaymentMethodTypeItem")

        self.__payment_method_type_list = payment_method_type_list


    def to_ams_dict(self):
        params = dict()
        if self.__payment_method_type_list is not None:
            params['paymentMethodTypeList'] = [item.to_ams_dict() for item in self.__payment_method_type_list]

        return params
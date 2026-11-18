import json




class AuthorizationConsultSubscriptionParams:
    def __init__(self):
        
        self.__subscribe_tpl_type = None  # type: str
        self.__first_subscription_info = None  # type: str
        self.__follow_subscription_infos = None  # type: str
        self.__origin_subscription_info = None  # type: str
        self.__target_subscription_info = None  # type: str
        self.__next_payment_date = None  # type: str
        self.__expire_at = None  # type: str
        self.__base_amount = None  # type: str
        self.__offset_amount = None  # type: str
        self.__deduct_name = None  # type: str
        self.__deduct_desc = None  # type: str
        

    @property
    def subscribe_tpl_type(self):
        """
        Required when directDebitInfo is provided for periodic signing. Null, empty and blank values are invalid. CREATE maps to CREATE or SEAT_CREATE; TRIAL to TRIAL; UPDATE to UPGRADE, SEAT_INCREASE or SEAT_DECREASE; DOWNGRADE to DOWNGRADE; REVERT_CANCEL to REVERT_CANCEL. Use only enabled action/template combinations. Allowed values: CREATE, TRIAL, UPGRADE, DOWNGRADE, SEAT_CREATE, SEAT_INCREASE, SEAT_DECREASE, REVERT_CANCEL. The subscription page template. It must match the signing action and the enabled channel capability.
        """
        return self.__subscribe_tpl_type

    @subscribe_tpl_type.setter
    def subscribe_tpl_type(self, value):
        self.__subscribe_tpl_type = value
    @property
    def first_subscription_info(self):
        """
        A serialized JSON object string, not a nested JSON object. Its fields retain camelCase: title, price, period, periodCount, paymentDay, currentPeriodStart, currentPeriodEnd, nextPaymentDate, discountName, discountAmount, labelName and quantity. Prices and discounts are CNY yuan strings; periodCount is a positive integer string; dates use YYYY-MM-DD. Populate only the fields required by the selected page block using the actual subscription data. Provide when creation, promotion or trial requires a first-period/trial block. Ordinary CREATE includes title, price, period, periodCount, currentPeriodStart and nextPaymentDate. Do not require this block for updates that use original and target snapshots.
        """
        return self.__first_subscription_info

    @first_subscription_info.setter
    def first_subscription_info(self, value):
        self.__first_subscription_info = value
    @property
    def follow_subscription_infos(self):
        """
        A serialized JSON array string, not a JSON array. Each element uses the same page-snapshot fields described for firstSubscriptionInfo. Provide only for enabled scenarios with different first and subsequent prices or periods; omit for ordinary same-price CREATE. Preserve camelCase keys and actual phase prices and dates.
        """
        return self.__follow_subscription_infos

    @follow_subscription_infos.setter
    def follow_subscription_infos(self, value):
        self.__follow_subscription_infos = value
    @property
    def origin_subscription_info(self):
        """
        A serialized JSON object string, not a nested JSON object. Its fields retain camelCase: title, price, period, periodCount, paymentDay, currentPeriodStart, currentPeriodEnd, nextPaymentDate, discountName, discountAmount, labelName and quantity. Prices and discounts are CNY yuan strings; periodCount is a positive integer string; dates use YYYY-MM-DD. Populate only the fields required by the selected page block using the actual subscription data. Required when upgrade, downgrade, seat increase or seat decrease displays the original subscription. Omit for creation or trial. Use the original plan and actual current-period dates.
        """
        return self.__origin_subscription_info

    @origin_subscription_info.setter
    def origin_subscription_info(self, value):
        self.__origin_subscription_info = value
    @property
    def target_subscription_info(self):
        """
        A serialized JSON object string, not a nested JSON object. Its fields retain camelCase: title, price, period, periodCount, paymentDay, currentPeriodStart, currentPeriodEnd, nextPaymentDate, discountName, discountAmount, labelName and quantity. Prices and discounts are CNY yuan strings; periodCount is a positive integer string; dates use YYYY-MM-DD. Populate only the fields required by the selected page block using the actual subscription data. Required when upgrade, downgrade, seat increase, seat decrease or restoration displays the target subscription. Use the target plan and next payment date consistent with the authorization rules.
        """
        return self.__target_subscription_info

    @target_subscription_info.setter
    def target_subscription_info(self, value):
        self.__target_subscription_info = value
    @property
    def next_payment_date(self):
        """
        Provide the page-summary next payment date for update or restoration when required by the template. Format: YYYY-MM-DD. This outer field is distinct from the date inside each snapshot; dates for the same payment plan must agree.
        """
        return self.__next_payment_date

    @next_payment_date.setter
    def next_payment_date(self, value):
        self.__next_payment_date = value
    @property
    def expire_at(self):
        """
        Provide when a period-end change needs to display the current subscription or period expiration date. Format: YYYY-MM-DD. It is not the signing request expiration time and does not replace agreement-state validation.
        """
        return self.__expire_at

    @expire_at.setter
    def expire_at(self, value):
        self.__expire_at = value
    @property
    def base_amount(self):
        """
        Provide for a personal upgrade when the page requires the amount before offsetting the remaining subscription value. Use a CNY yuan string with two decimal places. This field is outside the snapshot strings.
        """
        return self.__base_amount

    @base_amount.setter
    def base_amount(self, value):
        self.__base_amount = value
    @property
    def offset_amount(self):
        """
        Provide for a personal upgrade when the page requires the remaining-value offset. Use a CNY yuan string with two decimal places. The upgrade payment difference is baseAmount minus offsetAmount; consult does not execute that payment. This field is outside the snapshot strings.
        """
        return self.__offset_amount

    @offset_amount.setter
    def offset_amount(self, value):
        self.__offset_amount = value
    @property
    def deduct_name(self):
        """
        Provide only when a separate deduction name is needed; otherwise omit. It must agree with the displayed service name. Omission uses existing channel display behavior without adding an SDK default.
        """
        return self.__deduct_name

    @deduct_name.setter
    def deduct_name(self, value):
        self.__deduct_name = value
    @property
    def deduct_desc(self):
        """
        Provide only when a separate deduction description is needed; otherwise omit. It must agree with the displayed seat or billing information. Omission does not add an SDK default.
        """
        return self.__deduct_desc

    @deduct_desc.setter
    def deduct_desc(self, value):
        self.__deduct_desc = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "subscribe_tpl_type") and self.subscribe_tpl_type is not None:
            params['subscribeTplType'] = self.subscribe_tpl_type
        if hasattr(self, "first_subscription_info") and self.first_subscription_info is not None:
            params['firstSubscriptionInfo'] = self.first_subscription_info
        if hasattr(self, "follow_subscription_infos") and self.follow_subscription_infos is not None:
            params['followSubscriptionInfos'] = self.follow_subscription_infos
        if hasattr(self, "origin_subscription_info") and self.origin_subscription_info is not None:
            params['originSubscriptionInfo'] = self.origin_subscription_info
        if hasattr(self, "target_subscription_info") and self.target_subscription_info is not None:
            params['targetSubscriptionInfo'] = self.target_subscription_info
        if hasattr(self, "next_payment_date") and self.next_payment_date is not None:
            params['nextPaymentDate'] = self.next_payment_date
        if hasattr(self, "expire_at") and self.expire_at is not None:
            params['expireAt'] = self.expire_at
        if hasattr(self, "base_amount") and self.base_amount is not None:
            params['baseAmount'] = self.base_amount
        if hasattr(self, "offset_amount") and self.offset_amount is not None:
            params['offsetAmount'] = self.offset_amount
        if hasattr(self, "deduct_name") and self.deduct_name is not None:
            params['deductName'] = self.deduct_name
        if hasattr(self, "deduct_desc") and self.deduct_desc is not None:
            params['deductDesc'] = self.deduct_desc
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'subscribeTplType' in response_body:
            self.__subscribe_tpl_type = response_body['subscribeTplType']
        if 'firstSubscriptionInfo' in response_body:
            self.__first_subscription_info = response_body['firstSubscriptionInfo']
        if 'followSubscriptionInfos' in response_body:
            self.__follow_subscription_infos = response_body['followSubscriptionInfos']
        if 'originSubscriptionInfo' in response_body:
            self.__origin_subscription_info = response_body['originSubscriptionInfo']
        if 'targetSubscriptionInfo' in response_body:
            self.__target_subscription_info = response_body['targetSubscriptionInfo']
        if 'nextPaymentDate' in response_body:
            self.__next_payment_date = response_body['nextPaymentDate']
        if 'expireAt' in response_body:
            self.__expire_at = response_body['expireAt']
        if 'baseAmount' in response_body:
            self.__base_amount = response_body['baseAmount']
        if 'offsetAmount' in response_body:
            self.__offset_amount = response_body['offsetAmount']
        if 'deductName' in response_body:
            self.__deduct_name = response_body['deductName']
        if 'deductDesc' in response_body:
            self.__deduct_desc = response_body['deductDesc']

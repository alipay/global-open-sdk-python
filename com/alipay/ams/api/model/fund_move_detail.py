import json




class FundMoveDetail:
    def __init__(self):
        
        self.__payer_name = None  # type: str
        self.__payer_account_no = None  # type: str
        self.__payer_chaneel_accountnumber = None  # type: str
        self.__payer_account_type = None  # type: str
        self.__payer_asset_id = None  # type: str
        self.__beneficiary_name = None  # type: str
        self.__beneficiary_account_type = None  # type: str
        self.__beneficiary_bank_country = None  # type: str
        self.__beneficiary_bank_name = None  # type: str
        self.__beneficiary_asset_id = None  # type: str
        self.__remarks = None  # type: str
        self.__description = None  # type: str
        self.__memo = None  # type: str
        self.__reference_transaction_id = None  # type: str
        

    @property
    def payer_name(self):
        """
        付款人姓名
        """
        return self.__payer_name

    @payer_name.setter
    def payer_name(self, value):
        self.__payer_name = value
    @property
    def payer_account_no(self):
        """
        付款人账号
        """
        return self.__payer_account_no

    @payer_account_no.setter
    def payer_account_no(self, value):
        self.__payer_account_no = value
    @property
    def payer_chaneel_accountnumber(self):
        """
        付款渠道账号
        """
        return self.__payer_chaneel_accountnumber

    @payer_chaneel_accountnumber.setter
    def payer_chaneel_accountnumber(self, value):
        self.__payer_chaneel_accountnumber = value
    @property
    def payer_account_type(self):
        """
        付款人账户类型
        """
        return self.__payer_account_type

    @payer_account_type.setter
    def payer_account_type(self, value):
        self.__payer_account_type = value
    @property
    def payer_asset_id(self):
        """
        付款人资产ID
        """
        return self.__payer_asset_id

    @payer_asset_id.setter
    def payer_asset_id(self, value):
        self.__payer_asset_id = value
    @property
    def beneficiary_name(self):
        """
        受益人姓名
        """
        return self.__beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, value):
        self.__beneficiary_name = value
    @property
    def beneficiary_account_type(self):
        """
        受益人账户类型
        """
        return self.__beneficiary_account_type

    @beneficiary_account_type.setter
    def beneficiary_account_type(self, value):
        self.__beneficiary_account_type = value
    @property
    def beneficiary_bank_country(self):
        """
        受益人银行所在国家
        """
        return self.__beneficiary_bank_country

    @beneficiary_bank_country.setter
    def beneficiary_bank_country(self, value):
        self.__beneficiary_bank_country = value
    @property
    def beneficiary_bank_name(self):
        """
        受益人银行名称
        """
        return self.__beneficiary_bank_name

    @beneficiary_bank_name.setter
    def beneficiary_bank_name(self, value):
        self.__beneficiary_bank_name = value
    @property
    def beneficiary_asset_id(self):
        """
        受益人资产ID
        """
        return self.__beneficiary_asset_id

    @beneficiary_asset_id.setter
    def beneficiary_asset_id(self, value):
        self.__beneficiary_asset_id = value
    @property
    def remarks(self):
        """
        备注
        """
        return self.__remarks

    @remarks.setter
    def remarks(self, value):
        self.__remarks = value
    @property
    def description(self):
        """
        描述
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def memo(self):
        """
        备忘录
        """
        return self.__memo

    @memo.setter
    def memo(self, value):
        self.__memo = value
    @property
    def reference_transaction_id(self):
        """
        参考交易ID
        """
        return self.__reference_transaction_id

    @reference_transaction_id.setter
    def reference_transaction_id(self, value):
        self.__reference_transaction_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "payer_name") and self.payer_name is not None:
            params['payerName'] = self.payer_name
        if hasattr(self, "payer_account_no") and self.payer_account_no is not None:
            params['payerAccountNo'] = self.payer_account_no
        if hasattr(self, "payer_chaneel_accountnumber") and self.payer_chaneel_accountnumber is not None:
            params['payerChaneelAccountnumber'] = self.payer_chaneel_accountnumber
        if hasattr(self, "payer_account_type") and self.payer_account_type is not None:
            params['payerAccountType'] = self.payer_account_type
        if hasattr(self, "payer_asset_id") and self.payer_asset_id is not None:
            params['payerAssetId'] = self.payer_asset_id
        if hasattr(self, "beneficiary_name") and self.beneficiary_name is not None:
            params['beneficiaryName'] = self.beneficiary_name
        if hasattr(self, "beneficiary_account_type") and self.beneficiary_account_type is not None:
            params['beneficiaryAccountType'] = self.beneficiary_account_type
        if hasattr(self, "beneficiary_bank_country") and self.beneficiary_bank_country is not None:
            params['beneficiaryBankCountry'] = self.beneficiary_bank_country
        if hasattr(self, "beneficiary_bank_name") and self.beneficiary_bank_name is not None:
            params['beneficiaryBankName'] = self.beneficiary_bank_name
        if hasattr(self, "beneficiary_asset_id") and self.beneficiary_asset_id is not None:
            params['beneficiaryAssetId'] = self.beneficiary_asset_id
        if hasattr(self, "remarks") and self.remarks is not None:
            params['remarks'] = self.remarks
        if hasattr(self, "description") and self.description is not None:
            params['description'] = self.description
        if hasattr(self, "memo") and self.memo is not None:
            params['memo'] = self.memo
        if hasattr(self, "reference_transaction_id") and self.reference_transaction_id is not None:
            params['referenceTransactionId'] = self.reference_transaction_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'payerName' in response_body:
            self.__payer_name = response_body['payerName']
        if 'payerAccountNo' in response_body:
            self.__payer_account_no = response_body['payerAccountNo']
        if 'payerChaneelAccountnumber' in response_body:
            self.__payer_chaneel_accountnumber = response_body['payerChaneelAccountnumber']
        if 'payerAccountType' in response_body:
            self.__payer_account_type = response_body['payerAccountType']
        if 'payerAssetId' in response_body:
            self.__payer_asset_id = response_body['payerAssetId']
        if 'beneficiaryName' in response_body:
            self.__beneficiary_name = response_body['beneficiaryName']
        if 'beneficiaryAccountType' in response_body:
            self.__beneficiary_account_type = response_body['beneficiaryAccountType']
        if 'beneficiaryBankCountry' in response_body:
            self.__beneficiary_bank_country = response_body['beneficiaryBankCountry']
        if 'beneficiaryBankName' in response_body:
            self.__beneficiary_bank_name = response_body['beneficiaryBankName']
        if 'beneficiaryAssetId' in response_body:
            self.__beneficiary_asset_id = response_body['beneficiaryAssetId']
        if 'remarks' in response_body:
            self.__remarks = response_body['remarks']
        if 'description' in response_body:
            self.__description = response_body['description']
        if 'memo' in response_body:
            self.__memo = response_body['memo']
        if 'referenceTransactionId' in response_body:
            self.__reference_transaction_id = response_body['referenceTransactionId']

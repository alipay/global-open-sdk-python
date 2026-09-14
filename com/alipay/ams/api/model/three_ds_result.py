import json




class ThreeDSResult:
    def __init__(self):
        
        self.__three_ds_version = None  # type: str
        self.__eci = None  # type: str
        self.__cavv = None  # type: str
        self.__ds_transaction_id = None  # type: str
        self.__xid = None  # type: str
        self.__three_d_stransaction_status_reason = None  # type: str
        self.__challenge_cancel = None  # type: str
        self.__challenged = None  # type: bool
        self.__exemption_type = None  # type: str
        self.__three_ds_offered = None  # type: bool
        self.__pa_res_status = None  # type: str
        self.__liability_shift = None  # type: int
        

    @property
    def three_ds_version(self):
        """
        The version of 3D Secure protocol. Valid values are:  1.0.2 2.1.0 2.2.0  
        """
        return self.__three_ds_version

    @three_ds_version.setter
    def three_ds_version(self, value):
        self.__three_ds_version = value
    @property
    def eci(self):
        """
        Electronic Commerce Indicator (ECI) that is returned by the card scheme. This parameter is used to indicate the type of cardholder identity authentication. Valid values are:  02 or 05: Indicates fully authenticated transaction. 01 or 06: Indicates attempted authentication transaction. 00 or 07: Indicates non-3D Secure transaction. 04: Indicates 3D Secure data-only transaction. No authentication required (for Mastercard only). Note: This parameter is returned when the value of paymentMethodType is CARD and the issuing bank returns this data.
        """
        return self.__eci

    @eci.setter
    def eci(self, value):
        self.__eci = value
    @property
    def cavv(self):
        """
        The cardholder authentication value. The value of this parameter can be Cardholder Authentication Verification Value (CAVV) or Authentication Verification Value (AVV).  Note: This parameter is returned when the cardholder passes the 3D Secure authentication.
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value):
        self.__cavv = value
    @property
    def ds_transaction_id(self):
        """
        The unique transaction identifier assigned by the Directory Server (DS) for 3D Secure authentication.    Note: This parameter is returned for 3D Secure 2.0.
        """
        return self.__ds_transaction_id

    @ds_transaction_id.setter
    def ds_transaction_id(self, value):
        self.__ds_transaction_id = value
    @property
    def xid(self):
        """
        The unique transaction identifier assigned by the Directory Server (DS) for 3D Secure authentication.     Note: This parameter is returned for 3D Secure 1.0. 
        """
        return self.__xid

    @xid.setter
    def xid(self, value):
        self.__xid = value
    @property
    def three_d_stransaction_status_reason(self):
        """
        When a transaction is unsuccessful due to 3D Secure authentication failure, you may receive the transaction status reason code returned by this parameter, indicating the reason for the failure.
        """
        return self.__three_d_stransaction_status_reason

    @three_d_stransaction_status_reason.setter
    def three_d_stransaction_status_reason(self, value):
        self.__three_d_stransaction_status_reason = value
    @property
    def challenge_cancel(self):
        """
        Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. Possible values are:  01: Cardholder selected cancel. 02: 3DS Requestor cancelled authentication. 03: Transaction abandoned. 04: Transaction timed out at ACS — other timeouts. 05: Transaction timed out at ACS — the first Client Request not received by ACS. 06: Transaction error. 07: Unknown. 08: Transaction timed out at SDK.
        """
        return self.__challenge_cancel

    @challenge_cancel.setter
    def challenge_cancel(self, value):
        self.__challenge_cancel = value
    @property
    def challenged(self):
        """
        Indicates whether a 3DS challenge was triggered. Valid values are:  true: The transaction has been challenged, and the user is required to complete the 3D Secure authentication process. false: The transaction is a frictionless process, where the user does not experience the 3D Secure authentication process.
        """
        return self.__challenged

    @challenged.setter
    def challenged(self, value):
        self.__challenged = value
    @property
    def exemption_type(self):
        """
        The exemption type that Antom requested during 3DS authentication, specified through the 3DS requestor challenge indicator. Valid values are:  dataOnly: Transactions where shopper data is shared with the card schemes directly using the 3DS2 infrastructure. This flow is currently only available for Visa and Mastercard outside PSD2 SCA regulated markets. lowValue: Transactions below €30 may be exempt from Strong Customer Authentication, if certain cumulative amount and transaction count criteria are met. transactionRiskAnalysis: Transactions considered at low risk of fraud based on the fraud level of the payment provider.
        """
        return self.__exemption_type

    @exemption_type.setter
    def exemption_type(self, value):
        self.__exemption_type = value
    @property
    def three_ds_offered(self):
        """
        Indicates whether 3D Secure authentication was triggered for the payment. Valid values are:  true: indicates 3D Secure authentication was triggered for the payment. Determine the authentication result by combining the other returned 3D Secure parameters. false: indicates 3D Secure authentication was not triggered for the payment. Note: This parameter may be returned even if the payment fails.
        """
        return self.__three_ds_offered

    @three_ds_offered.setter
    def three_ds_offered(self, value):
        self.__three_ds_offered = value
    @property
    def pa_res_status(self):
        """
        Payer Authentication Response Status returned by the issuer or authentication system during 3D Secure authentication. Valid values are: Y (successful authentication), N (failed authentication or transaction denied), U (unable to complete authentication), A (successful attempts transaction), C (challenge required), R (authentication rejected; authorization must not be attempted), D (decoupled authentication challenge confirmed), and I (informational only). D and I are intermediate authentication states and require no merchant action; use paymentStatus and resultCode as the authoritative payment outcome. This field is returned only when paymentMethodType is CARD, threeDSOffered is true, and threeDSResult is returned. If these conditions are met but the channel does not provide a value, the JSON value can be null; otherwise the property is omitted.
        """
        return self.__pa_res_status

    @pa_res_status.setter
    def pa_res_status(self, value):
        self.__pa_res_status = value
    @property
    def liability_shift(self):
        """
        Indicates whether liability has shifted for the transaction. Valid values are: 1 (yes), 0 (no), and -1 (unknown). The upstream channel value is passed through when available; otherwise Antom calculates the value from CAVV and ECI according to card-network rules, and returns -1 only when the value cannot be determined. Treat -1 as liability not shifted for chargeback decisions. This field does not determine the payment outcome and is returned only when paymentMethodType is CARD, threeDSOffered is true, and threeDSResult is returned; otherwise the property is omitted.
        """
        return self.__liability_shift

    @liability_shift.setter
    def liability_shift(self, value):
        self.__liability_shift = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "three_ds_version") and self.three_ds_version is not None:
            params['threeDSVersion'] = self.three_ds_version
        if hasattr(self, "eci") and self.eci is not None:
            params['eci'] = self.eci
        if hasattr(self, "cavv") and self.cavv is not None:
            params['cavv'] = self.cavv
        if hasattr(self, "ds_transaction_id") and self.ds_transaction_id is not None:
            params['dsTransactionId'] = self.ds_transaction_id
        if hasattr(self, "xid") and self.xid is not None:
            params['xid'] = self.xid
        if hasattr(self, "three_d_stransaction_status_reason") and self.three_d_stransaction_status_reason is not None:
            params['threeDStransactionStatusReason'] = self.three_d_stransaction_status_reason
        if hasattr(self, "challenge_cancel") and self.challenge_cancel is not None:
            params['challengeCancel'] = self.challenge_cancel
        if hasattr(self, "challenged") and self.challenged is not None:
            params['challenged'] = self.challenged
        if hasattr(self, "exemption_type") and self.exemption_type is not None:
            params['exemptionType'] = self.exemption_type
        if hasattr(self, "three_ds_offered") and self.three_ds_offered is not None:
            params['threeDSOffered'] = self.three_ds_offered
        if hasattr(self, "pa_res_status") and self.pa_res_status is not None:
            params['paResStatus'] = self.pa_res_status
        if hasattr(self, "liability_shift") and self.liability_shift is not None:
            params['liabilityShift'] = self.liability_shift
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'threeDSVersion' in response_body:
            self.__three_ds_version = response_body['threeDSVersion']
        if 'eci' in response_body:
            self.__eci = response_body['eci']
        if 'cavv' in response_body:
            self.__cavv = response_body['cavv']
        if 'dsTransactionId' in response_body:
            self.__ds_transaction_id = response_body['dsTransactionId']
        if 'xid' in response_body:
            self.__xid = response_body['xid']
        if 'threeDStransactionStatusReason' in response_body:
            self.__three_d_stransaction_status_reason = response_body['threeDStransactionStatusReason']
        if 'challengeCancel' in response_body:
            self.__challenge_cancel = response_body['challengeCancel']
        if 'challenged' in response_body:
            self.__challenged = response_body['challenged']
        if 'exemptionType' in response_body:
            self.__exemption_type = response_body['exemptionType']
        if 'threeDSOffered' in response_body:
            self.__three_ds_offered = response_body['threeDSOffered']
        if 'paResStatus' in response_body:
            self.__pa_res_status = response_body['paResStatus']
        if 'liabilityShift' in response_body:
            self.__liability_shift = response_body['liabilityShift']

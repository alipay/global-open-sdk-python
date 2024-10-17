from enum import Enum

class AntomPathConstants(Enum):
    """
    Ant Group
    Copyright (c) 2004-2024 All Rights Reserved.
    """
    AUTH_CONSULT_PATH = "/ams/api/v1/authorizations/consult"
    AUTH_APPLY_TOKEN_PATH = "/ams/api/v1/authorizations/applyToken"
    AUTH_REVOKE_PATH = "/ams/api/v1/authorizations/revoke"
    AUTH_QUERY_PATH = "/ams/api/v1/authorizations/query"

    CREATE_VAULTING_SESSION_PATH = "/ams/api/v1/vaults/createVaultingSession"
    VAULT_PAYMENT_METHOD_PATH = "/ams/api/v1/vaults/vaultPaymentMethod"
    INQUIRE_VAULTING_PATH = "/ams/api/v1/vaults/inquireVaulting"

    CONSULT_PAYMENT_PATH = "/ams/api/v1/payments/consult"
    PAYMENT_PATH = "/ams/api/v1/payments/pay"
    CREATE_SESSION_PATH = "/ams/api/v1/payments/createPaymentSession"
    CAPTURE_PATH = "/ams/api/v1/payments/capture"
    INQUIRY_PAYMENT_PATH = "/ams/api/v1/payments/inquiryPayment"
    CANCEL_PATH = "/ams/api/v1/payments/cancel"
    SYNC_ARREAR_PATH = "/ams/api/v1/payments/syncArrear"
    CREATE_DEVICE_CERTIFICATE_PATH = "/ams/api/v1/payments/createDeviceCertificate"

    SUBSCRIPTION_CREATE_PATH = "/ams/api/v1/subscriptions/create"
    SUBSCRIPTION_CHANGE_PATH = "/ams/api/v1/subscriptions/change"
    SUBSCRIPTION_CANCEL_PATH = "/ams/api/v1/subscriptions/cancel"

    ACCEPT_DISPUTE_PATH = "/ams/api/v1/payments/acceptDispute"
    SUPPLY_DEFENCE_DOC_PATH = "/ams/api/v1/payments/supplyDefenseDocument"
    DOWNLOAD_DISPUTE_EVIDENCE_PATH = "/ams/api/v1/payments/downloadDisputeEvidence"

    REFUND_PATH = "/ams/api/v1/payments/refund"
    INQUIRY_REFUND_PATH = "/ams/api/v1/payments/inquiryRefund"

    DECLARE_PATH = "/ams/api/v1/customs/declare"
    INQUIRY_DECLARE_PATH = "/ams/api/v1/customs/inquiryDeclarationRequests"

    MARKETPLACE_SUBMITATTACHMENT_PATH = "/ams/api/open/openapiv2_file/v1/business/attachment/submitAttachment"
    MARKETPLACE_REGISTER_PATH = "/ams/api/v1/merchants/register"
    MARKETPLACE_SETTLEMENTINFO_UPDATE_PATH = "/ams/api/v1/merchants/settlementInfo/update"
    MARKETPLACE_INQUIREBALANCE_PATH = "/ams/api/v1/accounts/inquireBalance"
    MARKETPLACE_SETTLE_PATH = "/ams/api/v1/payments/settle"
    MARKETPLACE_CREATEPAYOUT_PATH = "/ams/api/v1/funds/createPayout"
    MARKETPLACE_CREATETRANSFER_PATH = "/ams/api/v1/funds/createTransfer"

    RISK_DECIDE_PATH = "/ams/api/v1/risk/payments/decide"
    RISK_REPORT_PATH = "/ams/api/v1/risk/payments/reportRisk"
    RISK_SEND_PAYMENT_RESULT_PATH = "/ams/api/v1/risk/payments/sendPaymentResult"
    RISK_SEND_REFUND_RESULT_PATH = "/ams/api/v1/risk/payments/sendRefundResult"

    MERCHANTS_INQUIRY_REGISTRATION_PATH  ="/ams/api/v1/merchants/inquiryRegistrationInfo"
    MERCHANTS_REGISTRATION_PATH = "/ams/api/v1/merchants/registration"
    MERCHANTS_INQUIRY_REGISTRATION_STATUS_PATH = "/ams/api/v1/merchants/inquiryRegistrationStatus"
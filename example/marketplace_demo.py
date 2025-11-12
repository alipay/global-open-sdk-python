import json
import uuid

from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.model.account_holder_type import AccountHolderType
from com.alipay.ams.api.model.account_type import AccountType
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.amount import Amount
from com.alipay.ams.api.model.association_type import AssociationType
from com.alipay.ams.api.model.attachment import Attachment
from com.alipay.ams.api.model.attachment_type import AttachmentType
from com.alipay.ams.api.model.business_info import BusinessInfo
from com.alipay.ams.api.model.certificate import Certificate
from com.alipay.ams.api.model.certificate_type import CertificateType
from com.alipay.ams.api.model.company import Company
from com.alipay.ams.api.model.companyType import CompanyType
from com.alipay.ams.api.model.entity_associations import EntityAssociations
from com.alipay.ams.api.model.individual import Individual
from com.alipay.ams.api.model.legal_entity_type import LegalEntityType
from com.alipay.ams.api.model.merchant_info import MerchantInfo
from com.alipay.ams.api.model.payment_method import PaymentMethod
from com.alipay.ams.api.model.payment_method_type import PaymentMethodType
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.model.settle_to_type import SettleToType
from com.alipay.ams.api.model.settlement_bank_account import SettlementBankAccount
from com.alipay.ams.api.model.settlement_detail import SettlementDetail
from com.alipay.ams.api.model.settlement_info import SettlementInfo
from com.alipay.ams.api.model.transfer_from_detail import TransferFromDetail
from com.alipay.ams.api.model.transfer_to_detail import TransferToDetail
from com.alipay.ams.api.model.user_name import UserName
from com.alipay.ams.api.model.web_site import WebSite
from com.alipay.ams.api.request.marketplace.alipay_create_payout_request import AlipayCreatePayoutRequest
from com.alipay.ams.api.request.marketplace.alipay_create_transfer_request import AlipayCreateTransferRequest
from com.alipay.ams.api.request.marketplace.alipay_inquire_balance_request import AlipayInquireBalanceRequest
from com.alipay.ams.api.request.marketplace.alipay_register_request import AlipayRegisterRequest
from com.alipay.ams.api.request.marketplace.alipay_settle_request import AlipaySettleRequest
from com.alipay.ams.api.request.marketplace.alipay_settlement_info_update_request import \
    AlipaySettlementInfoUpdateRequest
from com.alipay.ams.api.request.pay.alipay_pay_request import AlipayPayRequest
from com.alipay.ams.api.response.marketplace.alipay_create_payout_response import AlipayCreatePayoutResponse
from com.alipay.ams.api.response.marketplace.alipay_create_transfer_response import AlipayCreateTransferResponse
from com.alipay.ams.api.response.marketplace.alipay_inquire_balance_response import AlipayInquireBalanceResponse
from com.alipay.ams.api.response.marketplace.alipay_register_response import AlipayRegisterResponse
from com.alipay.ams.api.response.marketplace.alipay_settle_response import AlipaySettleResponse
from com.alipay.ams.api.response.marketplace.alipay_settlement_info_update_response import \
    AlipaySettlementInfoUpdateResponse

GATEWAY_HOST = "https://open-sea.alipay.com"
CLIENT_ID = "SANDBOX_5YC31G2ZNMQK07357"
MERCHANT_PRIVATE_KEY = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDhnOLYh3Tte5ELNzD6kr6TSN+F4oXaNlnKgx2aGf/xSSHIh1k+wihv6HbwPAexdtjpDQAgwEv4YXpdH3erQLuy3oBIBVsdbXWg09TRttyBeM8FzbMru6qR1TceypEPhR9W4/hP9DZEmn9XZmR7xR9KStDKJdnqSNr578IVFvp3hXUt2HfwoHbUwwOPbu8a66th9b1PyNJ5DOdSoTj52tvFMOyfCmKOn9U/bwtcT/EGEJFlIj1QjBSwlEeCBDUVwwKlo2ttMP5Omy7i4Lxi5NKAMdw+Cru49FqGEf9B/JKfovd6EcwrnUeDfXVltNrPJjdr19WzatDh0k0wE/9QT6EnAgMBAAECggEAZsbQdDFo69KRpZlT36I/3NqisNwbe+esidum/Y+Aj8tv72jxF+zc/PXaUOAX5RkuASSh/Ul8kj7dvlRacJJBr1868xQ1iLdXkZdOaOazluuQ66TkTTTlpB+MR6Oh538OYsfhU5L9sczr28XSWqvW8EIa0SvjFJ5x2tAFCxR3r0AqXFrRteHSPYI01sle9ynCq3frBQwX481N/T0YvDQNFiRw+YlzJwJsZqPooFA2H/o+AL+LQED7eevnLYvevNS4GGVkWNO7gfKFHJA3RCMJgRqsXfxs2SG2cBx6YBYCQ7JurP8veMr3NBf/OOGCZln4zY4Vl5bTXe5vxeT5gzm18QKBgQD/jCH38x0AIjx0zwpZyvcp6C/2PohVjb6B/TbAiMmaIjpei06DCXHrDiObTLoxguZfmA+ypiPTZBOwFEDo7wDJ8khQwRMx9ydPMiaWoFCvl5iSke2vs/ONxdw02zRGj2uivgqjDf+94eTS8aSTJ+7kt1KLq4ZQf80Efywv+0xVnwKBgQDiAy5MMU8oDiSun8FoSBX3SomjdOX/tg4hMZ2PKYnXTJFUJ5bkjLhgdsPO5WGcFGsdReuweTzKteIRmS0zvdekVIpWFchflyeIM3+OuI1ZJJG6t28Xg3e8VOXCD917fjLnOOmH3f7PV/rj59wVM0yPvGStlAbPP0kwrcci8Wo3eQKBgQDE/ujctGwhw0KppUVMbRtWEeiPQitlEGzQ1jtT9t661DH82hT/DNPlqLOoL2DFdCxVeup3BH5PojFPJn3XUw9fnkdDAWPju6xw768xpIouooV6T8ZUETvqiaG0mVrWHg+SmD+o7My+OxpjxuXgjwMpC201wFc9TRflpIeSwX1Z7wKBgQCpUgy7VC2jKoVctZ6ly2t5akQXSxqMKg4H3C3X9RypSVmPHGG1M59l1VP4imxIDBv7QEjEWu+qRfzphkIRA2asXBGPUJ5eztT0+u/TMnvijr0GjyoRCZMIaun+KviY7gCgrUh3W17sY1M4rpl44Ie5H0ClscIwPY9NgsMvcIFMsQKBgG/XoSq4KjB+/SFdLTH4ITLb6Q8rvWOOyu6OvTBCgfxhq4R+rBP/40bvd1Ax5Eawfwq/GDfUL5jpzoaJGXGXDI90eXdeDOHZB7rq/+un9De1jPLGc1Ty7YT3SctYAvFw8jo0K65eckL7AaiGHk39eOXrWmJVVchOVlkX8TayiTgk"
ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq7zEydi4Q2VvUIb1Mjpm/I2R3NVWcSMddlhvHYJADZ07YOGjvlQPbH3iixhLMnk1Y0tT7Sw7B1Ov1kXDGUhnui/YmGQBDbz9vg4iPDXA8OU7TaSsIk2BbP4+uZoortx2AZu/ABTGBDvyhLyJBkNplJ7196Np+IMaxi2RlT2NEAV4vFIurUcfFl5vvMliyV1SacvIyONkurzixSLirlKBl35t1mGm44xqh7M40tcMScgdF8pIdkzVz0nAnBcGb0aTeD3YLQmYFFmbQhWIe7MAa0BPEK7sxTJ1x1PbRUCHEXiZURnPjZTD7FBsTfLlcGOlOe0DXB7mrWm+AP+fVBjbAwIDAQAB"


def register():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_register_request = AlipayRegisterRequest()
    alipay_register_request.registration_request_id = str(uuid.uuid4())

    settlement_info = SettlementInfo()
    settlement_info.settlement_currency = "BRL"
    settlementBankAccount = SettlementBankAccount()
    settlementBankAccount.branch_code = "1234"
    settlementBankAccount.routing_number = "12"
    settlementBankAccount.bank_region = "BR"
    settlementBankAccount.account_type = AccountType.CHECKING
    settlementBankAccount.account_holder_tIN = "12345678901"
    settlementBankAccount.account_holder_name = "Jane Doe"
    settlementBankAccount.bank_account_no = "12345678901"
    settlementBankAccount.account_holder_type = AccountHolderType.ENTERPRISE
    settlement_info.settlement_bank_account = settlementBankAccount
    alipay_register_request.settlement_infos = [settlement_info]

    merchant_info = MerchantInfo()
    merchant_info.login_id = str(uuid.uuid4())[:6] + "@alipay.com"
    merchant_info.legal_entity_type = LegalEntityType.COMPANY
    company = Company()
    company.legal_name = "Alipay"
    address = Address()
    address.region = "BR"
    address.city = "Sao Paulo"
    address.address1 = "Rua dos bobos"
    address.postal_code = "12345678"
    company.registered_address = address
    company.company_type = CompanyType.LTDA
    company.operating_address = address
    attachment = Attachment()
    attachment.attachment_name = "test.jpg"
    attachment.file_key = "test"
    attachment.attachment_type = AttachmentType.ARTICLES_OF_ASSOCIATION
    company.attachments = [attachment]

    certificate = Certificate()
    certificate.certificate_no = "123124"
    certificate.certificate_type = CertificateType.ENTERPRISE_REGISTRATION
    company.certificates = [certificate]

    merchant_info.company = company

    businessInfo = BusinessInfo()
    businessInfo.doingBusinessAs = "businessName_DBA"
    webSite = WebSite()
    webSite.url = "https://www.alipay.com"
    businessInfo.websites = [webSite]
    merchant_info.business_info = businessInfo
    merchant_info.reference_merchant_id = str(uuid.uuid4())

    entityAssociations = EntityAssociations()
    individual = Individual()
    certificate1 = Certificate()
    certificate1.certificate_no = "1234"
    certificate1.certificate_type = CertificateType.CPF
    individual.certificates = [certificate1]
    username = UserName()
    username.full_name = "Jane Doe"
    username.first_name = "Jane"
    username.last_name = "Doe"
    individual.name = username
    individual.date_of_birth = "1990-01-01"
    individual.resident_address = address
    entityAssociations.individual = individual
    entityAssociations.legal_entity_type = LegalEntityType.INDIVIDUAL
    entityAssociations.association_type = AssociationType.LEGAL_REPRESENTATIVE

    entityAssociations1 = EntityAssociations()
    individual1 = Individual()
    certificate2 = Certificate()
    certificate2.certificate_no = "1234"
    certificate2.certificate_type = CertificateType.CPF
    certificate2.file_keys = ["13124325235235"]
    individual1.certificates = [certificate2]
    username = UserName()
    username.first_name = "Jane"
    username.last_name = "Doe"
    username.full_name = "Jane Doe"
    individual1.name = username
    individual1.date_of_birth = "1990-01-01"
    individual1.resident_address = address
    entityAssociations1.individual = individual1
    entityAssociations1.legal_entity_type = LegalEntityType.INDIVIDUAL
    entityAssociations1.association_type = AssociationType.UBO

    merchant_info.entity_associations = [entityAssociations, entityAssociations1]

    alipay_register_request.merchant_info = merchant_info

    rsp_body = default_alipay_client.execute(alipay_register_request)

    alipay_register_response = AlipayRegisterResponse(rsp_body)

    if alipay_register_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_register_response.result.result_status.name)
        print(alipay_register_response.result.result_message)
        print(alipay_register_response.registration_status)
    else:
        print(alipay_register_response.result.result_message)


def update(referenceMerchantId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_settlement_info_update_request = AlipaySettlementInfoUpdateRequest()
    alipay_settlement_info_update_request.reference_merchant_id = referenceMerchantId
    alipay_settlement_info_update_request.update_request_id = str(uuid.uuid4())
    alipay_settlement_info_update_request.settlement_currency = "BRL"
    settlementBankAccount = SettlementBankAccount()
    settlementBankAccount.branch_code = "1234"
    settlementBankAccount.routing_number = "12"
    settlementBankAccount.bank_region = "BR"
    settlementBankAccount.account_type = AccountType.CHECKING
    settlementBankAccount.account_holder_tIN = "12345678901"
    settlementBankAccount.account_holder_name = "Jane Doe"
    settlementBankAccount.bank_account_no = "12345678901"
    settlementBankAccount.account_holder_type = AccountHolderType.ENTERPRISE
    alipay_settlement_info_update_request.settlement_bank_account = settlementBankAccount

    rsp_body = default_alipay_client.execute(alipay_settlement_info_update_request)
    response = AlipaySettlementInfoUpdateResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.update_status)
        print(response.result.result_message)
    else:
        print(response.result.result_message)


def queryBanlance(referenceMerchantId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_inquire_balance_request = AlipayInquireBalanceRequest()
    alipay_inquire_balance_request.reference_merchant_id = referenceMerchantId

    rsp_body = default_alipay_client.execute(alipay_inquire_balance_request)
    response = AlipayInquireBalanceResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response.account_balances)
        print(response.result.result_message)
    else:
        print(response.result.result_message)


def settleRequest(paymentId):
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_settle_request = AlipaySettleRequest()
    alipay_settle_request.settlement_request_id = str(uuid.uuid4())
    alipay_settle_request.payment_id = paymentId
    settlementDetail = SettlementDetail()
    settlementDetail.settle_to = SettleToType.SELLER
    settlementDetail.settlement_amount = Amount("BRL", "90")

    settlementDetail1 = SettlementDetail()
    settlementDetail1.settle_to = SettleToType.MARKETPLACE
    settlementDetail1.settlement_amount = Amount("BRL", "10")

    alipay_settle_request.settlement_details = [settlementDetail, settlementDetail1]

    rsp_body = default_alipay_client.execute(alipay_settle_request)
    response = AlipaySettleResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response)
    else:
        print(response.result.result_message)


def createPayout():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_create_payout_request = AlipayCreatePayoutRequest()
    alipay_create_payout_request.transfer_requestId = str(uuid.uuid4())

    transfer_from_detail = TransferFromDetail()
    payment_method = PaymentMethod()
    payment_method.payment_method_id = str(uuid.uuid4())
    payment_method.payment_method_type = PaymentMethodType.BALANCE_ACCOUNT
    alipay_create_payout_request.transfer_from_detail = transfer_from_detail

    transfer_to_detail = TransferToDetail()
    payment_method1 = PaymentMethod()
    payment_method1.payment_method_id = str(uuid.uuid4())
    payment_method1.payment_method_type = PaymentMethodType.SETTLEMENT_CARD
    transfer_to_detail.payment_method = payment_method1
    transfer_to_detail.transfer_to_currency = "BRL"
    transfer_to_detail.purpose_code = "GSD"
    transfer_to_detail.transfer_notify_url = "https://www.yourNotifyUrl.com"
    alipay_create_payout_request.transfer_to_detail = transfer_to_detail

    rsp_body = default_alipay_client.execute(alipay_create_payout_request)
    response = AlipayCreatePayoutResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response)
    else:
        print(response.result.result_message)


def createTransfer():
    default_alipay_client = DefaultAlipayClient(GATEWAY_HOST, CLIENT_ID, MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_create_transfer_request = AlipayCreateTransferRequest()
    alipay_create_transfer_request.transfer_request_id = str(uuid.uuid4())

    transfer_from_detail = TransferFromDetail()
    payment_method = PaymentMethod()
    payment_method.payment_method_id = str(uuid.uuid4())
    payment_method.payment_method_type = PaymentMethodType.BALANCE_ACCOUNT
    transfer_from_detail.transfer_from_amount = Amount("BRL", "100")
    alipay_create_transfer_request.transfer_from_detail = transfer_from_detail

    transfer_to_detail = TransferToDetail()
    payment_method1 = PaymentMethod()
    payment_method1.payment_method_id = str(uuid.uuid4())
    payment_method1.payment_method_type = PaymentMethodType.BALANCE_ACCOUNT
    transfer_to_detail.payment_method = payment_method1
    transfer_to_detail.transfer_to_currency = "BRL"
    transfer_to_detail.purpose_code = "GSD"
    transfer_to_detail.transfer_notify_url = "https://www.yourNotifyUrl.com"
    alipay_create_transfer_request.transfer_to_detail = transfer_to_detail

    rsp_body = default_alipay_client.execute(alipay_create_transfer_request)
    response = AlipayCreateTransferResponse(rsp_body)

    if response.result.result_status.name != ResultStatusType.F.name:
        print(response)
    else:
        print(response.result.result_message)


register()
# update("mid_zhangtianren_ztr_20230807_180716_981")
# queryBanlance("mid_zhangtianren_ztr_20230807_180716_981")
from com.alipay.ams.api.default_alipay_client import DefaultAlipayClient
from com.alipay.ams.api.model.address import Address
from com.alipay.ams.api.model.attachment import Attachment
from com.alipay.ams.api.model.contact_info import ContactInfo
from com.alipay.ams.api.model.logo import Logo
from com.alipay.ams.api.model.merchant_registration_info import MerchantRegistrationInfo
from com.alipay.ams.api.model.registration_detail import RegistrationDetail
from com.alipay.ams.api.model.result_status_type import ResultStatusType
from com.alipay.ams.api.model.web_site import WebSite
from com.alipay.ams.api.request.merchant.alipay_merchant_registration_info_query_request import \
    AlipayMerchantRegistrationInfoQueryRequest
from com.alipay.ams.api.request.merchant.alipay_merchant_registration_request import AlipayMerchantRegistrationRequest
from com.alipay.ams.api.request.merchant.alipay_merchant_registration_status_query_request import \
    AlipayMerchantRegistrationStatusQueryRequest
from com.alipay.ams.api.response.merchant.alipay_merchant_registration_info_query_response import \
    AlipayMerchantRegistrationInfoQueryResponse
from com.alipay.ams.api.response.merchant.alipay_merchant_registration_response import \
    AlipayMerchantRegistrationResponse
from com.alipay.ams.api.response.merchant.alipay_merchant_registration_status_query_response import \
    AlipayMerchantRegistrationStatusQueryResponse

MERCHANT_PRIVATE_KEY = ""
ALIPAY_PUBLIC_KEY = ""
CLIENT_ID = ""


def register():
    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLIC_KEY)

    alipay_merchant_registration_request = AlipayMerchantRegistrationRequest()
    alipay_merchant_registration_request.registration_request_id = "reqId107336691327831097346773_test_111"
    alipay_merchant_registration_request.pass_through_info = "{\"acquiringCurrency\":[\"HKD\"],\"settlementType\":\"DOMESTIC_SETTLEMENT\",\"legalRepresentativeName\":\"legalRepresentativeName\"}"
    alipay_merchant_registration_request.registration_notify_url = "http://xmock.inc.alipay.net/api/Test/yibeiTest/testPayNotify1.htm"
    alipay_merchant_registration_request.path = "/ams/sandbox/api/v1/merchants/registration"
    alipay_merchant_registration_request.product_codes = ["AGREEMENT_PAYMENT"]

    merchant_info = MerchantRegistrationInfo()
    merchant_info.reference_merchant_id = "reference_merchant_id_test07"

    logo = Logo()
    logo.logo_url = "http://www.logo.com"
    logo.logo_name = "logoName"
    merchant_info.logo = logo

    merchant_address = Address()
    merchant_address.city = "hong kong"
    merchant_address.label = "label"
    merchant_address.state = "HK"
    merchant_address.region = "HK"
    merchant_address.address1 = "58 Leighton Road, ****"
    merchant_address.address2 = "28 Leighton Road, ****"
    merchant_address.zip_code = "zipCode"

    merchant_info.merchant_address = merchant_address
    merchant_info.merchant_mcc = "merchantMcc_test66"
    merchant_info.merchant_display_name = "merchantXXXX"

    registration_detail = RegistrationDetail()
    attachment1 = Attachment()
    attachment1.file = "file_test_1"
    attachment1.attachment_name = "attachment_name_test1"
    attachment1.attachment_type = "ARTICLES_OF_ASSOCIATION"

    attachment2 = Attachment()
    attachment2.file = "file_test_2"
    attachment2.attachment_name = "attachment_name_test2"
    attachment2.attachment_type = "ARTICLES_OF_ASSOCIATION"

    registration_detail.attachments = [attachment1, attachment2]

    registration_detail.business_type = "ENTERPRISE"

    contact_info = ContactInfo()
    contact_info.contact_no = "contactNo123"
    contact_info.contact_type = "MOBILE_PHONE"

    registration_detail.contact_info = [contact_info]
    registration_detail.legal_name = "Example Legal Name"
    registration_address = Address()
    registration_address.city = "hong kong"
    registration_address.label = "label"
    registration_address.state = "HK"
    registration_address.region = "HK"
    registration_address.address1 = "58 Leighton Road, ****"
    registration_address.address2 = "28 Leighton Road, ****"
    registration_address.zip_code = "zipCode"

    registration_detail.registration_address = registration_address

    registration_detail.registration_effective_date = "2020-01-01T12:08:55+08:00"
    registration_detail.registration_expire_date = "2022-01-01T12:08:55+08:00"

    registration_detail.registration_no = "registrati_on_*****"
    registration_detail.registration_type = "ENTERPRISE_REGISTRATION_NO"

    merchant_info.registration_detail = registration_detail
    website1 = WebSite()
    website1.name = "websiteName1"
    website1.url = "http://www.website1.com"
    website1.desc = "website1 desc"

    website2 = WebSite()
    website2.name = "websiteName2"
    website2.url = "http://www.website2.com"
    website2.desc = "website2 desc"

    merchant_info.websites = [website1, website2]

    alipay_merchant_registration_request.merchant_info = merchant_info

    print(alipay_merchant_registration_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_merchant_registration_request)

    alipay_merchant_registration_response = AlipayMerchantRegistrationResponse(rsp_body)

    print(alipay_merchant_registration_response.result.result_message)


def query_info():
    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", CLIENT_ID, MERCHANT_PRIVATE_KEY,
                                                ALIPAY_PUBLIC_KEY)
    alipay_merchant_registration_info_query_request = AlipayMerchantRegistrationInfoQueryRequest()
    alipay_merchant_registration_info_query_request.path = "/ams/sandbox/api/v1/merchants/inquiryRegistrationInfo"

    alipay_merchant_registration_info_query_request.reference_merchant_id = "5188122826664900663130"

    print(alipay_merchant_registration_info_query_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_merchant_registration_info_query_request)
    alipay_merchant_registration_info_response = AlipayMerchantRegistrationInfoQueryResponse(rsp_body)
    if alipay_merchant_registration_info_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_merchant_registration_info_response.product_codes)
        print(alipay_merchant_registration_info_response.merchant_info)
    else:
        print(alipay_merchant_registration_info_response.result.result_message)


def query_registration_status():
    default_alipay_client = DefaultAlipayClient("https://open-na.alipay.com", CLIENT_ID,
                                                MERCHANT_PRIVATE_KEY, ALIPAY_PUBLIC_KEY)
    alipay_merchant_registration_status_query_request = AlipayMerchantRegistrationStatusQueryRequest()
    alipay_merchant_registration_status_query_request.path = "/ams/sandbox/api/v1/merchants/inquiryRegistrationStatus"

    alipay_merchant_registration_status_query_request.reference_merchant_id = "5188122826664900663130"

    print(alipay_merchant_registration_status_query_request.to_ams_json())

    rsp_body = default_alipay_client.execute(alipay_merchant_registration_status_query_request)
    alipay_merchant_registration_status_response = AlipayMerchantRegistrationStatusQueryResponse(rsp_body)
    if alipay_merchant_registration_status_response.result.result_status.name != ResultStatusType.F.name:
        print(alipay_merchant_registration_status_response.psp_registration_result_list)
        print(alipay_merchant_registration_status_response.registration_result)
    else:
        print(alipay_merchant_registration_status_response.result.result_message)


register()

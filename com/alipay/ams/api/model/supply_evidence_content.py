import json
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile
from com.alipay.ams.api.model.evidence_file import EvidenceFile




class SupplyEvidenceContent:
    def __init__(self):
        
        self.__merchant_order_no = None  # type: str
        self.__product_description = None  # type: str
        self.__product_unit_price = None  # type: str
        self.__quantity = None  # type: str
        self.__original_order_receipt_file = None  # type: EvidenceFile
        self.__receiver_name = None  # type: str
        self.__receiver_email_address = None  # type: str
        self.__receiver_contact_number = None  # type: str
        self.__customer_communications = None  # type: str
        self.__customer_communications_file = None  # type: EvidenceFile
        self.__return_and_refund_policy = None  # type: str
        self.__return_and_refund_policy_file = None  # type: EvidenceFile
        self.__cancellation_policy = None  # type: str
        self.__cancellation_policy_file = None  # type: EvidenceFile
        self.__subscription_policy = None  # type: str
        self.__subscription_policy_file = None  # type: EvidenceFile
        self.__payment_policy = None  # type: str
        self.__payment_policy_file = None  # type: EvidenceFile
        self.__certification_records = None  # type: str
        self.__certification_records_file = None  # type: EvidenceFile
        self.__merchant_comments = None  # type: str
        self.__merchant_comments_file = None  # type: EvidenceFile
        self.__marketing_materials_and_listings = None  # type: str
        self.__marketing_materials_and_listings_file = None  # type: EvidenceFile
        self.__usage_records_of_recurring_service = None  # type: str
        self.__usage_records_of_recurring_service_file = None  # type: EvidenceFile
        self.__transaction_date = None  # type: str
        self.__transaction_amount = None  # type: str
        self.__transaction_currency = None  # type: str
        self.__arn = None  # type: str
        self.__order_description = None  # type: str
        self.__payment_auth_mode = None  # type: str
        self.__ip_address = None  # type: str
        self.__supplement_proof = None  # type: str
        self.__supplement_proof_file = None  # type: EvidenceFile
        self.__refund_method = None  # type: str
        self.__refunded_amount = None  # type: str
        self.__refund_finished_time = None  # type: str
        self.__booking_confirmation_terms = None  # type: str
        self.__booking_confirmation_terms_file = None  # type: EvidenceFile
        self.__offline_signed_agreement = None  # type: str
        self.__offline_signed_agreement_file = None  # type: EvidenceFile
        self.__installment_billing_agreement = None  # type: str
        self.__installment_billing_agreement_file = None  # type: EvidenceFile
        self.__tracking_number = None  # type: str
        self.__post_code = None  # type: str
        self.__shipping_address = None  # type: str
        self.__tracking_url = None  # type: str
        self.__proof_of_shipment_file = None  # type: EvidenceFile
        self.__logistic_screenshot_file = None  # type: EvidenceFile
        self.__picture_of_dispatched_item_file = None  # type: EvidenceFile
        self.__user_recharge_account_number = None  # type: str
        self.__digital_product_completion_file = None  # type: EvidenceFile
        self.__service_completion_file = None  # type: EvidenceFile
        self.__order_number = None  # type: str
        self.__booking_time = None  # type: str
        self.__air_route = None  # type: str
        self.__number_of_passenger = None  # type: str
        self.__passenger_name = None  # type: str
        self.__booking_reference_number = None  # type: str
        self.__ticket_number = None  # type: str
        self.__order_status = None  # type: str
        self.__order_amount = None  # type: str
        self.__total_payment_amount = None  # type: str
        self.__flight_route = None  # type: str
        self.__flight_no = None  # type: str
        self.__cabin_class = None  # type: str
        self.__departure_time = None  # type: str
        self.__arrival_time = None  # type: str
        self.__ticket_status = None  # type: str
        self.__baggage = None  # type: str
        self.__reservation_confirmation_number = None  # type: str
        self.__hotel_name = None  # type: str
        self.__hotel_address = None  # type: str
        self.__check_in_date = None  # type: str
        self.__check_out_date = None  # type: str
        self.__number_of_guest = None  # type: str
        self.__guest_name = None  # type: str
        self.__pre_payment_fees = None  # type: str
        self.__accommodation_fee_per_night = None  # type: str
        self.__number_of_night = None  # type: str
        self.__additional_service_charge = None  # type: str
        self.__city_tax = None  # type: str
        self.__checkout_payment = None  # type: str
        self.__supplement_proof_file_list = None  # type: [EvidenceFile]
        

    @property
    def merchant_order_no(self):
        """
        The merchant order number. Applicable tags: ORDER_INFORMATION, REFUND_INFORMATION, PROOF_OF_DIGITAL_ACCESS, PROOF_OF_SERVICE_COMPLETION. Required for ORDER_INFORMATION, REFUND_INFORMATION, PROOF_OF_DIGITAL_ACCESS, PROOF_OF_SERVICE_COMPLETION when that tag is submitted.
        """
        return self.__merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self.__merchant_order_no = value
    @property
    def product_description(self):
        """
        The product description. Required when the dispute reason concerns goods or services not matching their description; optional otherwise. Applicable tags: ORDER_INFORMATION.
        """
        return self.__product_description

    @product_description.setter
    def product_description(self, value):
        self.__product_description = value
    @property
    def product_unit_price(self):
        """
        The product unit price as a numeric string. Applicable tags: ORDER_INFORMATION.
        """
        return self.__product_unit_price

    @product_unit_price.setter
    def product_unit_price(self, value):
        self.__product_unit_price = value
    @property
    def quantity(self):
        """
        The quantity as a positive integer string. Applicable tags: ORDER_INFORMATION.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    @property
    def original_order_receipt_file(self):
        """Gets the original_order_receipt_file of this SupplyEvidenceContent.
        
        """
        return self.__original_order_receipt_file

    @original_order_receipt_file.setter
    def original_order_receipt_file(self, value):
        self.__original_order_receipt_file = value
    @property
    def receiver_name(self):
        """
        The recipient&#39;s name. Applicable tags: ORDER_INFORMATION.
        """
        return self.__receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self.__receiver_name = value
    @property
    def receiver_email_address(self):
        """
        The recipient&#39;s email address. Applicable tags: ORDER_INFORMATION.
        """
        return self.__receiver_email_address

    @receiver_email_address.setter
    def receiver_email_address(self, value):
        self.__receiver_email_address = value
    @property
    def receiver_contact_number(self):
        """
        The recipient&#39;s contact number. Applicable tags: ORDER_INFORMATION.
        """
        return self.__receiver_contact_number

    @receiver_contact_number.setter
    def receiver_contact_number(self, value):
        self.__receiver_contact_number = value
    @property
    def customer_communications(self):
        """
        Communication records as text. Applicable tags: CUSTOMER_COMMUNICATIONS. at least one of customerCommunications or customerCommunicationsFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__customer_communications

    @customer_communications.setter
    def customer_communications(self, value):
        self.__customer_communications = value
    @property
    def customer_communications_file(self):
        """Gets the customer_communications_file of this SupplyEvidenceContent.
        
        """
        return self.__customer_communications_file

    @customer_communications_file.setter
    def customer_communications_file(self, value):
        self.__customer_communications_file = value
    @property
    def return_and_refund_policy(self):
        """
        The return and refund policy as text or a link. Applicable tags: RETURN_AND_REFUND_POLICY. at least one of returnAndRefundPolicy or returnAndRefundPolicyFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__return_and_refund_policy

    @return_and_refund_policy.setter
    def return_and_refund_policy(self, value):
        self.__return_and_refund_policy = value
    @property
    def return_and_refund_policy_file(self):
        """Gets the return_and_refund_policy_file of this SupplyEvidenceContent.
        
        """
        return self.__return_and_refund_policy_file

    @return_and_refund_policy_file.setter
    def return_and_refund_policy_file(self, value):
        self.__return_and_refund_policy_file = value
    @property
    def cancellation_policy(self):
        """
        The cancellation policy as text or a link. Applicable tags: CANCELLATION_POLICY. at least one of cancellationPolicy or cancellationPolicyFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__cancellation_policy

    @cancellation_policy.setter
    def cancellation_policy(self, value):
        self.__cancellation_policy = value
    @property
    def cancellation_policy_file(self):
        """Gets the cancellation_policy_file of this SupplyEvidenceContent.
        
        """
        return self.__cancellation_policy_file

    @cancellation_policy_file.setter
    def cancellation_policy_file(self, value):
        self.__cancellation_policy_file = value
    @property
    def subscription_policy(self):
        """
        The subscription renewal policy as text or a link. Applicable tags: SUBSCRIPTION_POLICY. at least one of subscriptionPolicy or subscriptionPolicyFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__subscription_policy

    @subscription_policy.setter
    def subscription_policy(self, value):
        self.__subscription_policy = value
    @property
    def subscription_policy_file(self):
        """Gets the subscription_policy_file of this SupplyEvidenceContent.
        
        """
        return self.__subscription_policy_file

    @subscription_policy_file.setter
    def subscription_policy_file(self, value):
        self.__subscription_policy_file = value
    @property
    def payment_policy(self):
        """
        The platform payment rules as text or a link. Applicable tags: PAYMENT_POLICY. at least one of paymentPolicy or paymentPolicyFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__payment_policy

    @payment_policy.setter
    def payment_policy(self, value):
        self.__payment_policy = value
    @property
    def payment_policy_file(self):
        """Gets the payment_policy_file of this SupplyEvidenceContent.
        
        """
        return self.__payment_policy_file

    @payment_policy_file.setter
    def payment_policy_file(self, value):
        self.__payment_policy_file = value
    @property
    def certification_records(self):
        """
        Certification records as text or a link. Applicable tags: CERTIFICATION_RECORDS. at least one of certificationRecords or certificationRecordsFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__certification_records

    @certification_records.setter
    def certification_records(self, value):
        self.__certification_records = value
    @property
    def certification_records_file(self):
        """Gets the certification_records_file of this SupplyEvidenceContent.
        
        """
        return self.__certification_records_file

    @certification_records_file.setter
    def certification_records_file(self, value):
        self.__certification_records_file = value
    @property
    def merchant_comments(self):
        """
        Merchant comments or remarks as text or a link. Applicable tags: MERCHANT_COMMENTS. at least one of merchantComments or merchantCommentsFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__merchant_comments

    @merchant_comments.setter
    def merchant_comments(self, value):
        self.__merchant_comments = value
    @property
    def merchant_comments_file(self):
        """Gets the merchant_comments_file of this SupplyEvidenceContent.
        
        """
        return self.__merchant_comments_file

    @merchant_comments_file.setter
    def merchant_comments_file(self, value):
        self.__merchant_comments_file = value
    @property
    def marketing_materials_and_listings(self):
        """
        Product marketing images and statements as text or a link. Applicable tags: MARKETING_MATERIALS_AND_LISTINGS. at least one of marketingMaterialsAndListings or marketingMaterialsAndListingsFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__marketing_materials_and_listings

    @marketing_materials_and_listings.setter
    def marketing_materials_and_listings(self, value):
        self.__marketing_materials_and_listings = value
    @property
    def marketing_materials_and_listings_file(self):
        """Gets the marketing_materials_and_listings_file of this SupplyEvidenceContent.
        
        """
        return self.__marketing_materials_and_listings_file

    @marketing_materials_and_listings_file.setter
    def marketing_materials_and_listings_file(self, value):
        self.__marketing_materials_and_listings_file = value
    @property
    def usage_records_of_recurring_service(self):
        """
        Historical recurring service usage records as text or a link. Applicable tags: USAGE_RECORDS_OF_RECURRING_SERVICE. at least one of usageRecordsOfRecurringService or usageRecordsOfRecurringServiceFile must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__usage_records_of_recurring_service

    @usage_records_of_recurring_service.setter
    def usage_records_of_recurring_service(self, value):
        self.__usage_records_of_recurring_service = value
    @property
    def usage_records_of_recurring_service_file(self):
        """Gets the usage_records_of_recurring_service_file of this SupplyEvidenceContent.
        
        """
        return self.__usage_records_of_recurring_service_file

    @usage_records_of_recurring_service_file.setter
    def usage_records_of_recurring_service_file(self, value):
        self.__usage_records_of_recurring_service_file = value
    @property
    def transaction_date(self):
        """
        The historical transaction date as ISO 8601 text. Applicable tags: USER_HISTORY_UNDISPUTED_TRANSACTION. Required for USER_HISTORY_UNDISPUTED_TRANSACTION when that tag is submitted.
        """
        return self.__transaction_date

    @transaction_date.setter
    def transaction_date(self, value):
        self.__transaction_date = value
    @property
    def transaction_amount(self):
        """
        The historical transaction amount as a numeric string in the smallest unit of transactionCurrency. It need not equal the current disputed transaction amount. Applicable tags: USER_HISTORY_UNDISPUTED_TRANSACTION. Required for USER_HISTORY_UNDISPUTED_TRANSACTION when that tag is submitted.
        """
        return self.__transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value):
        self.__transaction_amount = value
    @property
    def transaction_currency(self):
        """
        The historical transaction&#39;s actual ISO 4217 currency. It need not match the current disputed transaction currency. Applicable tags: USER_HISTORY_UNDISPUTED_TRANSACTION. Required for USER_HISTORY_UNDISPUTED_TRANSACTION when that tag is submitted.
        """
        return self.__transaction_currency

    @transaction_currency.setter
    def transaction_currency(self, value):
        self.__transaction_currency = value
    @property
    def arn(self):
        """
        The clearing reference number. Applicable tags: USER_HISTORY_UNDISPUTED_TRANSACTION.
        """
        return self.__arn

    @arn.setter
    def arn(self, value):
        self.__arn = value
    @property
    def order_description(self):
        """
        The order description. Applicable tags: USER_HISTORY_UNDISPUTED_TRANSACTION.
        """
        return self.__order_description

    @order_description.setter
    def order_description(self, value):
        self.__order_description = value
    @property
    def payment_auth_mode(self):
        """
        The payment authorization mode. Applicable tags: USER_HISTORY_UNDISPUTED_TRANSACTION.
        """
        return self.__payment_auth_mode

    @payment_auth_mode.setter
    def payment_auth_mode(self, value):
        self.__payment_auth_mode = value
    @property
    def ip_address(self):
        """
        The order placement IP address, in IPv4 or IPv6 form. Applicable tags: USER_HISTORY_UNDISPUTED_TRANSACTION.
        """
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, value):
        self.__ip_address = value
    @property
    def supplement_proof(self):
        """
        Supplementary evidence as text. Applicable tags: USER_HISTORY_UNDISPUTED_TRANSACTION, ITINERARY_INFORMATION, HOTEL_RESERVATION_INFORMATION, HOTEL_BILL_INFORMATION, UNCATEGORIZED. Maximum length: 4096 characters for UNCATEGORIZED; 2048 characters for the other applicable tags. For UNCATEGORIZED, at least one of supplementProof or supplementProofFileList must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__supplement_proof

    @supplement_proof.setter
    def supplement_proof(self, value):
        self.__supplement_proof = value
    @property
    def supplement_proof_file(self):
        """Gets the supplement_proof_file of this SupplyEvidenceContent.
        
        """
        return self.__supplement_proof_file

    @supplement_proof_file.setter
    def supplement_proof_file(self, value):
        self.__supplement_proof_file = value
    @property
    def refund_method(self):
        """
        The refund method, such as a refund to the original payment method or a voucher. Applicable tags: REFUND_INFORMATION.
        """
        return self.__refund_method

    @refund_method.setter
    def refund_method(self, value):
        self.__refund_method = value
    @property
    def refunded_amount(self):
        """
        The refunded amount as a numeric string. Applicable tags: REFUND_INFORMATION.
        """
        return self.__refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, value):
        self.__refunded_amount = value
    @property
    def refund_finished_time(self):
        """
        The refund completion time as ISO 8601 text. Applicable tags: REFUND_INFORMATION.
        """
        return self.__refund_finished_time

    @refund_finished_time.setter
    def refund_finished_time(self, value):
        self.__refund_finished_time = value
    @property
    def booking_confirmation_terms(self):
        """
        The booking confirmation terms. Applicable tags: BOOKING_CONFIRMATION_TERMS.
        """
        return self.__booking_confirmation_terms

    @booking_confirmation_terms.setter
    def booking_confirmation_terms(self, value):
        self.__booking_confirmation_terms = value
    @property
    def booking_confirmation_terms_file(self):
        """Gets the booking_confirmation_terms_file of this SupplyEvidenceContent.
        
        """
        return self.__booking_confirmation_terms_file

    @booking_confirmation_terms_file.setter
    def booking_confirmation_terms_file(self, value):
        self.__booking_confirmation_terms_file = value
    @property
    def offline_signed_agreement(self):
        """
        The contents of the agreement signed offline. Applicable tags: OFFLINE_SIGNED_AGREEMENT.
        """
        return self.__offline_signed_agreement

    @offline_signed_agreement.setter
    def offline_signed_agreement(self, value):
        self.__offline_signed_agreement = value
    @property
    def offline_signed_agreement_file(self):
        """Gets the offline_signed_agreement_file of this SupplyEvidenceContent.
        
        """
        return self.__offline_signed_agreement_file

    @offline_signed_agreement_file.setter
    def offline_signed_agreement_file(self, value):
        self.__offline_signed_agreement_file = value
    @property
    def installment_billing_agreement(self):
        """
        The installment billing agreement contents. Applicable tags: INSTALLMENT_BILLING_AGREEMENT.
        """
        return self.__installment_billing_agreement

    @installment_billing_agreement.setter
    def installment_billing_agreement(self, value):
        self.__installment_billing_agreement = value
    @property
    def installment_billing_agreement_file(self):
        """Gets the installment_billing_agreement_file of this SupplyEvidenceContent.
        
        """
        return self.__installment_billing_agreement_file

    @installment_billing_agreement_file.setter
    def installment_billing_agreement_file(self, value):
        self.__installment_billing_agreement_file = value
    @property
    def tracking_number(self):
        """
        The shipment tracking number. Applicable tags: LOGISTIC_INFORMATION. Required for LOGISTIC_INFORMATION when that tag is submitted.
        """
        return self.__tracking_number

    @tracking_number.setter
    def tracking_number(self, value):
        self.__tracking_number = value
    @property
    def post_code(self):
        """
        The postal code. Applicable tags: LOGISTIC_INFORMATION.
        """
        return self.__post_code

    @post_code.setter
    def post_code(self, value):
        self.__post_code = value
    @property
    def shipping_address(self):
        """
        The recipient&#39;s shipping address. Applicable tags: LOGISTIC_INFORMATION.
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        self.__shipping_address = value
    @property
    def tracking_url(self):
        """
        The shipment tracking URL. Applicable tags: LOGISTIC_INFORMATION.
        """
        return self.__tracking_url

    @tracking_url.setter
    def tracking_url(self, value):
        self.__tracking_url = value
    @property
    def proof_of_shipment_file(self):
        """Gets the proof_of_shipment_file of this SupplyEvidenceContent.
        
        """
        return self.__proof_of_shipment_file

    @proof_of_shipment_file.setter
    def proof_of_shipment_file(self, value):
        self.__proof_of_shipment_file = value
    @property
    def logistic_screenshot_file(self):
        """Gets the logistic_screenshot_file of this SupplyEvidenceContent.
        
        """
        return self.__logistic_screenshot_file

    @logistic_screenshot_file.setter
    def logistic_screenshot_file(self, value):
        self.__logistic_screenshot_file = value
    @property
    def picture_of_dispatched_item_file(self):
        """Gets the picture_of_dispatched_item_file of this SupplyEvidenceContent.
        
        """
        return self.__picture_of_dispatched_item_file

    @picture_of_dispatched_item_file.setter
    def picture_of_dispatched_item_file(self, value):
        self.__picture_of_dispatched_item_file = value
    @property
    def user_recharge_account_number(self):
        """
        The buyer&#39;s recharge account. This is core evidence for non-receipt disputes concerning digital goods and cannot be empty. Applicable tags: PROOF_OF_DIGITAL_ACCESS. Required for PROOF_OF_DIGITAL_ACCESS when that tag is submitted.
        """
        return self.__user_recharge_account_number

    @user_recharge_account_number.setter
    def user_recharge_account_number(self, value):
        self.__user_recharge_account_number = value
    @property
    def digital_product_completion_file(self):
        """Gets the digital_product_completion_file of this SupplyEvidenceContent.
        
        """
        return self.__digital_product_completion_file

    @digital_product_completion_file.setter
    def digital_product_completion_file(self, value):
        self.__digital_product_completion_file = value
    @property
    def service_completion_file(self):
        """Gets the service_completion_file of this SupplyEvidenceContent.
        
        """
        return self.__service_completion_file

    @service_completion_file.setter
    def service_completion_file(self, value):
        self.__service_completion_file = value
    @property
    def order_number(self):
        """
        The order number. Applicable tags: FLIGHT_ORDER_SUMMARY, ITINERARY_INFORMATION. Required for FLIGHT_ORDER_SUMMARY, ITINERARY_INFORMATION when that tag is submitted.
        """
        return self.__order_number

    @order_number.setter
    def order_number(self, value):
        self.__order_number = value
    @property
    def booking_time(self):
        """
        The booking time as ISO 8601 text. Applicable tags: FLIGHT_ORDER_SUMMARY.
        """
        return self.__booking_time

    @booking_time.setter
    def booking_time(self, value):
        self.__booking_time = value
    @property
    def air_route(self):
        """
        The flight route. Applicable tags: FLIGHT_ORDER_SUMMARY.
        """
        return self.__air_route

    @air_route.setter
    def air_route(self, value):
        self.__air_route = value
    @property
    def number_of_passenger(self):
        """
        The passenger count as a string. Applicable tags: FLIGHT_ORDER_SUMMARY.
        """
        return self.__number_of_passenger

    @number_of_passenger.setter
    def number_of_passenger(self, value):
        self.__number_of_passenger = value
    @property
    def passenger_name(self):
        """
        The passenger name. Applicable tags: FLIGHT_ORDER_SUMMARY.
        """
        return self.__passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        self.__passenger_name = value
    @property
    def booking_reference_number(self):
        """
        The booking reference number. Applicable tags: FLIGHT_ORDER_SUMMARY.
        """
        return self.__booking_reference_number

    @booking_reference_number.setter
    def booking_reference_number(self, value):
        self.__booking_reference_number = value
    @property
    def ticket_number(self):
        """
        The electronic ticket number. Applicable tags: FLIGHT_ORDER_SUMMARY.
        """
        return self.__ticket_number

    @ticket_number.setter
    def ticket_number(self, value):
        self.__ticket_number = value
    @property
    def order_status(self):
        """
        The order status. Applicable tags: FLIGHT_ORDER_SUMMARY, HOTEL_RESERVATION_INFORMATION.
        """
        return self.__order_status

    @order_status.setter
    def order_status(self, value):
        self.__order_status = value
    @property
    def order_amount(self):
        """
        The order amount as a string. Applicable tags: FLIGHT_ORDER_SUMMARY.
        """
        return self.__order_amount

    @order_amount.setter
    def order_amount(self, value):
        self.__order_amount = value
    @property
    def total_payment_amount(self):
        """
        The total payment amount as a string. Applicable tags: FLIGHT_ORDER_SUMMARY.
        """
        return self.__total_payment_amount

    @total_payment_amount.setter
    def total_payment_amount(self, value):
        self.__total_payment_amount = value
    @property
    def flight_route(self):
        """
        The flight route. Applicable tags: ITINERARY_INFORMATION.
        """
        return self.__flight_route

    @flight_route.setter
    def flight_route(self, value):
        self.__flight_route = value
    @property
    def flight_no(self):
        """
        The flight number. Applicable tags: ITINERARY_INFORMATION.
        """
        return self.__flight_no

    @flight_no.setter
    def flight_no(self, value):
        self.__flight_no = value
    @property
    def cabin_class(self):
        """
        The cabin class. Applicable tags: ITINERARY_INFORMATION.
        """
        return self.__cabin_class

    @cabin_class.setter
    def cabin_class(self, value):
        self.__cabin_class = value
    @property
    def departure_time(self):
        """
        The departure time as ISO 8601 text. Applicable tags: ITINERARY_INFORMATION.
        """
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value
    @property
    def arrival_time(self):
        """
        The arrival time as ISO 8601 text. Applicable tags: ITINERARY_INFORMATION.
        """
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        self.__arrival_time = value
    @property
    def ticket_status(self):
        """
        The ticket status. Applicable tags: ITINERARY_INFORMATION.
        """
        return self.__ticket_status

    @ticket_status.setter
    def ticket_status(self, value):
        self.__ticket_status = value
    @property
    def baggage(self):
        """
        The baggage allowance. Applicable tags: ITINERARY_INFORMATION.
        """
        return self.__baggage

    @baggage.setter
    def baggage(self, value):
        self.__baggage = value
    @property
    def reservation_confirmation_number(self):
        """
        The reservation confirmation number. Applicable tags: HOTEL_RESERVATION_INFORMATION. Required for HOTEL_RESERVATION_INFORMATION when that tag is submitted.
        """
        return self.__reservation_confirmation_number

    @reservation_confirmation_number.setter
    def reservation_confirmation_number(self, value):
        self.__reservation_confirmation_number = value
    @property
    def hotel_name(self):
        """
        The hotel name. Applicable tags: HOTEL_RESERVATION_INFORMATION.
        """
        return self.__hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self.__hotel_name = value
    @property
    def hotel_address(self):
        """
        The hotel address. Applicable tags: HOTEL_RESERVATION_INFORMATION.
        """
        return self.__hotel_address

    @hotel_address.setter
    def hotel_address(self, value):
        self.__hotel_address = value
    @property
    def check_in_date(self):
        """
        The check-in date as ISO 8601 text. Applicable tags: HOTEL_RESERVATION_INFORMATION.
        """
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self.__check_in_date = value
    @property
    def check_out_date(self):
        """
        The check-out date as ISO 8601 text. Applicable tags: HOTEL_RESERVATION_INFORMATION.
        """
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        self.__check_out_date = value
    @property
    def number_of_guest(self):
        """
        The guest count as a string. Applicable tags: HOTEL_RESERVATION_INFORMATION.
        """
        return self.__number_of_guest

    @number_of_guest.setter
    def number_of_guest(self, value):
        self.__number_of_guest = value
    @property
    def guest_name(self):
        """
        The guest name. Applicable tags: HOTEL_RESERVATION_INFORMATION.
        """
        return self.__guest_name

    @guest_name.setter
    def guest_name(self, value):
        self.__guest_name = value
    @property
    def pre_payment_fees(self):
        """
        The prepayment amount as a string. Applicable tags: HOTEL_RESERVATION_INFORMATION.
        """
        return self.__pre_payment_fees

    @pre_payment_fees.setter
    def pre_payment_fees(self, value):
        self.__pre_payment_fees = value
    @property
    def accommodation_fee_per_night(self):
        """
        The nightly accommodation fee as a string. Applicable tags: HOTEL_BILL_INFORMATION. Required for HOTEL_BILL_INFORMATION when that tag is submitted.
        """
        return self.__accommodation_fee_per_night

    @accommodation_fee_per_night.setter
    def accommodation_fee_per_night(self, value):
        self.__accommodation_fee_per_night = value
    @property
    def number_of_night(self):
        """
        The number of nights as a string. Applicable tags: HOTEL_BILL_INFORMATION.
        """
        return self.__number_of_night

    @number_of_night.setter
    def number_of_night(self, value):
        self.__number_of_night = value
    @property
    def additional_service_charge(self):
        """
        The additional service charge as a string. Applicable tags: HOTEL_BILL_INFORMATION.
        """
        return self.__additional_service_charge

    @additional_service_charge.setter
    def additional_service_charge(self, value):
        self.__additional_service_charge = value
    @property
    def city_tax(self):
        """
        The city or tourist tax as a string. Applicable tags: HOTEL_BILL_INFORMATION.
        """
        return self.__city_tax

    @city_tax.setter
    def city_tax(self, value):
        self.__city_tax = value
    @property
    def checkout_payment(self):
        """
        The checkout settlement amount as a string. Applicable tags: HOTEL_BILL_INFORMATION.
        """
        return self.__checkout_payment

    @checkout_payment.setter
    def checkout_payment(self, value):
        self.__checkout_payment = value
    @property
    def supplement_proof_file_list(self):
        """
        Files containing evidence that does not fit any of the other 23 tags. This is the only field that accepts multiple files. Submit all files in one call: resubmitting this tag replaces the previous files rather than appending. More than five files rejects the entire request with CAPACITY_EXCEEDED; files are never silently truncated. Applicable tags: UNCATEGORIZED. at least one of supplementProof or supplementProofFileList must be supplied; if both are absent, EVIDENCE_CONTENT_INVALID is returned.
        """
        return self.__supplement_proof_file_list

    @supplement_proof_file_list.setter
    def supplement_proof_file_list(self, value):
        self.__supplement_proof_file_list = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "merchant_order_no") and self.merchant_order_no is not None:
            params['merchantOrderNo'] = self.merchant_order_no
        if hasattr(self, "product_description") and self.product_description is not None:
            params['productDescription'] = self.product_description
        if hasattr(self, "product_unit_price") and self.product_unit_price is not None:
            params['productUnitPrice'] = self.product_unit_price
        if hasattr(self, "quantity") and self.quantity is not None:
            params['quantity'] = self.quantity
        if hasattr(self, "original_order_receipt_file") and self.original_order_receipt_file is not None:
            params['originalOrderReceiptFile'] = self.original_order_receipt_file
        if hasattr(self, "receiver_name") and self.receiver_name is not None:
            params['receiverName'] = self.receiver_name
        if hasattr(self, "receiver_email_address") and self.receiver_email_address is not None:
            params['receiverEmailAddress'] = self.receiver_email_address
        if hasattr(self, "receiver_contact_number") and self.receiver_contact_number is not None:
            params['receiverContactNumber'] = self.receiver_contact_number
        if hasattr(self, "customer_communications") and self.customer_communications is not None:
            params['customerCommunications'] = self.customer_communications
        if hasattr(self, "customer_communications_file") and self.customer_communications_file is not None:
            params['customerCommunicationsFile'] = self.customer_communications_file
        if hasattr(self, "return_and_refund_policy") and self.return_and_refund_policy is not None:
            params['returnAndRefundPolicy'] = self.return_and_refund_policy
        if hasattr(self, "return_and_refund_policy_file") and self.return_and_refund_policy_file is not None:
            params['returnAndRefundPolicyFile'] = self.return_and_refund_policy_file
        if hasattr(self, "cancellation_policy") and self.cancellation_policy is not None:
            params['cancellationPolicy'] = self.cancellation_policy
        if hasattr(self, "cancellation_policy_file") and self.cancellation_policy_file is not None:
            params['cancellationPolicyFile'] = self.cancellation_policy_file
        if hasattr(self, "subscription_policy") and self.subscription_policy is not None:
            params['subscriptionPolicy'] = self.subscription_policy
        if hasattr(self, "subscription_policy_file") and self.subscription_policy_file is not None:
            params['subscriptionPolicyFile'] = self.subscription_policy_file
        if hasattr(self, "payment_policy") and self.payment_policy is not None:
            params['paymentPolicy'] = self.payment_policy
        if hasattr(self, "payment_policy_file") and self.payment_policy_file is not None:
            params['paymentPolicyFile'] = self.payment_policy_file
        if hasattr(self, "certification_records") and self.certification_records is not None:
            params['certificationRecords'] = self.certification_records
        if hasattr(self, "certification_records_file") and self.certification_records_file is not None:
            params['certificationRecordsFile'] = self.certification_records_file
        if hasattr(self, "merchant_comments") and self.merchant_comments is not None:
            params['merchantComments'] = self.merchant_comments
        if hasattr(self, "merchant_comments_file") and self.merchant_comments_file is not None:
            params['merchantCommentsFile'] = self.merchant_comments_file
        if hasattr(self, "marketing_materials_and_listings") and self.marketing_materials_and_listings is not None:
            params['marketingMaterialsAndListings'] = self.marketing_materials_and_listings
        if hasattr(self, "marketing_materials_and_listings_file") and self.marketing_materials_and_listings_file is not None:
            params['marketingMaterialsAndListingsFile'] = self.marketing_materials_and_listings_file
        if hasattr(self, "usage_records_of_recurring_service") and self.usage_records_of_recurring_service is not None:
            params['usageRecordsOfRecurringService'] = self.usage_records_of_recurring_service
        if hasattr(self, "usage_records_of_recurring_service_file") and self.usage_records_of_recurring_service_file is not None:
            params['usageRecordsOfRecurringServiceFile'] = self.usage_records_of_recurring_service_file
        if hasattr(self, "transaction_date") and self.transaction_date is not None:
            params['transactionDate'] = self.transaction_date
        if hasattr(self, "transaction_amount") and self.transaction_amount is not None:
            params['transactionAmount'] = self.transaction_amount
        if hasattr(self, "transaction_currency") and self.transaction_currency is not None:
            params['transactionCurrency'] = self.transaction_currency
        if hasattr(self, "arn") and self.arn is not None:
            params['arn'] = self.arn
        if hasattr(self, "order_description") and self.order_description is not None:
            params['orderDescription'] = self.order_description
        if hasattr(self, "payment_auth_mode") and self.payment_auth_mode is not None:
            params['paymentAuthMode'] = self.payment_auth_mode
        if hasattr(self, "ip_address") and self.ip_address is not None:
            params['ipAddress'] = self.ip_address
        if hasattr(self, "supplement_proof") and self.supplement_proof is not None:
            params['supplementProof'] = self.supplement_proof
        if hasattr(self, "supplement_proof_file") and self.supplement_proof_file is not None:
            params['supplementProofFile'] = self.supplement_proof_file
        if hasattr(self, "refund_method") and self.refund_method is not None:
            params['refundMethod'] = self.refund_method
        if hasattr(self, "refunded_amount") and self.refunded_amount is not None:
            params['refundedAmount'] = self.refunded_amount
        if hasattr(self, "refund_finished_time") and self.refund_finished_time is not None:
            params['refundFinishedTime'] = self.refund_finished_time
        if hasattr(self, "booking_confirmation_terms") and self.booking_confirmation_terms is not None:
            params['bookingConfirmationTerms'] = self.booking_confirmation_terms
        if hasattr(self, "booking_confirmation_terms_file") and self.booking_confirmation_terms_file is not None:
            params['bookingConfirmationTermsFile'] = self.booking_confirmation_terms_file
        if hasattr(self, "offline_signed_agreement") and self.offline_signed_agreement is not None:
            params['offlineSignedAgreement'] = self.offline_signed_agreement
        if hasattr(self, "offline_signed_agreement_file") and self.offline_signed_agreement_file is not None:
            params['offlineSignedAgreementFile'] = self.offline_signed_agreement_file
        if hasattr(self, "installment_billing_agreement") and self.installment_billing_agreement is not None:
            params['installmentBillingAgreement'] = self.installment_billing_agreement
        if hasattr(self, "installment_billing_agreement_file") and self.installment_billing_agreement_file is not None:
            params['installmentBillingAgreementFile'] = self.installment_billing_agreement_file
        if hasattr(self, "tracking_number") and self.tracking_number is not None:
            params['trackingNumber'] = self.tracking_number
        if hasattr(self, "post_code") and self.post_code is not None:
            params['postCode'] = self.post_code
        if hasattr(self, "shipping_address") and self.shipping_address is not None:
            params['shippingAddress'] = self.shipping_address
        if hasattr(self, "tracking_url") and self.tracking_url is not None:
            params['trackingUrl'] = self.tracking_url
        if hasattr(self, "proof_of_shipment_file") and self.proof_of_shipment_file is not None:
            params['proofOfShipmentFile'] = self.proof_of_shipment_file
        if hasattr(self, "logistic_screenshot_file") and self.logistic_screenshot_file is not None:
            params['logisticScreenshotFile'] = self.logistic_screenshot_file
        if hasattr(self, "picture_of_dispatched_item_file") and self.picture_of_dispatched_item_file is not None:
            params['pictureOfDispatchedItemFile'] = self.picture_of_dispatched_item_file
        if hasattr(self, "user_recharge_account_number") and self.user_recharge_account_number is not None:
            params['userRechargeAccountNumber'] = self.user_recharge_account_number
        if hasattr(self, "digital_product_completion_file") and self.digital_product_completion_file is not None:
            params['digitalProductCompletionFile'] = self.digital_product_completion_file
        if hasattr(self, "service_completion_file") and self.service_completion_file is not None:
            params['serviceCompletionFile'] = self.service_completion_file
        if hasattr(self, "order_number") and self.order_number is not None:
            params['orderNumber'] = self.order_number
        if hasattr(self, "booking_time") and self.booking_time is not None:
            params['bookingTime'] = self.booking_time
        if hasattr(self, "air_route") and self.air_route is not None:
            params['airRoute'] = self.air_route
        if hasattr(self, "number_of_passenger") and self.number_of_passenger is not None:
            params['numberOfPassenger'] = self.number_of_passenger
        if hasattr(self, "passenger_name") and self.passenger_name is not None:
            params['passengerName'] = self.passenger_name
        if hasattr(self, "booking_reference_number") and self.booking_reference_number is not None:
            params['bookingReferenceNumber'] = self.booking_reference_number
        if hasattr(self, "ticket_number") and self.ticket_number is not None:
            params['ticketNumber'] = self.ticket_number
        if hasattr(self, "order_status") and self.order_status is not None:
            params['orderStatus'] = self.order_status
        if hasattr(self, "order_amount") and self.order_amount is not None:
            params['orderAmount'] = self.order_amount
        if hasattr(self, "total_payment_amount") and self.total_payment_amount is not None:
            params['totalPaymentAmount'] = self.total_payment_amount
        if hasattr(self, "flight_route") and self.flight_route is not None:
            params['flightRoute'] = self.flight_route
        if hasattr(self, "flight_no") and self.flight_no is not None:
            params['flightNo'] = self.flight_no
        if hasattr(self, "cabin_class") and self.cabin_class is not None:
            params['cabinClass'] = self.cabin_class
        if hasattr(self, "departure_time") and self.departure_time is not None:
            params['departureTime'] = self.departure_time
        if hasattr(self, "arrival_time") and self.arrival_time is not None:
            params['arrivalTime'] = self.arrival_time
        if hasattr(self, "ticket_status") and self.ticket_status is not None:
            params['ticketStatus'] = self.ticket_status
        if hasattr(self, "baggage") and self.baggage is not None:
            params['baggage'] = self.baggage
        if hasattr(self, "reservation_confirmation_number") and self.reservation_confirmation_number is not None:
            params['reservationConfirmationNumber'] = self.reservation_confirmation_number
        if hasattr(self, "hotel_name") and self.hotel_name is not None:
            params['hotelName'] = self.hotel_name
        if hasattr(self, "hotel_address") and self.hotel_address is not None:
            params['hotelAddress'] = self.hotel_address
        if hasattr(self, "check_in_date") and self.check_in_date is not None:
            params['checkInDate'] = self.check_in_date
        if hasattr(self, "check_out_date") and self.check_out_date is not None:
            params['checkOutDate'] = self.check_out_date
        if hasattr(self, "number_of_guest") and self.number_of_guest is not None:
            params['numberOfGuest'] = self.number_of_guest
        if hasattr(self, "guest_name") and self.guest_name is not None:
            params['guestName'] = self.guest_name
        if hasattr(self, "pre_payment_fees") and self.pre_payment_fees is not None:
            params['prePaymentFees'] = self.pre_payment_fees
        if hasattr(self, "accommodation_fee_per_night") and self.accommodation_fee_per_night is not None:
            params['accommodationFeePerNight'] = self.accommodation_fee_per_night
        if hasattr(self, "number_of_night") and self.number_of_night is not None:
            params['numberOfNight'] = self.number_of_night
        if hasattr(self, "additional_service_charge") and self.additional_service_charge is not None:
            params['additionalServiceCharge'] = self.additional_service_charge
        if hasattr(self, "city_tax") and self.city_tax is not None:
            params['cityTax'] = self.city_tax
        if hasattr(self, "checkout_payment") and self.checkout_payment is not None:
            params['checkoutPayment'] = self.checkout_payment
        if hasattr(self, "supplement_proof_file_list") and self.supplement_proof_file_list is not None:
            params['supplementProofFileList'] = self.supplement_proof_file_list
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'merchantOrderNo' in response_body:
            self.__merchant_order_no = response_body['merchantOrderNo']
        if 'productDescription' in response_body:
            self.__product_description = response_body['productDescription']
        if 'productUnitPrice' in response_body:
            self.__product_unit_price = response_body['productUnitPrice']
        if 'quantity' in response_body:
            self.__quantity = response_body['quantity']
        if 'originalOrderReceiptFile' in response_body:
            self.__original_order_receipt_file = EvidenceFile()
            self.__original_order_receipt_file.parse_rsp_body(response_body['originalOrderReceiptFile'])
        if 'receiverName' in response_body:
            self.__receiver_name = response_body['receiverName']
        if 'receiverEmailAddress' in response_body:
            self.__receiver_email_address = response_body['receiverEmailAddress']
        if 'receiverContactNumber' in response_body:
            self.__receiver_contact_number = response_body['receiverContactNumber']
        if 'customerCommunications' in response_body:
            self.__customer_communications = response_body['customerCommunications']
        if 'customerCommunicationsFile' in response_body:
            self.__customer_communications_file = EvidenceFile()
            self.__customer_communications_file.parse_rsp_body(response_body['customerCommunicationsFile'])
        if 'returnAndRefundPolicy' in response_body:
            self.__return_and_refund_policy = response_body['returnAndRefundPolicy']
        if 'returnAndRefundPolicyFile' in response_body:
            self.__return_and_refund_policy_file = EvidenceFile()
            self.__return_and_refund_policy_file.parse_rsp_body(response_body['returnAndRefundPolicyFile'])
        if 'cancellationPolicy' in response_body:
            self.__cancellation_policy = response_body['cancellationPolicy']
        if 'cancellationPolicyFile' in response_body:
            self.__cancellation_policy_file = EvidenceFile()
            self.__cancellation_policy_file.parse_rsp_body(response_body['cancellationPolicyFile'])
        if 'subscriptionPolicy' in response_body:
            self.__subscription_policy = response_body['subscriptionPolicy']
        if 'subscriptionPolicyFile' in response_body:
            self.__subscription_policy_file = EvidenceFile()
            self.__subscription_policy_file.parse_rsp_body(response_body['subscriptionPolicyFile'])
        if 'paymentPolicy' in response_body:
            self.__payment_policy = response_body['paymentPolicy']
        if 'paymentPolicyFile' in response_body:
            self.__payment_policy_file = EvidenceFile()
            self.__payment_policy_file.parse_rsp_body(response_body['paymentPolicyFile'])
        if 'certificationRecords' in response_body:
            self.__certification_records = response_body['certificationRecords']
        if 'certificationRecordsFile' in response_body:
            self.__certification_records_file = EvidenceFile()
            self.__certification_records_file.parse_rsp_body(response_body['certificationRecordsFile'])
        if 'merchantComments' in response_body:
            self.__merchant_comments = response_body['merchantComments']
        if 'merchantCommentsFile' in response_body:
            self.__merchant_comments_file = EvidenceFile()
            self.__merchant_comments_file.parse_rsp_body(response_body['merchantCommentsFile'])
        if 'marketingMaterialsAndListings' in response_body:
            self.__marketing_materials_and_listings = response_body['marketingMaterialsAndListings']
        if 'marketingMaterialsAndListingsFile' in response_body:
            self.__marketing_materials_and_listings_file = EvidenceFile()
            self.__marketing_materials_and_listings_file.parse_rsp_body(response_body['marketingMaterialsAndListingsFile'])
        if 'usageRecordsOfRecurringService' in response_body:
            self.__usage_records_of_recurring_service = response_body['usageRecordsOfRecurringService']
        if 'usageRecordsOfRecurringServiceFile' in response_body:
            self.__usage_records_of_recurring_service_file = EvidenceFile()
            self.__usage_records_of_recurring_service_file.parse_rsp_body(response_body['usageRecordsOfRecurringServiceFile'])
        if 'transactionDate' in response_body:
            self.__transaction_date = response_body['transactionDate']
        if 'transactionAmount' in response_body:
            self.__transaction_amount = response_body['transactionAmount']
        if 'transactionCurrency' in response_body:
            self.__transaction_currency = response_body['transactionCurrency']
        if 'arn' in response_body:
            self.__arn = response_body['arn']
        if 'orderDescription' in response_body:
            self.__order_description = response_body['orderDescription']
        if 'paymentAuthMode' in response_body:
            self.__payment_auth_mode = response_body['paymentAuthMode']
        if 'ipAddress' in response_body:
            self.__ip_address = response_body['ipAddress']
        if 'supplementProof' in response_body:
            self.__supplement_proof = response_body['supplementProof']
        if 'supplementProofFile' in response_body:
            self.__supplement_proof_file = EvidenceFile()
            self.__supplement_proof_file.parse_rsp_body(response_body['supplementProofFile'])
        if 'refundMethod' in response_body:
            self.__refund_method = response_body['refundMethod']
        if 'refundedAmount' in response_body:
            self.__refunded_amount = response_body['refundedAmount']
        if 'refundFinishedTime' in response_body:
            self.__refund_finished_time = response_body['refundFinishedTime']
        if 'bookingConfirmationTerms' in response_body:
            self.__booking_confirmation_terms = response_body['bookingConfirmationTerms']
        if 'bookingConfirmationTermsFile' in response_body:
            self.__booking_confirmation_terms_file = EvidenceFile()
            self.__booking_confirmation_terms_file.parse_rsp_body(response_body['bookingConfirmationTermsFile'])
        if 'offlineSignedAgreement' in response_body:
            self.__offline_signed_agreement = response_body['offlineSignedAgreement']
        if 'offlineSignedAgreementFile' in response_body:
            self.__offline_signed_agreement_file = EvidenceFile()
            self.__offline_signed_agreement_file.parse_rsp_body(response_body['offlineSignedAgreementFile'])
        if 'installmentBillingAgreement' in response_body:
            self.__installment_billing_agreement = response_body['installmentBillingAgreement']
        if 'installmentBillingAgreementFile' in response_body:
            self.__installment_billing_agreement_file = EvidenceFile()
            self.__installment_billing_agreement_file.parse_rsp_body(response_body['installmentBillingAgreementFile'])
        if 'trackingNumber' in response_body:
            self.__tracking_number = response_body['trackingNumber']
        if 'postCode' in response_body:
            self.__post_code = response_body['postCode']
        if 'shippingAddress' in response_body:
            self.__shipping_address = response_body['shippingAddress']
        if 'trackingUrl' in response_body:
            self.__tracking_url = response_body['trackingUrl']
        if 'proofOfShipmentFile' in response_body:
            self.__proof_of_shipment_file = EvidenceFile()
            self.__proof_of_shipment_file.parse_rsp_body(response_body['proofOfShipmentFile'])
        if 'logisticScreenshotFile' in response_body:
            self.__logistic_screenshot_file = EvidenceFile()
            self.__logistic_screenshot_file.parse_rsp_body(response_body['logisticScreenshotFile'])
        if 'pictureOfDispatchedItemFile' in response_body:
            self.__picture_of_dispatched_item_file = EvidenceFile()
            self.__picture_of_dispatched_item_file.parse_rsp_body(response_body['pictureOfDispatchedItemFile'])
        if 'userRechargeAccountNumber' in response_body:
            self.__user_recharge_account_number = response_body['userRechargeAccountNumber']
        if 'digitalProductCompletionFile' in response_body:
            self.__digital_product_completion_file = EvidenceFile()
            self.__digital_product_completion_file.parse_rsp_body(response_body['digitalProductCompletionFile'])
        if 'serviceCompletionFile' in response_body:
            self.__service_completion_file = EvidenceFile()
            self.__service_completion_file.parse_rsp_body(response_body['serviceCompletionFile'])
        if 'orderNumber' in response_body:
            self.__order_number = response_body['orderNumber']
        if 'bookingTime' in response_body:
            self.__booking_time = response_body['bookingTime']
        if 'airRoute' in response_body:
            self.__air_route = response_body['airRoute']
        if 'numberOfPassenger' in response_body:
            self.__number_of_passenger = response_body['numberOfPassenger']
        if 'passengerName' in response_body:
            self.__passenger_name = response_body['passengerName']
        if 'bookingReferenceNumber' in response_body:
            self.__booking_reference_number = response_body['bookingReferenceNumber']
        if 'ticketNumber' in response_body:
            self.__ticket_number = response_body['ticketNumber']
        if 'orderStatus' in response_body:
            self.__order_status = response_body['orderStatus']
        if 'orderAmount' in response_body:
            self.__order_amount = response_body['orderAmount']
        if 'totalPaymentAmount' in response_body:
            self.__total_payment_amount = response_body['totalPaymentAmount']
        if 'flightRoute' in response_body:
            self.__flight_route = response_body['flightRoute']
        if 'flightNo' in response_body:
            self.__flight_no = response_body['flightNo']
        if 'cabinClass' in response_body:
            self.__cabin_class = response_body['cabinClass']
        if 'departureTime' in response_body:
            self.__departure_time = response_body['departureTime']
        if 'arrivalTime' in response_body:
            self.__arrival_time = response_body['arrivalTime']
        if 'ticketStatus' in response_body:
            self.__ticket_status = response_body['ticketStatus']
        if 'baggage' in response_body:
            self.__baggage = response_body['baggage']
        if 'reservationConfirmationNumber' in response_body:
            self.__reservation_confirmation_number = response_body['reservationConfirmationNumber']
        if 'hotelName' in response_body:
            self.__hotel_name = response_body['hotelName']
        if 'hotelAddress' in response_body:
            self.__hotel_address = response_body['hotelAddress']
        if 'checkInDate' in response_body:
            self.__check_in_date = response_body['checkInDate']
        if 'checkOutDate' in response_body:
            self.__check_out_date = response_body['checkOutDate']
        if 'numberOfGuest' in response_body:
            self.__number_of_guest = response_body['numberOfGuest']
        if 'guestName' in response_body:
            self.__guest_name = response_body['guestName']
        if 'prePaymentFees' in response_body:
            self.__pre_payment_fees = response_body['prePaymentFees']
        if 'accommodationFeePerNight' in response_body:
            self.__accommodation_fee_per_night = response_body['accommodationFeePerNight']
        if 'numberOfNight' in response_body:
            self.__number_of_night = response_body['numberOfNight']
        if 'additionalServiceCharge' in response_body:
            self.__additional_service_charge = response_body['additionalServiceCharge']
        if 'cityTax' in response_body:
            self.__city_tax = response_body['cityTax']
        if 'checkoutPayment' in response_body:
            self.__checkout_payment = response_body['checkoutPayment']
        if 'supplementProofFileList' in response_body:
            self.__supplement_proof_file_list = []
            for item in response_body['supplementProofFileList']:
                obj = EvidenceFile()
                obj.parse_rsp_body(item)
                self.__supplement_proof_file_list.append(obj)

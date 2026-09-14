from com.alipay.ams.api.model import DisputeJudgedResult
from com.alipay.ams.api.model.acquirer_info import AcquirerInfo
from com.alipay.ams.api.model.dispute_accept_reason_type import DisputeAcceptReasonType
from com.alipay.ams.api.model.dispute_notification_type import DisputeNotificationType
from com.alipay.ams.api.model.issuer_comments import IssuerComments
from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayDisputeNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayDisputeNotify, self).__init__()
        self.__payment_request_id = None
        self.__dispute_id = None
        self.__payment_id = None
        self.__dispute_time = None
        self.__dispute_amount = None
        self.__dispute_notification_type = None  # type: DisputeNotificationType
        self.__dispute_reason_msg = None
        self.__dispute_judged_time = None
        self.__dispute_judged_amount = None
        self.__dispute_judged_result = None  # type: DisputeJudgedResult
        self.__defense_due_time = None
        self.__dispute_reason_code = None
        self.__dispute_source = None
        self.__arn = None
        self.__dispute_accept_reason = None  # type: DisputeAcceptReasonType
        self.__dispute_accept_time = None
        self.__dispute_type = None
        self.__defendable = None
        self.__capture_id = None
        self.__auto_defend_reason = None
        self.__acquirer_info = None  # type: AcquirerInfo
        self.__issuer_comments = None  # type: IssuerComments
        self.__parse_notify_body(notify_body)

    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @property
    def dispute_id(self):
        return self.__dispute_id

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def dispute_time(self):
        return self.__dispute_time

    @property
    def dispute_amount(self):
        return self.__dispute_amount

    @property
    def dispute_notification_type(self):
        return self.__dispute_notification_type

    @property
    def dispute_reason_msg(self):
        return self.__dispute_reason_msg

    @property
    def dispute_judged_time(self):
        return self.__dispute_judged_time

    @property
    def dispute_judged_amount(self):
        return self.__dispute_judged_amount

    @property
    def dispute_judged_result(self):
        return self.__dispute_judged_result

    @property
    def defense_due_time(self):
        return self.__defense_due_time

    @property
    def dispute_reason_code(self):
        return self.__dispute_reason_code

    @property
    def dispute_source(self):
        return self.__dispute_source

    @property
    def arn(self):
        return self.__arn

    @property
    def dispute_accept_reason(self):
        return self.__dispute_accept_reason

    @property
    def dispute_accept_time(self):
        return self.__dispute_accept_time

    @property
    def dispute_type(self):
        return self.__dispute_type

    @property
    def defendable(self):
        return self.__defendable

    @property
    def capture_id(self):
        return self.__capture_id

    @property
    def auto_defend_reason(self):
        return self.__auto_defend_reason

    @property
    def acquirer_info(self):
        return self.__acquirer_info

    @property
    def issuer_comments(self):
        return self.__issuer_comments

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayDisputeNotify, self).parse_notify_body(notify_body)

        def get_value(camel_case_key, snake_case_key=None):
            if camel_case_key in notify:
                return notify[camel_case_key]
            if snake_case_key is not None:
                return notify.get(snake_case_key)
            return None

        self.__payment_request_id = get_value("paymentRequestId", "payment_request_id")
        self.__dispute_id = get_value("disputeId", "dispute_id")
        self.__payment_id = get_value("paymentId", "payment_id")
        self.__dispute_time = get_value("disputeTime", "dispute_time")
        self.__dispute_amount = get_value("disputeAmount", "dispute_amount")
        self.__dispute_notification_type = get_value(
            "disputeNotificationType", "dispute_notification_type"
        )
        self.__dispute_reason_msg = get_value("disputeReasonMsg", "dispute_reason_msg")
        self.__dispute_judged_time = get_value("disputeJudgedTime", "dispute_judged_time")
        self.__dispute_judged_amount = get_value(
            "disputeJudgedAmount", "dispute_judged_amount"
        )
        self.__dispute_judged_result = get_value(
            "disputeJudgedResult", "dispute_judged_result"
        )
        self.__defense_due_time = get_value("defenseDueTime", "defense_due_time")
        self.__dispute_reason_code = get_value("disputeReasonCode", "dispute_reason_code")
        self.__dispute_source = get_value("disputeSource", "dispute_source")
        self.__arn = get_value("arn")
        self.__dispute_accept_reason = get_value(
            "disputeAcceptReason", "dispute_accept_reason"
        )
        self.__dispute_accept_time = get_value("disputeAcceptTime", "dispute_accept_time")
        self.__dispute_type = get_value("disputeType", "dispute_type")
        self.__defendable = get_value("defendable")
        self.__capture_id = get_value("captureId", "capture_id")
        self.__auto_defend_reason = get_value("autoDefendReason", "auto_defend_reason")
        self.__acquirer_info = get_value("acquirerInfo", "acquirer_info")

        issuer_comments_body = get_value("issuerComments", "issuer_comments")
        if isinstance(issuer_comments_body, dict):
            self.__issuer_comments = IssuerComments()
            self.__issuer_comments.cardholder_comments = issuer_comments_body.get(
                "cardholderComments", issuer_comments_body.get("cardholder_comments")
            )
            self.__issuer_comments.reason_of_invalid_authorization = issuer_comments_body.get(
                "reasonOfInvalidAuthorization",
                issuer_comments_body.get("reason_of_invalid_authorization"),
            )
            self.__issuer_comments.explanation_of_credit_presented = issuer_comments_body.get(
                "explanationOfCreditPresented",
                issuer_comments_body.get("explanation_of_credit_presented"),
            )
            self.__issuer_comments.judge_reason = issuer_comments_body.get(
                "judgeReason", issuer_comments_body.get("judge_reason")
            )

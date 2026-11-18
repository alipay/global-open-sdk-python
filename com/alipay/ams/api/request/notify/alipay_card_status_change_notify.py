from com.alipay.ams.api.request.notify.alipay_notify import AlipayNotify


class AlipayCardStatusChangeNotify(AlipayNotify):

    def __init__(self, notify_body):
        super(AlipayCardStatusChangeNotify, self).__init__()
        self.__request_id = None
        self.__asset_id = None
        self.__operate_type = None
        self.__status = None
        self.__card_status = None
        self.__created_time = None
        self.__updated_time = None
        self.__card_brand = None
        self.__card_type = None
        self.__parse_notify_body(notify_body)

    @property
    def request_id(self):
        return self.__request_id

    @property
    def asset_id(self):
        return self.__asset_id

    @property
    def operate_type(self):
        return self.__operate_type

    @property
    def status(self):
        return self.__status

    @property
    def card_status(self):
        return self.__card_status

    @property
    def created_time(self):
        return self.__created_time

    @property
    def updated_time(self):
        return self.__updated_time

    @property
    def card_brand(self):
        return self.__card_brand

    @property
    def card_type(self):
        return self.__card_type

    def __parse_notify_body(self, notify_body):
        notify = super(AlipayCardStatusChangeNotify, self).parse_notify_body(notify_body)

        if "requestId" in notify:
            self.__request_id = notify["requestId"]
        if "assetId" in notify:
            self.__asset_id = notify["assetId"]
        if "operateType" in notify:
            self.__operate_type = notify["operateType"]
        if "status" in notify:
            self.__status = notify["status"]
        if "cardStatus" in notify:
            self.__card_status = notify["cardStatus"]
        if "createdTime" in notify:
            self.__created_time = notify["createdTime"]
        if "updatedTime" in notify:
            self.__updated_time = notify["updatedTime"]
        if "cardBrand" in notify:
            self.__card_brand = notify["cardBrand"]
        if "cardType" in notify:
            self.__card_type = notify["cardType"]

import json

from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayUploadInvoiceShippingFileRequest(AlipayRequest):

    def __init__(self):
        super(AlipayUploadInvoiceShippingFileRequest, self).__init__("/ams/api/v1/payments/uploadInvoiceShippingFile")
        self.__payment_request_id = None
        self.__file_id = None
        self.__upload_file = None
        self.__file_type = None
        self.__file_name = None


    @property
    def payment_request_id(self):
        return self.__payment_request_id

    @payment_request_id.setter
    def payment_request_id(self, value):
        self.__payment_request_id = value

    @property
    def file_id(self):
        return self.__file_id

    @file_id.setter
    def file_id(self, value):
        self.__file_id = value

    @property
    def upload_file(self):
        return self.__upload_file

    @upload_file.setter
    def upload_file(self, value):
        self.__upload_file = value

    @property
    def file_type(self):
        return self.__file_type

    @file_type.setter
    def file_type(self, value):
        self.__file_type = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if hasattr(self, "payment_request_id") and self.payment_request_id:
            params['paymentRequestId'] = self.payment_request_id
        if hasattr(self, "file_id") and self.file_id:
            params['fileId'] = self.file_id
        if hasattr(self, "upload_file") and self.upload_file:
            params['uploadFile'] = self.upload_file
        if hasattr(self, "file_type") and self.file_type:
            params['fileType'] = self.file_type
        if hasattr(self, "file_name") and self.file_name:
            params['fileName'] = self.file_name
        return params
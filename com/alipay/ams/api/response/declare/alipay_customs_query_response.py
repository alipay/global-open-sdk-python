import json

from com.alipay.ams.api.model.declaration_record import DeclarationRecord
from com.alipay.ams.api.response.alipay_response import AlipayResponse


class AlipayCustomsQueryResponse(AlipayResponse):

    def __init__(self, rsp_body):
        super(AlipayCustomsQueryResponse, self).__init__()
        self.__declaration_requests_not_found = None  # type: list[str]
        self.__declaration_records = None  # type: list[DeclarationRecord]
        self.parse_rsp_body(rsp_body)

    @property
    def declaration_requests_not_found(self):
        return self.__declaration_requests_not_found

    @property
    def declaration_records(self):
        return self.__declaration_records

    def parse_rsp_body(self, rsp_body):
        rsp_dict = super(AlipayCustomsQueryResponse, self).parse_rsp_body(rsp_body)
        if "declarationRequestsNotFound" in rsp_dict:
            self.__declaration_requests_not_found = rsp_dict[
                "declarationRequestsNotFound"
            ]
        if "declarationRecords" in rsp_dict:
            self.__declaration_records = []
            for declaration_record_dict in rsp_dict["declarationRecords"]:
                declaration_record = DeclarationRecord()
                declaration_record.parse_rsp_body(declaration_record_dict)
                self.__declaration_records.append(declaration_record)

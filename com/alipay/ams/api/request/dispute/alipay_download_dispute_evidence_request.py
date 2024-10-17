import json

from com.alipay.ams.api.model.antom_path_constants import AntomPathConstants
from com.alipay.ams.api.model.dispute_evidence_type import DisputeEvidenceType
from com.alipay.ams.api.request.alipay_request import AlipayRequest


class AlipayDownloadDisputeEvidenceRequest(AlipayRequest):
    def __init__(self):
        super(AlipayDownloadDisputeEvidenceRequest, self).__init__(AntomPathConstants.DOWNLOAD_DISPUTE_EVIDENCE_PATH)
        self.__dispute_id = None
        self.__dispute_evidence_type = None  # type:DisputeEvidenceType

    @property
    def dispute_id(self):
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self.__dispute_id = value

    @property
    def dispute_evidence_type(self):
        return self.__dispute_evidence_type

    @dispute_evidence_type.setter
    def dispute_evidence_type(self, value):
        self.__dispute_evidence_type = value

    def to_ams_json(self):
        json_str = json.dumps(obj=self.__to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3)
        return json_str

    def __to_ams_dict(self):
        params = dict()
        if self.__dispute_id is not None:
            params['disputeId'] = self.__dispute_id
        if self.__dispute_evidence_type is not None:
            params['disputeEvidenceType'] = self.__dispute_evidence_type
        return params

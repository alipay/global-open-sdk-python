import json




class DisputeEvidenceResult:
    def __init__(self):
        
        self.__evidence_tag = None  # type: str
        self.__success = None  # type: str
        self.__result_code = None  # type: str
        self.__failed_field_path = None  # type: str
        

    @property
    def evidence_tag(self):
        """
        The evidence tag associated with this result.
        """
        return self.__evidence_tag

    @evidence_tag.setter
    def evidence_tag(self, value):
        self.__evidence_tag = value
    @property
    def success(self):
        """
        Whether the evidence was saved successfully, expressed as \&quot;true\&quot; or \&quot;false\&quot;.
        """
        return self.__success

    @success.setter
    def success(self, value):
        self.__success = value
    @property
    def result_code(self):
        """
        The failure code, returned when success is \&quot;false\&quot;.
        """
        return self.__result_code

    @result_code.setter
    def result_code(self, value):
        self.__result_code = value
    @property
    def failed_field_path(self):
        """
        The path of the first missing or invalid field, returned for field-level validation failures.
        """
        return self.__failed_field_path

    @failed_field_path.setter
    def failed_field_path(self, value):
        self.__failed_field_path = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "evidence_tag") and self.evidence_tag is not None:
            params['evidenceTag'] = self.evidence_tag
        if hasattr(self, "success") and self.success is not None:
            params['success'] = self.success
        if hasattr(self, "result_code") and self.result_code is not None:
            params['resultCode'] = self.result_code
        if hasattr(self, "failed_field_path") and self.failed_field_path is not None:
            params['failedFieldPath'] = self.failed_field_path
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'evidenceTag' in response_body:
            self.__evidence_tag = response_body['evidenceTag']
        if 'success' in response_body:
            self.__success = response_body['success']
        if 'resultCode' in response_body:
            self.__result_code = response_body['resultCode']
        if 'failedFieldPath' in response_body:
            self.__failed_field_path = response_body['failedFieldPath']

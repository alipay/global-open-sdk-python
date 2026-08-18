import json
from com.alipay.ams.api.model.meter_event_batch import MeterEventBatch



from com.alipay.ams.api.request.alipay_request import AlipayRequest

class AlipayMeterUploadEventRequest(AlipayRequest):
    def __init__(self):
        super(AlipayMeterUploadEventRequest, self).__init__("/ams/api/v1/meter/uploadEvent") 

        self.__meters = None  # type: [MeterEventBatch]
        

    @property
    def meters(self):
        """
        The meters. Maximum length: 500 characters.
        """
        return self.__meters

    @meters.setter
    def meters(self, value):
        self.__meters = value


    def to_ams_json(self): 
        json_str = json.dumps(obj=self.to_ams_dict(), default=lambda o: o.to_ams_dict(), indent=3) 
        return json_str


    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "meters") and self.meters is not None:
            params['meters'] = self.meters
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'meters' in response_body:
            self.__meters = []
            for item in response_body['meters']:
                obj = MeterEventBatch()
                obj.parse_rsp_body(item)
                self.__meters.append(obj)

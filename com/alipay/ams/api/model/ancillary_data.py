import json
from com.alipay.ams.api.model.service import Service




class AncillaryData:
    def __init__(self):
        
        self.__services = None  # type: [Service]
        self.__connected_ticket_number = None  # type: str
        

    @property
    def services(self):
        """
        List of services for ancillary data
        """
        return self.__services

    @services.setter
    def services(self, value):
        self.__services = value
    @property
    def connected_ticket_number(self):
        """
        Connected ticket number
        """
        return self.__connected_ticket_number

    @connected_ticket_number.setter
    def connected_ticket_number(self, value):
        self.__connected_ticket_number = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "services") and self.services is not None:
            params['services'] = self.services
        if hasattr(self, "connected_ticket_number") and self.connected_ticket_number is not None:
            params['connectedTicketNumber'] = self.connected_ticket_number
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'services' in response_body:
            self.__services = []
            for item in response_body['services']:
                obj = Service()
                obj.parse_rsp_body(item)
                self.__services.append(obj)
        if 'connectedTicketNumber' in response_body:
            self.__connected_ticket_number = response_body['connectedTicketNumber']

import json
from com.alipay.ams.api.model.transit_type import TransitType
from com.alipay.ams.api.model.leg import Leg
from com.alipay.ams.api.model.passenger import Passenger
from com.alipay.ams.api.model.ancillary_data import AncillaryData




class Transit:
    def __init__(self):
        
        self.__transit_type = None  # type: TransitType
        self.__legs = None  # type: [Leg]
        self.__passengers = None  # type: [Passenger]
        self.__agent_code = None  # type: str
        self.__agent_name = None  # type: str
        self.__ticket_number = None  # type: str
        self.__ticket_issuer_code = None  # type: str
        self.__restricted_ticket_indicator = None  # type: str
        self.__ancillary_data = None  # type: AncillaryData
        

    @property
    def transit_type(self):
        """Gets the transit_type of this Transit.
        
        """
        return self.__transit_type

    @transit_type.setter
    def transit_type(self, value):
        self.__transit_type = value
    @property
    def legs(self):
        """
        Information about sections of the trip, including departure time, arrival time, departure address, arrival address, transportation company name, carrier code and service type.  More information:  Maximum size: 10 elements
        """
        return self.__legs

    @legs.setter
    def legs(self, value):
        self.__legs = value
    @property
    def passengers(self):
        """
        Information about the passenger of the trip, including the passenger names, passenger email and phone number.  More information:  Maximum size: 100 elements
        """
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        self.__passengers = value
    @property
    def agent_code(self):
        """
        Added field for agent code
        """
        return self.__agent_code

    @agent_code.setter
    def agent_code(self, value):
        self.__agent_code = value
    @property
    def agent_name(self):
        """
        Added field for agent name
        """
        return self.__agent_name

    @agent_name.setter
    def agent_name(self, value):
        self.__agent_name = value
    @property
    def ticket_number(self):
        """
        Added field for ticket number
        """
        return self.__ticket_number

    @ticket_number.setter
    def ticket_number(self, value):
        self.__ticket_number = value
    @property
    def ticket_issuer_code(self):
        """
        Added field for ticket issuer code
        """
        return self.__ticket_issuer_code

    @ticket_issuer_code.setter
    def ticket_issuer_code(self, value):
        self.__ticket_issuer_code = value
    @property
    def restricted_ticket_indicator(self):
        """
        Added field for restricted ticket indicator
        """
        return self.__restricted_ticket_indicator

    @restricted_ticket_indicator.setter
    def restricted_ticket_indicator(self, value):
        self.__restricted_ticket_indicator = value
    @property
    def ancillary_data(self):
        """Gets the ancillary_data of this Transit.
        
        """
        return self.__ancillary_data

    @ancillary_data.setter
    def ancillary_data(self, value):
        self.__ancillary_data = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "transit_type") and self.transit_type is not None:
            params['transitType'] = self.transit_type
        if hasattr(self, "legs") and self.legs is not None:
            params['legs'] = self.legs
        if hasattr(self, "passengers") and self.passengers is not None:
            params['passengers'] = self.passengers
        if hasattr(self, "agent_code") and self.agent_code is not None:
            params['agentCode'] = self.agent_code
        if hasattr(self, "agent_name") and self.agent_name is not None:
            params['agentName'] = self.agent_name
        if hasattr(self, "ticket_number") and self.ticket_number is not None:
            params['ticketNumber'] = self.ticket_number
        if hasattr(self, "ticket_issuer_code") and self.ticket_issuer_code is not None:
            params['ticketIssuerCode'] = self.ticket_issuer_code
        if hasattr(self, "restricted_ticket_indicator") and self.restricted_ticket_indicator is not None:
            params['restrictedTicketIndicator'] = self.restricted_ticket_indicator
        if hasattr(self, "ancillary_data") and self.ancillary_data is not None:
            params['ancillaryData'] = self.ancillary_data
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'transitType' in response_body:
            transit_type_temp = TransitType.value_of(response_body['transitType'])
            self.__transit_type = transit_type_temp
        if 'legs' in response_body:
            self.__legs = []
            for item in response_body['legs']:
                obj = Leg()
                obj.parse_rsp_body(item)
                self.__legs.append(obj)
        if 'passengers' in response_body:
            self.__passengers = []
            for item in response_body['passengers']:
                obj = Passenger()
                obj.parse_rsp_body(item)
                self.__passengers.append(obj)
        if 'agentCode' in response_body:
            self.__agent_code = response_body['agentCode']
        if 'agentName' in response_body:
            self.__agent_name = response_body['agentName']
        if 'ticketNumber' in response_body:
            self.__ticket_number = response_body['ticketNumber']
        if 'ticketIssuerCode' in response_body:
            self.__ticket_issuer_code = response_body['ticketIssuerCode']
        if 'restrictedTicketIndicator' in response_body:
            self.__restricted_ticket_indicator = response_body['restrictedTicketIndicator']
        if 'ancillaryData' in response_body:
            self.__ancillary_data = AncillaryData()
            self.__ancillary_data.parse_rsp_body(response_body['ancillaryData'])

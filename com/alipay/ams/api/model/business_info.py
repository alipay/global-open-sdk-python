import json
from com.alipay.ams.api.model.web_site import WebSite




class BusinessInfo:
    def __init__(self):
        
        self.__mcc = None  # type: str
        self.__websites = None  # type: [WebSite]
        self.__english_name = None  # type: str
        self.__doing_business_as = None  # type: str
        self.__main_sales_country = None  # type: str
        self.__app_name = None  # type: str
        self.__service_description = None  # type: str
        

    @property
    def mcc(self):
        """
        mcc String  The merchant category code (MCC). See MCC list to check valid values.    More information:  Maximum length: 32 characters
        """
        return self.__mcc

    @mcc.setter
    def mcc(self, value):
        self.__mcc = value
    @property
    def websites(self):
        """
        The list of merchant websites. The information is used to verify the company&#39;s legal status and ensure the company complies with regulatory requirements.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is BR.   More information:  Maximum size: 10 elements 
        """
        return self.__websites

    @websites.setter
    def websites(self, value):
        self.__websites = value
    @property
    def english_name(self):
        """
        The English name of the company.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is JP.    More information:  Maximum length: 256 characters 
        """
        return self.__english_name

    @english_name.setter
    def english_name(self, value):
        self.__english_name = value
    @property
    def doing_business_as(self):
        """
        The customer-facing business name. Consider user interface limitations when choosing this name.    More information:  Maximum length: 256 characters
        """
        return self.__doing_business_as

    @doing_business_as.setter
    def doing_business_as(self, value):
        self.__doing_business_as = value
    @property
    def main_sales_country(self):
        """
        The country where your primary sales activities take place. The value of this parameter is a 2-letter country or region code based on the ISO 3166 Country Codes standard.  Specify this parameter when the value of merchantInfo.company.registeredAddress.region is US.    More information:  Maximum length: 2 characters
        """
        return self.__main_sales_country

    @main_sales_country.setter
    def main_sales_country(self, value):
        self.__main_sales_country = value
    @property
    def app_name(self):
        """
        The App name. Specify this parameter when the value of paymentMethodType is TRUEMONEY.  More information:  Maximum length: 256 characters
        """
        return self.__app_name

    @app_name.setter
    def app_name(self, value):
        self.__app_name = value
    @property
    def service_description(self):
        """
        A clear and detailed description of the product or service. Specify this parameter when the value of paymentMethodType is TRUEMONEY.  More information:  Maximum length: 256 characters
        """
        return self.__service_description

    @service_description.setter
    def service_description(self, value):
        self.__service_description = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "mcc") and self.mcc is not None:
            params['mcc'] = self.mcc
        if hasattr(self, "websites") and self.websites is not None:
            params['websites'] = self.websites
        if hasattr(self, "english_name") and self.english_name is not None:
            params['englishName'] = self.english_name
        if hasattr(self, "doing_business_as") and self.doing_business_as is not None:
            params['doingBusinessAs'] = self.doing_business_as
        if hasattr(self, "main_sales_country") and self.main_sales_country is not None:
            params['mainSalesCountry'] = self.main_sales_country
        if hasattr(self, "app_name") and self.app_name is not None:
            params['appName'] = self.app_name
        if hasattr(self, "service_description") and self.service_description is not None:
            params['serviceDescription'] = self.service_description
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'mcc' in response_body:
            self.__mcc = response_body['mcc']
        if 'websites' in response_body:
            self.__websites = []
            for item in response_body['websites']:
                obj = WebSite()
                obj.parse_rsp_body(item)
                self.__websites.append(obj)
        if 'englishName' in response_body:
            self.__english_name = response_body['englishName']
        if 'doingBusinessAs' in response_body:
            self.__doing_business_as = response_body['doingBusinessAs']
        if 'mainSalesCountry' in response_body:
            self.__main_sales_country = response_body['mainSalesCountry']
        if 'appName' in response_body:
            self.__app_name = response_body['appName']
        if 'serviceDescription' in response_body:
            self.__service_description = response_body['serviceDescription']

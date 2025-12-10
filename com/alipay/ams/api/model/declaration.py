import json
from com.alipay.ams.api.model.declaration_biz_scene_type import DeclarationBizSceneType




class Declaration:
    def __init__(self):
        
        self.__declaration_biz_scene = None  # type: DeclarationBizSceneType
        self.__declaration_beneficiary_id = None  # type: str
        

    @property
    def declaration_biz_scene(self):
        """Gets the declaration_biz_scene of this Declaration.
        
        """
        return self.__declaration_biz_scene

    @declaration_biz_scene.setter
    def declaration_biz_scene(self, value):
        self.__declaration_biz_scene = value
    @property
    def declaration_beneficiary_id(self):
        """
        用于唯一标识用于申报额度累计的三方收款人Id。非OTA结汇场景不传，OTA场景必传，且与declarationBizScene需同时存在。
        """
        return self.__declaration_beneficiary_id

    @declaration_beneficiary_id.setter
    def declaration_beneficiary_id(self, value):
        self.__declaration_beneficiary_id = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "declaration_biz_scene") and self.declaration_biz_scene is not None:
            params['declarationBizScene'] = self.declaration_biz_scene
        if hasattr(self, "declaration_beneficiary_id") and self.declaration_beneficiary_id is not None:
            params['declarationBeneficiaryId'] = self.declaration_beneficiary_id
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'declarationBizScene' in response_body:
            declaration_biz_scene_temp = DeclarationBizSceneType.value_of(response_body['declarationBizScene'])
            self.__declaration_biz_scene = declaration_biz_scene_temp
        if 'declarationBeneficiaryId' in response_body:
            self.__declaration_beneficiary_id = response_body['declarationBeneficiaryId']

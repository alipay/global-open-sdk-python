import json




class InvoiceNote:
    def __init__(self):
        
        self.__note_id = None  # type: str
        self.__note = None  # type: str
        self.__action = None  # type: str
        self.__note_time = None  # type: str
        

    @property
    def note_id(self):
        """
        The note id. Maximum length: 64 characters.
        """
        return self.__note_id

    @note_id.setter
    def note_id(self, value):
        self.__note_id = value
    @property
    def note(self):
        """
        The note. Maximum length: 512 characters.
        """
        return self.__note

    @note.setter
    def note(self, value):
        self.__note = value
    @property
    def action(self):
        """
        The action. Maximum length: 32 characters.
        """
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = value
    @property
    def note_time(self):
        """
        The note time. Maximum length: 24 characters.
        """
        return self.__note_time

    @note_time.setter
    def note_time(self, value):
        self.__note_time = value


    

    def to_ams_dict(self):
        params = dict()
        if hasattr(self, "note_id") and self.note_id is not None:
            params['noteId'] = self.note_id
        if hasattr(self, "note") and self.note is not None:
            params['note'] = self.note
        if hasattr(self, "action") and self.action is not None:
            params['action'] = self.action
        if hasattr(self, "note_time") and self.note_time is not None:
            params['noteTime'] = self.note_time
        return params


    def parse_rsp_body(self, response_body):
        if isinstance(response_body, str): 
            response_body = json.loads(response_body)
        if 'noteId' in response_body:
            self.__note_id = response_body['noteId']
        if 'note' in response_body:
            self.__note = response_body['note']
        if 'action' in response_body:
            self.__action = response_body['action']
        if 'noteTime' in response_body:
            self.__note_time = response_body['noteTime']

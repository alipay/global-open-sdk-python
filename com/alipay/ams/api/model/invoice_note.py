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
        Unique identifier for this note within the array (UUID). Cannot be null.
        """
        return self.__note_id

    @note_id.setter
    def note_id(self, value):
        self.__note_id = value
    @property
    def note(self):
        """
        The actual note content. Provided by the merchant when performing an action on the invoice. Cannot be null.
        """
        return self.__note

    @note.setter
    def note(self, value):
        self.__note = value
    @property
    def action(self):
        """
        The action that triggered this note. Allowed values: &#x60;CREATE&#x60; - invoice created; &#x60;UPDATE&#x60; - invoice updated; &#x60;FINALIZE&#x60; - invoice finalized (DRAFT-&gt;OPEN); &#x60;VOID&#x60; - invoice voided; &#x60;MARK_UNCOLLECTIBLE&#x60; - invoice marked uncollectible; &#x60;PAID&#x60; - payment confirmed. Cannot be null.
        """
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = value
    @property
    def note_time(self):
        """
        ISO 8601 timestamp of when the note was created. Cannot be null.
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

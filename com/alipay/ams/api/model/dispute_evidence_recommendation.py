class DisputeEvidenceRecommendation(object):
    """An evidence item recommended for defending a dispute."""

    def __init__(self):
        self.__evidence_tag = None
        self.__obtained = None
        self.__win_rate_contribution = None

    @property
    def evidence_tag(self):
        """Evidence tag."""
        return self.__evidence_tag

    @evidence_tag.setter
    def evidence_tag(self, value):
        self.__evidence_tag = value

    @property
    def obtained(self):
        """Whether Antom has already obtained this evidence."""
        return self.__obtained

    @obtained.setter
    def obtained(self, value):
        self.__obtained = value

    @property
    def win_rate_contribution(self):
        """Optional contribution level: HIGH, MEDIUM or LOW."""
        return self.__win_rate_contribution

    @win_rate_contribution.setter
    def win_rate_contribution(self, value):
        self.__win_rate_contribution = value

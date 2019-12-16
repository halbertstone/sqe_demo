class Opportunity_Exception(Exception):
    """
    A root exception for the testing of Opportunity Application
    All exceptions used within these tests are subclasses
    """

    def __init__(self, message):
        super(Opportunity_Exception, self).__init__(message)


class Opportunity_Exception_Not_Implemented(Opportunity_Exception):
    pass

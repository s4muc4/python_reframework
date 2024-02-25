
# Business Exception
class BusinessRuleException(Exception):
    def __init__(self, message="Business Rule Exception", source=None, business_error_code=None, msg=None):
        super().__init__(message)
        self.source = source
        self.business_error_code = business_error_code
        self.msg = msg
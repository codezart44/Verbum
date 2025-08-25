class EndpointError(Exception): pass
class PayloadError(EndpointError): pass

class ServiceError(Exception): pass
class ParameterError(ServiceError): pass

class QueryError(Exception): pass
class InsertError(QueryError): pass
class UpdateError(QueryError): pass
class SelectError(QueryError): pass
class DeleteError(QueryError): pass

# class UnexpectedError(Exception): pass
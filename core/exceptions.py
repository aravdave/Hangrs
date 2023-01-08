from rest_framework.views import exception_handler

def core_exception_handler(exc, context):
    """Method that accepts all exceptions and handles certain types of errors"""
    # Gets the response from django's exception handler
    response = exception_handler(exc, context)
    
    # dictionarity that specifies all the handled exception classes and their methods
    handlers = {
        'ProfileDoesNotExist':_handle_generic_error,
        'ValidationError': _handle_generic_error
    }
    
    # Extracts the type of exception from the exc parameter
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        
        # Returns the response from the respective method if the exception is handled here
        return handlers[exception_class](exc, context, response)

    # Returns django's exception handler
    return response

def _handle_generic_error(exc, context, response):
    """Wraps DRF's exception response with 'errors'"""
    
    response.data = {
        'errors': response.data
    }

    return response
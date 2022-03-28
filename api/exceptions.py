from rest_framework.views import exception_handler

def my_exception_handler(exc, context):    
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None:
        response.data["message"] = str(exc)
        response.data["results"] = None
        del response.data["detail"]
    return response
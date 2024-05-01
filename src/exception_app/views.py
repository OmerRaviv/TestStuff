from django.http import HttpResponse
import sentry_sdk

# Initialize Sentry with the DSN provided
sentry_sdk.init(dsn="https://895585edfbb9b7109ab756025ca94e96@o4507172871340032.ingest.us.sentry.io/4507177524461568")

# Import helper modules for exception throwing
from . import helper1, helper2, helper3, helper4, helper5

# Dictionary mapping exception names to functions
exception_functions = {
    'exception1': helper1.throw_exception1,
    'exception2': helper2.throw_exception2,
    'exception3': helper3.throw_exception3,
    'exception4': helper4.throw_exception4,
    'exception5': helper5.throw_exception5,
}

def trigger_exception(request):
    # Get the exception type from the query string parameter
    exception_type = request.GET.get('exception')
    if exception_type in exception_functions:
        try:
            # Call the function to throw the exception
            exception_functions[exception_type]()
        except Exception as e:
            # Capture the exception in Sentry
            sentry_sdk.capture_exception(e)
            return HttpResponse("Exception captured in Sentry.")
    else:
        return HttpResponse("No valid exception type provided.")

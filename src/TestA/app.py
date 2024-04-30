import sentry_sdk
import time

# Initialize Sentry with the DSN provided
sentry_sdk.init(dsn="https://895585edfbb9b7109ab756025ca94e96@o4507172871340032.ingest.us.sentry.io/4507177524461568")

# Import additional modules for exception throwing
import helper1
import helper2
import helper3
import helper4
import helper5

def throw_exception():
    while True:
        try:
            # Call functions from helper modules that throw exceptions
            helper1.throw_exception1()
            helper2.throw_exception2()
            helper3.throw_exception3()
            helper4.throw_exception4()
            helper5.throw_exception5()
        except Exception as e:
            # Capture the exception in Sentry
            sentry_sdk.capture_exception(e)
            print("Exception captured in Sentry.")
        # Wait for 5 seconds before throwing the next exception
        time.sleep(5)

if __name__ == "__main__":
    throw_exception()

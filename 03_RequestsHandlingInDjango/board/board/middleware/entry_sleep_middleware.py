import time


class EntrySleepMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # time.sleep(1)
        responce = self.get_response(request)

        return responce

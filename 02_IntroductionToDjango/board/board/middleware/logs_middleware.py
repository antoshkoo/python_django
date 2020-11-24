import datetime as dt


class LogsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        current_time = dt.datetime.now().strftime('[%d/%m/%Y %H:%M:%S]')
        current_url = request.get_full_path()
        current_method = request.META.get('REQUEST_METHOD')

        file = open('logs.txt', 'a+')
        file.write(f'{current_time} {current_url} {current_method}\n')
        file.close()

        responce = self.get_response(request)
        return responce

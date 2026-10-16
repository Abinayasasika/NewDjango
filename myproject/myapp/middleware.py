import time
class RequestLoggingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print("Requested URL: ",request.path)

        response = self.get_response(request)

        print("Response Status: ",response.status_code)

        return response

class LoadTimeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        start_time=time.time()
        response=self.get_response(request)
        end_time=time.time()
        load_time=end_time-start_time
        print(f"page loaded in {load_time:.4f}seconds")
        return response

count = 0
class VisitCountMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        global count
        count += 1
        print(f"total visits: {count}")

        response = self.get_response(request)
        return response
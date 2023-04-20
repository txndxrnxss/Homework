import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.decorators.http import require_http_methods
import requests


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def index(request, factorial_json):

        nums = n = int(factorial_json)
        factorial = 1
        while int(n) > 1:
            factorial *= int(n)
            n = int(n) - 1
        back = json.dumps({"number": nums, "factorial": factorial})
        return HttpResponse(back)

class MyClassBasedView(View):

    def get(self, request, number):

        url_k = 'https://api.kanye.rest'
        a = [requests.get(url_k).json()['quote'] for _ in range(int(number))]
        return render(request, 'quote_21.html', {"quotes": a})
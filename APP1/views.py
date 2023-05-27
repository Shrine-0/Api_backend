from django.http import HttpResponse
from django.shortcuts import render  
from django.http import JsonResponse

# import sys 
# sys.path.append('/OCR_demo')

from OCR_demo import Api_check



def veryfi_api(request):
    
    data={
        'name':'veryfi'
    }
    return JsonResponse(data)
    # return HttpResponse("HEY THIS si working")

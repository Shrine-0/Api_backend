from django.http import HttpResponse
from django.shortcuts import render  
from django.http import JsonResponse
import json 
import sys 
sys.path.append('/OCR_demo')


f =  open('./OCR_demo/Result.json')
result = json.load(f)

for i in result['line_items']:
    print(i)
def veryfi_api(request):
    
    data={
        'result':result,
        'status':'success'
    }
    return JsonResponse(data)
    # return HttpResponse("HEY THIS si working")

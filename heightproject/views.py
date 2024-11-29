from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def save_comparison(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Here you can add database storage logic if needed
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

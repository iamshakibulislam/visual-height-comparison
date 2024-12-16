from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from blog.models import blogpost

def home(request):
    get_all = blogpost.objects.all()[:10]
    return render(request, 'index.html',{"posts":get_all})

@csrf_exempt
def save_comparison(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Here you can add database storage logic if needed
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

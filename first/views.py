from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import Mat
from .utils import pagination_manager

# Create your views here.

qs = Mat.objects.all()

def index(request):
    all_matches = Mat.objects.all()
    page_obj, pages = pagination_manager(all_matches,5,2,request.GET.get('page',1))
    return render (request,'index.html', context={'page_obj':page_obj,'pages':pages})

def sorts(request):
    global qs
    if request.method == 'POST':
        if request.POST['condition'] == 'more':
            if not request.POST['value']:
                qs = qs.order_by(request.POST['column'])
            elif request.POST['value'] and request.POST['column'] == 'match_count':
                qs = qs.filter(match_count__gt=int(request.POST['value']))
            elif request.POST['value'] and request.POST['column'] == 'match_distance':
                qs = qs.filter(match_distance__gt=int(request.POST['value']))
        elif request.POST['condition'] == 'less':
            if not request.POST['value']:
                qs = qs.order_by(f"-{request.POST['column']}")
            elif request.POST['value'] and request.POST['column'] == 'match_count':
                qs = qs.filter(match_count__lt=int(request.POST['value']))       # количество меньше
            elif request.POST['value'] and request.POST['column'] == 'match_distance':
                qs = qs.filter(match_distance__lt=int(request.POST['value']))     # расстояние меньше
        elif request.POST['condition'] == 'contains':                            # значение содержит
            if request.POST['column'] == 'match_name':
                qs = qs.filter(match_name__icontains=request.POST['value'])      # название содержит
            elif request.POST['column'] == 'match_count' and request.POST['value']:
                qs = qs.filter(match_count__gte=int(request.POST['value']))       # количество "содержит" (больше либо равно)
            elif request.POST['column'] == 'match_distance' and request.POST['value']:
                qs = qs.filter(match_distance__gte=int(request.POST['value']))     # расстояние "содержит" (больше либо равно)
        elif request.POST['condition'] == 'equals':                              # значение равно
            if request.POST['column'] == 'match_name':
                qs = qs.filter(title__iexact=request.POST['value'])          # название равно
            elif request.POST['column'] == 'match_count' and request.POST['value']:
                qs = qs.filter(match_count=int(request.POST['value']))            # количество равно
            elif request.POST['column'] == 'match_distance' and request.POST['value']:
                qs = qs.filter(match_distance=int(request.POST['value']))           # расстояние равно
        else:
            qs = qs.all()


    paginator = Paginator(qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'sort.html', context)

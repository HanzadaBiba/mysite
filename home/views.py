from django.shortcuts import render,get_object_or_404
from django.views.generic.base import View
# Create your views here.
from workers.models import *
class HomeView(View):

    def get(self,request):
        units=Units.objects.all()
        return render(request,'home/index.html',locals())

def units_detail(request,slug):
    unit=get_object_or_404(Units,slug=slug)
    return render(request,'home/units_detail.html',locals())
def departament_detail(request,slug):
    departament=get_object_or_404(Departaments,slug=slug)
    print(departament.departament_block_set)
    return render(request,'home/departament_detail.html',locals())
def departament_block_detail(request,slug):
    departament_block=get_object_or_404(Departament_block,slug=slug)
    print(departament_block.workers_set.all())
    return render(request,'home/departament_block_detail.html',locals())
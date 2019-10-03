from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Car
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):
    def get(self, request, *args, **kwargs):
        form = SelectForm(request.GET)
        if form.is_valid():
            car_inst = get_object_or_404(Car, pk=form.cleaned_data["id"])
            return JsonResponse(model_to_dict(car_inst))
        else:
            return HttpResponse("There is no such id", status=404)

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        form = DeleteForm(request.GET)
        if form.is_valid():
            car_inst = get_object_or_404(Car, pk=form.cleaned_data["id"]) 
            car_inst.delete()
            return HttpResponse(status = 204)
        else:
            return HttpResponse("There is no such id", status=404)


    @csrf_exempt
    def post(self, request, *args, **kwargs):
        form = CreateCarForm(request.GET)
        if form.is_valid():
            car_inst = Car.create(**form.cleaned_data)
            car_inst.save()
            return HttpResponse(status = 201)
        else:
            return HttpResponse("Data is not valid", status=404)


    @csrf_exempt
    def update(self, request, *args, **kwargs):
        form = UpdateForm(request.GET)
        if form.is_valid():
            car_inst = get_object_or_404(Car, pk=form.cleaned_data["id"]) 
            car_inst.update(**form.cleaned_data)
            car_inst.save()
            return HttpResponse(status = 201)
        else:
            return HttpResponse("There is no such id", status=404)










@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index." + str(666))

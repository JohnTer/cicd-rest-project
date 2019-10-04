from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from .models import Car, Driver

@method_decorator(csrf_exempt, name='dispatch')
class CarView(View):
    def get(self, request, *args, **kwargs):
        form = SelectForm(request.GET)
        if form.is_valid():
            car_inst = get_object_or_404(Car, pk=form.cleaned_data["id"])
            return JsonResponse(model_to_dict(car_inst))
        else:
            return HttpResponse("Invalid id", status=422)

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        form = DeleteForm(request.GET)
        if form.is_valid():
            car_inst = get_object_or_404(Car, pk=form.cleaned_data["id"]) 
            car_inst.delete()
            return HttpResponse(status = 204)
        else:
            return HttpResponse("There is no such id", status=422)


    @csrf_exempt
    def post(self, request, *args, **kwargs):
        form = CreateCarForm(request.GET)
        if form.is_valid():
            car_inst = Car.create(**form.cleaned_data)
            car_inst.save()
            return HttpResponse(car_inst.id, status = 201)
        else:
            return HttpResponse("Data is not valid", status=422)


    @csrf_exempt
    def put(self, request, *args, **kwargs):
        form = UpdateForm(request.GET)
        if form.is_valid():
            car_inst = get_object_or_404(Car, pk=form.cleaned_data["id"]) 
            del form.cleaned_data["id"]
            car_inst.update(**form.cleaned_data)
            car_inst.save()
            return HttpResponse(car_inst.id, status = 200)
        else:
            return HttpResponse("There is no such id", status=422)




@method_decorator(csrf_exempt, name='dispatch')
class DriverView(View):
    def get(self, request, *args, **kwargs):
        form = SelectForm(request.GET)
        if form.is_valid():
            driver_inst = get_object_or_404(Driver, pk=form.cleaned_data["id"])
            return JsonResponse(model_to_dict(driver_inst))
        else:
            return HttpResponse("There is no such id", status=422)

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        form = DeleteForm(request.GET)
        if form.is_valid():
            driver_inst = get_object_or_404(Driver, pk=form.cleaned_data["id"]) 
            driver_inst.delete()
            return HttpResponse(status = 204)
        else:
            return HttpResponse("There is no such id", status=422)


    @csrf_exempt
    def post(self, request, *args, **kwargs):
        form = CreateDriverForm(request.GET)
        if form.is_valid():
            try:
                car_inst = Car.objects.get(pk=form.cleaned_data['car_id'])
            except Car.DoesNotExist:
                return HttpResponse("There is no such car id", status=422)
            driver_inst = Driver.create(first_name=form.cleaned_data['first_name'],second_name = form.cleaned_data['second_name'], car_inst=car_inst)
            driver_inst.save()
            return HttpResponse(driver_inst.id, status = 201)
        else:
            return HttpResponse("Data is not valid", status=422)



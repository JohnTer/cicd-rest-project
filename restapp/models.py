from django.db import models
from django.core import serializers
import uuid


class Car(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    model = models.CharField(max_length=255)
    body_type = models.CharField(max_length = 255)
    seats = models.IntegerField()

    def __str__(self):
        return self.model

    @classmethod
    def create(cls, model, body_type, seats):
        car_id = str(uuid.uuid4())
        car = cls(id = car_id, 
        model = model, 
        body_type = body_type, 
        seats = seats)
        return car
    
    def update(self, model, body_type, seats):
        self.model = model 
        self.body_type = body_type
        self.seats = seats



class Driver(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    car_id = models.ForeignKey('Car', on_delete=models.CASCADE)

    @classmethod
    def create(cls, first_name, second_name, car_id):
        driver_id = str(uuid.uuid4())
        driver = cls(id = driver_id, 
        first_name = first_name,
        second_name = second_name, 
        car_id = car_id)
        return driver 

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)



        




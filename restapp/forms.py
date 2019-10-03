from django import forms
from django.core.exceptions import ValidationError
import uuid

class CreateCarForm(forms.Form):
    model = forms.CharField()
    body_type = forms.CharField()
    seats = forms.IntegerField()


class CreateDriverForm(forms.Form):
    first_name = forms.CharField()
    second_name = forms.CharField()
    car_id = forms.UUIDField()


    
    
class UpdateForm(forms.Form):
    id = forms.CharField()
    model = forms.CharField()
    body_type = forms.CharField()
    seats = forms.IntegerField()
    def clean_id(self):
        data = self.cleaned_data['id']
        try:
            uuid.UUID(data)
        except ValueError:
            raise ValidationError("Invalid id")
        return data


class DeleteForm(forms.Form):
    id = forms.CharField()
    def clean_id(self):
        data = self.cleaned_data['id']
        try:
            uuid.UUID(data)
        except ValueError:
            raise ValidationError("Invalid id")
        return data


class SelectForm(forms.Form):
    id = forms.CharField()
    def clean_id(self):
        data = self.cleaned_data['id']
        try:
            uuid.UUID(data)
        except ValueError:
            raise ValidationError("Invalid id")
        return data
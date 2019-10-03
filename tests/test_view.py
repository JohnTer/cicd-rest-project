from django.test import TestCase
from restapp.models import Car
from uuid import uuid4
from django.urls import reverse
from json import loads

class ViewGetTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        id1 = '6d348bf9-e572-46b3-b2d2-501ede6e8e01'
        obj_data1 = {
        'id': id1,
        'model': 'E-klasse',
        'body_type': 'CUV',
        'seats': 5
        }
        Car.objects.create(**obj_data1)

        id2 = 'd97a238d-92ca-4eb2-9137-f228c6956dce'
        obj_data2 = {
        'id': id2,
        'model': 'X5M',
        'body_type': 'CUV',
        'seats': 6
        }

        Car.objects.create(**obj_data2)


    def test_get_exist_car(self):
        #response = self.client.get(reverse('car', kwargs={'id': 'd97a238d-92ca-4eb2-9137-f228c6956dce'}))
        response = self.client.get('/api/v1/car/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dce'))
        self.assertEqual(response.status_code, 200)
        content = loads(response.content.decode('utf8').replace("'", '"'))
        self.assertEqual('X5M', content['model'])
        self.assertEqual('CUV', content['body_type'])
        self.assertEqual(6, content['seats'])


    
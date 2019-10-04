from django.test import TestCase
from restapp.models import Car
from uuid import uuid4
from django.urls import reverse
from json import loads

class ViewCarGetTest(TestCase):
    
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
        response = self.client.get('/api/v1/car/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dce'))
        self.assertEqual(response.status_code, 200)
        content = loads(response.content.decode('utf8').replace("'", '"'))
        self.assertEqual('X5M', content['model'])
        self.assertEqual('CUV', content['body_type'])
        self.assertEqual(6, content['seats'])

    def test_get_no_exist_car(self):
        response = self.client.get('/api/v1/car/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dff'))
        self.assertEqual(response.status_code, 404)


    def test_get_invalid_id(self):
        response = self.client.get('/api/v1/car/?id={}'.format('12345'))
        self.assertEqual(response.status_code, 400)




class ViewCarDeleteTest(TestCase):
    
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


    def test_delete_correct(self):
        self.client.delete('/api/v1/car/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dce'))
        #Car.objects.get(pk='d97a238d-92ca-4eb2-9137-f228c6956dce')
        self.assertRaises(Car.DoesNotExist, lambda: Car.objects.get(pk='d97a238d-92ca-4eb2-9137-f228c6956dce'))


    def test_delete_id_not_found(self):
        response = self.client.delete('/api/v1/car/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dff'))
        self.assertEqual(response.status_code, 404)

    def test_delete_invalid_id(self):
        response = self.client.delete('/api/v1/car/?id={}'.format('abcd'))
        self.assertEqual(response.status_code, 400)
        



class ViewCarPostTest(TestCase):
    
    def test_post_ok(self):
        json_dict = {
        'model': 'E-klasse',
        'body_type': 'CUV',
        'seats': 5
        }
        url = "http://127.0.0.1:8000/api/v1/car/?model={model}&body_type={body_type}&seats={seats}".format(**json_dict)
        response = self.client.post(url)
        car_id_resp = response.content.decode()
        Car.objects.get(pk=car_id_resp)


    def test_post_wrong_seats_value(self):
        json_dict = {
        'model': 'E-klasse',
        'body_type': 'CUV',
        'seats': "abcd"
        }
        url = "http://127.0.0.1:8000/api/v1/car/?model={model}&body_type={body_type}&seats={seats}".format(**json_dict)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

        
    def test_post_wrong_body_empty(self):
        json_dict = {
        'model': 'E-klasse',
        'body_type': '',
        'seats': "abcd"
        }
        url = "http://127.0.0.1:8000/api/v1/car/?model={model}&body_type={body_type}&seats={seats}".format(**json_dict)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)



class ViewCarPutTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        id1 = 'd97a238d-92ca-4eb2-9137-f228c6956dce'
        obj_data1 = {
        'model': 'X5M',
        'body_type': 'CUV',
        'seats': 6
        }

        c = Car.create(**obj_data1)
        c.id = id1
        c.save()
    
    def test_put_ok(self):
        json_dict = {
        'id': 'd97a238d-92ca-4eb2-9137-f228c6956dce',
        'model': 'A-klasse',
        'body_type': 'CUV',
        'seats': 5
        }
        url = "http://127.0.0.1:8000/api/v1/car/?id={id}&model={model}&body_type={body_type}&seats={seats}".format(**json_dict)
        response = self.client.put(url)
        car_id_resp = response.content.decode()
        car_obj = Car.objects.get(pk=car_id_resp)
        self.assertEqual(car_obj.model, 'A-klasse')


    def test_put_unknown_id(self):
        json_dict = {
        'id': 'd97a238d-92ca-4eb2-9137-f228c6956dff',
        'model': 'A-klasse',
        'body_type': 'CUV',
        'seats': 5
        }
        url = "http://127.0.0.1:8000/api/v1/car/?id={id}&model={model}&body_type={body_type}&seats={seats}".format(**json_dict)
        response = self.client.put(url)
        self.assertEqual(response.status_code, 404)


    def test_put_wrong_seats_type(self):
        json_dict = {
        'id': 'd97a238d-92ca-4eb2-9137-f228c6956dce',
        'model': 'A-klasse',
        'body_type': 'CUV',
        'seats': "abcd"
        }
        url = "http://127.0.0.1:8000/api/v1/car/?id={id}&model={model}&body_type={body_type}&seats={seats}".format(**json_dict)
        response = self.client.put(url)
        self.assertEqual(response.status_code, 400)

    def test_put_no_seats_field(self):
        json_dict = {
        'id': 'd97a238d-92ca-4eb2-9137-f228c6956dce',
        'model': 'A-klasse',
        'body_type': 'CUV'
        }
        url = "http://127.0.0.1:8000/api/v1/car/?id={id}&model={model}&body_type={body_type}".format(**json_dict)
        response = self.client.put(url)
        self.assertEqual(response.status_code, 400) 

    







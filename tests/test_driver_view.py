from django.test import TestCase
from restapp.models import Driver, Car
from uuid import uuid4
from django.urls import reverse
from json import loads


class ViewDriverGetTest(TestCase):
    
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
        'first_name': 'A',
        'second_name': 'B',
        }

        car_inst = Car.objects.get(pk=id1)
        driver_inst = Driver.create(first_name=obj_data2['first_name'],second_name = obj_data2['second_name'], car_inst=car_inst)
        driver_inst.id = id2
        driver_inst.save()



    def test_get_exist_driver(self):
        response = self.client.get('/api/v1/driver/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dce'))
        self.assertEqual(response.status_code, 200)
        content = loads(response.content.decode('utf8').replace("'", '"'))
        self.assertEqual('A', content['first_name'])
        self.assertEqual('B', content['second_name'])
        self.assertEqual('6d348bf9-e572-46b3-b2d2-501ede6e8e01', content['car_id'])

        
    def test_get_no_exist_driver(self):
        response = self.client.get('/api/v1/driver/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dff'))
        self.assertEqual(response.status_code, 404)

    def test_get_invalid_id_driver(self):
        response = self.client.get('/api/v1/driver/?id={}'.format('12345'))
        self.assertEqual(response.status_code, 422)



class ViewDriverDeleteTest(TestCase):
    
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
        'first_name': 'A',
        'second_name': 'B',
        }

        car_inst = Car.objects.get(pk=id1)
        driver_inst = Driver.create(first_name=obj_data2['first_name'],second_name = obj_data2['second_name'], car_inst=car_inst)
        driver_inst.id = id2
        driver_inst.save()

    def test_delete_correct(self):
        self.client.delete('/api/v1/driver/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dce'))
        self.assertRaises(Car.DoesNotExist, lambda: Car.objects.get(pk='d97a238d-92ca-4eb2-9137-f228c6956dce'))


    def test_delete_id_not_found(self):
        response = self.client.delete('/api/v1/driver/?id={}'.format('d97a238d-92ca-4eb2-9137-f228c6956dff'))
        self.assertEqual(response.status_code, 404)

    def test_delete_invalid_id(self):
        response = self.client.delete('/api/v1/driver/?id={}'.format('abcd'))
        self.assertEqual(response.status_code, 422)



class ViewDriverPostTest(TestCase):

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
    
    def test_post_ok(self):
        id1 = '6d348bf9-e572-46b3-b2d2-501ede6e8e01'
        json_dict = {
        'car_id': id1,
        'first_name': 'A',
        'second_name': 'B',
        }
        url = "http://127.0.0.1:8000/api/v1/driver/?car_id={car_id}&first_name={first_name}&second_name={second_name}".format(**json_dict)
        response = self.client.post(url)
        driver_id_resp = response.content.decode()
        Driver.objects.get(pk=driver_id_resp)
        


    def test_post_wrong_car_id_value(self):
        id1 = '6d348bf9-e572-46b3-b2d2-501ede6e8eff'
        json_dict = {
        'car_id': id1,
        'first_name': 'A',
        'second_name': 'B',
        }
        url = "http://127.0.0.1:8000/api/v1/driver/?car_id={car_id}&first_name={first_name}&second_name={second_name}".format(**json_dict)
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 422)


    def test_post_wrong_body_empty(self):
        json_dict = {
        'car_id': '',
        'first_name': 'A',
        'second_name': 'B',
        }
        url = "http://127.0.0.1:8000/api/v1/driver/?car_id={car_id}&first_name={first_name}&second_name={second_name}".format(**json_dict)
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 424)

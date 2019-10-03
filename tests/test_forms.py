from restapp.forms import UpdateForm, DeleteForm, CreateCarForm, SelectForm
from django.test import TestCase
from uuid import uuid4


class DeleteFormTest(TestCase):
    def test_update_clean_id_int(self):
        obj_id = {'id': 12345}
        form = DeleteForm(obj_id)
        self.assertFalse(form.is_valid())

    def test_update_clean_id_str(self):
        obj_id = {'id': "123456"}
        form = DeleteForm(obj_id)
        self.assertFalse(form.is_valid())

    def test_update_clean_id_uuid(self):
        obj_id = {'id': str(uuid4())}
        form = DeleteForm(obj_id)
        self.assertTrue(form.is_valid())


class SelectFormTest(TestCase):
    def test_update_clean_id_int(self):
        obj_id = {'id': 12345}
        form = SelectForm(obj_id)
        self.assertFalse(form.is_valid())

    def test_update_clean_id_str(self):
        obj_id = {'id': "123456"}
        form = SelectForm(obj_id)
        self.assertFalse(form.is_valid())

    def test_update_clean_id_uuid(self):
        obj_id = {'id': str(uuid4())}
        form = SelectForm(obj_id)
        self.assertTrue(form.is_valid())


class UpdateCreateFormTest(TestCase):
    def test_update_clean_id_uuid(self):
        obj_data = {'id': str(uuid4()),
        'model': 'E-klasse',
        'body_type': 'CUV',
        'seats': 10
        }
        form = UpdateForm(obj_data)
        self.assertTrue(form.is_valid())
        
    







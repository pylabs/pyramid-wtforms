import unittest
from pyramid import testing
from pyramid_wtforms import Form, FileField
from cgi import FieldStorage as cgiFieldStorage
from pyramid_wtforms.storage import FieldStorage

class TestPyramidWTFormsFieldsFileField(unittest.TestCase):

    def setUp(self):
        class TestForm(Form):
            file = FileField('testfile')
        self.form = TestForm()

        request = testing.DummyRequest()
        self.config = testing.setUp(request=request)

    def tearDown(self):
        testing.tearDown()

    def test_process_data_with_non_singular_valuelist_should_raise_error(self):
        with self.assertRaises(ValueError):
            self.form.file.process_formdata([FieldStorage(cgiFieldStorage()), FieldStorage(cgiFieldStorage())])

    def test_process_data_with_valuelist_should_set_data_properly(self):
        test_objects = [FieldStorage(cgiFieldStorage())]
        self.form.file.process_formdata(test_objects)
        self.assertEqual(self.form.file.data, test_objects[0])

    def test_process_data_without_file_upload_should_set_data_to_None(self):
        self.form.file.process_formdata([b''])
        self.assertIsNone(self.form.file.data)
    
    def test_process_data_without_a_correspoding_upload_file_should_raise_error(self):
        with self.assertRaises(ValueError):
            self.form.file.process_formdata([])

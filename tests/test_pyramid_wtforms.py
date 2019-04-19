import unittest

class TestPyramidWTForms(unittest.TestCase):

    def test_pyramid_wtforms_should_have_essential_elements(self):
        import pyramid_wtforms
        essential_elements = [ i for i in dir(pyramid_wtforms) if i[0].isupper()]
        self.assertEqual(
            ['BooleanField', 'DateField', 'DateTimeField', 'DecimalField',
             'Field', 'FieldList', 'FileField', 'Flags', 'FloatField', 'Form',
             'FormField', 'HiddenField', 'IntegerField', 'Label', 'MultipleFileField',
             'MultipleFilesField', 'PasswordField', 'RadioField', 'SecureForm',
             'SelectField', 'SelectFieldBase', 'SelectMultipleField',
             'StringField', 'SubmitField', 'TextAreaField', 'TextField', 'TimeField',
             'ValidationError'],
             essential_elements
        )

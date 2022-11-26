""" Unit testing for forms """
from django.test import TestCase
from .forms import BuildForm, CommentForm


class TestBuildForm(TestCase):

    def test_build_image_is_required(self):
        form = BuildForm({'build_image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('build_image', form.errors.keys())
        self.assertEqual(form.errors['build_image'][0],
                         'No file selected!')

    def test_build_make_is_required(self):
        form = BuildForm({'make': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('make', form.errors.keys())
        self.assertEqual(form.errors['make'][0],
                         'This field is required.')

    def test_build_model_is_required(self):
        form = BuildForm({'model': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('model', form.errors.keys())
        self.assertEqual(form.errors['model'][0],
                         'This field is required.')

    def test_build_year_is_required(self):
        form = BuildForm({'year': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('year', form.errors.keys())
        self.assertEqual(form.errors['year'][0],
                         'This field is required.')

    def test_build_overview_is_required(self):
        form = BuildForm({'overview': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('overview', form.errors.keys())
        self.assertEqual(form.errors['overview'][0],
                         'This field is required.')

    def test_build_specifications_is_required(self):
        form = BuildForm({'specifications': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('specifications', form.errors.keys())
        self.assertEqual(form.errors['specifications'][0],
                         'This field is required.')

    def test_build_plans_is_required(self):
        form = BuildForm({'plans': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('plans', form.errors.keys())
        self.assertEqual(form.errors['plans'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BuildForm()
        self.assertEqual(form.Meta.fields,
                         ('build_image', 'make', 'model', 'year', 'overview',
                          'specifications', 'plans'))

"""
Forms For Creating Build Posts & Comments
"""
from .models import Comment, Build
from django import forms
from django_summernote.widgets import SummernoteWidget


class BuildForm(forms.ModelForm):
    """
    Build Post Form
    """
    class Meta:
        """
        Form Fields
        """
        model = Build
        fields = ('build_image', 'make', 'model', 'year',
                  'overview', 'specifications', 'plans')

        widgets = {
            'overview': SummernoteWidget(),
            'specifications': SummernoteWidget(),
            'plans': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(BuildForm, self).__init__(*args, **kwargs)
        self.fields[
            'build_image'
            ].label = "Upload a landscape image showcasing your build"
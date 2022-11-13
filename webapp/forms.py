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
                ].label = "Upload a landscape image of your build"
        self.fields[
                'overview'
                ].label = "Build Overview"
        self.fields[
                'specifications'
                ].label = "Build Specifications / Modifications"
        self.fields[
                'plans'
                ].label = "Future Plans / Recommendations"


class CommentForm(forms.ModelForm):
    """
    Add Comment Form
    """
    class Meta:
        """
        Form Fields
        """
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields[
                'body'
        ].label = ""

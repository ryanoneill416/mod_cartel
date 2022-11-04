from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.utils.text import slugify
from .models import Build, Comment
from .forms import BuildForm


class Home(View):
    """
    View for the home page
    Will show the featured builds of the week
    """

    def get(self, request):
        """
        get request to retrieve the home page
        with the featured posts included
        """
        featured_builds = Build.objects.filter(is_featured=True)[:4]
        context = {
            "featured_builds": featured_builds,
        }
        return render(request, 'index.html', context)


class Showcase(generic.ListView):
    """
    View for the 'Showcase' Page
    Will show all member's posted builds
    """

    model = Build
    queryset = Build.objects.order_by('-publish_date')
    template_name = 'showcase.html'
    paginate_by = 9

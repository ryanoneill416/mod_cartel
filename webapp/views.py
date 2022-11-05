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
    paginate_by = 6


class AddBuild(View):
    """
    View for adding a user's build
    """

    def get(self, request):
        """
        Retrieving the form
        """
        return render(request, "add_build.html", {"build_form": BuildForm()})

    def post(self, request):
        """
        Posting the build after form completion
        """
        build_form = BuildForm(request.POST, request.FILES)

        if build_form.is_valid():
            build = build_form.save(commit=False)
            build.member = request.user
            build.slug = slugify('-'.join([str(build.member), str(build.year),
                                           build.make, build.model]),
                                 allow_unicode=False)
            build.save()
            return redirect('showcase')
        else:
            build_form = BuildForm()

            return render(
                request, "add_build.html",
                {
                    "build_form": build_form
                },
            )

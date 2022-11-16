from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Build, Comment
from .forms import BuildForm, CommentForm


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


class BuildDetail(View):
    """
    View showing all the build details of
    a specified member's build
    """

    def get(self, request, slug):
        """
        get request to retreive the build details
        for the build in question
        """

        queryset = Build.objects.all()
        build = get_object_or_404(queryset, slug=slug)
        comments = build.build_comments.order_by('comment_date')
        liked = False
        if build.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'build_detail.html',
            {
                "build": build,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug):
        """
        post request to add a comment to a post
        """

        queryset = Build.objects.all()
        build = get_object_or_404(queryset, slug=slug)
        comments = build.build_comments.order_by('-comment_date')
        liked = False
        if build.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.build = build
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'build_detail.html',
            {
                "build": build,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class MyGarage(generic.ListView):
    """
    View for the 'My Garage' Page
    Will show all of a member's builds
    """

    def get(self, request):
        if request.user.is_authenticated:
            build = Build.objects.filter(member=request.user)

            paginator = Paginator(build, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(
                request, 'my_garage.html', {"page_obj": page_obj, })
        else:
            return render(request, 'my_garage.html')


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


class EditBuild(UpdateView):
    """
    View for editing a user's build
    """

    model = Build
    form_class = BuildForm
    template_name = 'edit_build.html'


@login_required
def delete_build(request, build_id):
    """
    Deletes a specified user build
    """

    build = get_object_or_404(Build, id=build_id)
    build.delete()
    return redirect(reverse('my_garage'))


@login_required
def delete_comment(request, comment_id):
    """
    Deletes a specified user comment
    """

    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect(reverse(
        'build_detail', args=[comment.build.slug]))

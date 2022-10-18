from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Build(models.Model):
    """ Member Build Model """
    make = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    slug = models.SlugField(max_length=200, unique=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member_builds")
    updated_date = models.DateTimeField(auto_now=True)
    year = models.PositiveSmallIntegerField()
    overview = models.TextField()
    specifications = models.TextField()
    plans = models.TextField()
    build_image = CloudinaryField('image')
    publish_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    featured_excerpt = models.CharField(max_length=300, blank=True)
    likes = models.ManyToManyField(User, related_name="build_likes", blank=True)
    saves = models.ManyToManyField(User, related_name="build_saves", blank=True)

    class Meta:
        """ Model is ordered in descending date order """
        ordering = ['-publish_date']

    def __str__(self):
        """ Generates string title """
        return f"{self.member}'s {self.make_and_model}"

    def number_of_likes(self):
        """ Counts number of likes on build """
        return self.likes.count()


class Comment(models.Model):
    """ Model for comments made by members """
    build = models.ForeignKey(Build, on_delete=models.CASCADE, related_name="build_comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Model is ordered in ascending date order """
        ordering = ['comment_date']

    def __str__(self):

        return f"Comment: {self.body} by {self.name}"

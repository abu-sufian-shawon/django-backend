
from django.urls import path

from . import views


app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", view=views.details, name="details"),
    path("<int:question_id>/results/", view=views.results, name="results"),
    path("<int:question_id>/vote/", view=views.vote, name="vote"),
]
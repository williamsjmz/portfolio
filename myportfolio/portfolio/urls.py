
from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("cv/", views.cv, name="cv"),
    path("hire_me/", views.hire_me, name="hire_me"),


    # API routes
    path("projects/get/all/", views.get_projects, name="get_projects"),
    path("profile/", views.profile, name="profile"),
    path("soft_skills/get/all/", views.get_soft_skills, name="get_soft_skills"),
    path("cv/get/all/experiences/", views.get_experiences, name="get_experiences"),
    path("cv/get/all/technologies/", views.get_technologies, name="get_technologies"),
    path("hire_me/send_email/", views.send_email, name="send_email"),
]
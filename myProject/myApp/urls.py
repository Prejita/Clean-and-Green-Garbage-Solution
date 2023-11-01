from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("about/", views.about, name="about"),
    path("blog_post1/", views.blog_post1, name="blog_post1"),
    path("blog_post2/", views.blog_post2, name="blog_post2"),
    path("blog_post3/", views.blog_post3, name="blog_post3"),
    path("blog_post4/", views.blog_post4, name="blog_post4"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("termsandconditions/", views.termsandconditions, name="termsandconditions"),
]
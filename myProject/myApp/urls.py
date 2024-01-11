from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="myApp/login.html"), name="login"),
    path("about/", views.about, name="about"),
    path("blog_post1/", views.blog_post1, name="blog_post1"),
    path("blog_post2/", views.blog_post2, name="blog_post2"),
    path("blog_post3/", views.blog_post3, name="blog_post3"),
    path("blog_post4/", views.blog_post4, name="blog_post4"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("termsandconditions/", views.termsandconditions, name="termsandconditions"),
    path("notifications/", views.notifications, name="notifications"),
    path("addevents/", views.addevents, name="addevents"),
    path('api/dustbin_data_receiver', views.dustbin_data_receiver, name='dustbin_data_receiver'),    
    path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('delete_all_notifications/', views.delete_all_notifications, name='delete_all_notifications'),
    path('create_event/', views.create_event, name='create_event'),

    ]

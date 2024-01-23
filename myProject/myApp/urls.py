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
    path('userrequest/', views.userrequest, name='userrequest'),
    path('api/dustbin_data_receiver', views.dustbin_data_receiver, name='dustbin_data_receiver'),    
    # path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('delete_all_notifications/', views.delete_all_notifications, name='delete_all_notifications'),
    path('create_event/', views.create_event, name='create_event'),
    path('events/', views.events, name='events'),
    path('notify/<int:notification_id>/', views.notify, name='notify'),
    path('get_events/', views.get_events, name='get_events'),
    path('register/', views.register, name='register'),
    path('submit_registration/', views.submit_registration, name='submit_registration'),
    path('clear_all_requests/', views.clear_all_requests, name='clear_all_requests'),
    path('delete_registration/', views.delete_registration, name='delete_registration'),
    path('accept_registration/', views.accept_registration, name='accept_registration'),
    path('decline_registration/', views.decline_registration, name='decline_registration'),
    path('delete_selected_notifications/', views.delete_selected_notifications, name='delete_selected_notifications'),
    ]

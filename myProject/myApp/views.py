from django.shortcuts import render,redirect
from django.contrib import messages
import serial
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Define your other views here

def index(request):
    context = {}
    return render(request, "myApp/index.html", context)

def login(request):
    context = {}
    return render(request, "myApp/login.html", context)

def about(request):
    context = {}
    return render(request, "myApp/about.html", context)

def blog_post1(request):
    context = {}
    return render(request, "myApp/blog-post-1.html", context)

def blog_post2(request):
    context = {}
    return render(request, "myApp/blog-post-2.html", context)

def blog_post3(request):
    context = {}
    return render(request, "myApp/blog-post-3.html", context)

def blog_post4(request):
    context = {}
    return render(request, "myApp/blog-post-4.html", context)

def blog(request):
    context = {}
    return render(request, "myApp/blog.html", context)

def contact(request):
    context = {}
    return render(request, "myApp/contact.html", context)

def dashboard(request):
    # You can retrieve messages from other views here and display them in your dashboard.
    messages_data = messages.get_messages(request)
    context = {'messages_data': messages_data}
    return render(request, "myApp/dashboard.html", context)

def termsandconditions(request):
    context = {}
    return render(request, "myApp/terms-and-conditions.html", context)

def notifications(request):
    context = {}
    return render(request, "myApp/notifications.html", context)

# from django.contrib import messages
# from django.shortcuts import redirect
# ser = serial.Serial('COM6', 9600)

# @csrf_exempt  # Add the csrf_exempt decorator here
# def handle_arduino_data(request):
#     if request.method == 'POST':
#         data = request.POST.get('fill_level')  # Get the 'fill_level' data from the POST request
#         # Process the data as needed
#         if data:
#             if data == 'dustbin_full':
#                 messages.error(request, 'The dustbin is full. Please take necessary action.')
#                 print("Dustbin full notification sent.")
#             else:
#                 print("Data received:", data)  # Print the data to the console for testing purposes
#             # Perform further processing or save the data to a database or send it to another system

#     # Redirect to the notifications page after setting the message
#     return redirect('notifications')

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


# Django view to handle incoming data from ESP32 and save it to the database
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Use this decorator to exempt CSRF verification (for testing purposes)
def save_dustbin_status(request):
    if request.method == 'POST':  # Ensure the view only responds to POST requests
        try:
            received_data = json.loads(request.body)
            # Process received_data as needed
            print("Received data:", received_data)
            # Perform actions based on the received data
            
            # Return a success response
            return JsonResponse({'message': 'Data received successfully'})
        except json.JSONDecodeError as e:
            # Handle JSON decoding errors
            return JsonResponse({'error': 'Invalid JSON format'})
    else:
        # For other methods (GET, PUT, DELETE, etc.), return a method not allowed response
        return JsonResponse({'error': 'Method not allowed'}, status=405)

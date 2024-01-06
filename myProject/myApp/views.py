from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import DustbinData  # Import the DustbinData model

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

@csrf_exempt
def dustbin_data_receiver(request):
    if request.method == 'POST':
        try:
            received_data = json.loads(request.body)
            distance = received_data.get('distance')
            status = received_data.get('status')

            # Store the received data in the DustbinData model
            DustbinData.objects.create(distance=distance, status=status)

            return JsonResponse({'message': 'Data received and processed successfully'})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def dashboard(request):
    # Retrieve the latest DustbinData instance 
    latest_data = DustbinData.objects.latest('timestamp')
    context = {
        'distance': latest_data.distance,
        'status': latest_data.status
    }
    return render(request, "myApp/dashboard.html", context)

# @csrf_exempt
# def dustbin_data_receiver(request):
#     if request.method == 'POST':
#         try:
#             received_data = json.loads(request.body)
#             distance = received_data.get('distance')
#             status = received_data.get('status')
#             kathmandu_time = received_data.get('kathmandu_time')  # Extract Kathmandu time

#             # Store the received data in the DustbinData model
#             DustbinData.objects.create(distance=distance, status=status, kathmandu_time=kathmandu_time)

#             return JsonResponse({'message': 'Data received and processed successfully'})
#         except json.JSONDecodeError as e:
#             return JsonResponse({'error': 'Invalid JSON format'})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})


# def dashboard(request):
#     # Retrieve the latest DustbinData instance
#     latest_data = DustbinData.objects.latest('timestamp')
#     context = {
#         'distance': latest_data.distance,
#         'status': latest_data.status,
#         'kathmandu_time': latest_data.kathmandu_time  # Pass Kathmandu time to context
#     }
#     return render(request, "myApp/dashboard.html", context)

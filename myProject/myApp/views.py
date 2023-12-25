from django.shortcuts import render,redirect
from django.contrib import messages
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


# # Inside views.py of your Django app

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt  # Disables CSRF protection for this view (for simplicity, ensure this is secure in production)
# def receive_data_from_esp32(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             fill_percentage = data.get('full', 0)
#             status = data.get('status', 'Unknown')
            
#             # Process the received data as needed (e.g., store it in a database)
#             # Perform actions based on the fill percentage and status
            
#             return JsonResponse({'message': 'Data received successfully'})
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON format in request'}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt  # Use only during development for simplicity. Proper CSRF handling should be implemented.
# def esp32_data_handler(request):
#     if request.method == 'POST':
#         status = request.POST.get('status')  # Extract 'status' sent by the ESP32
#         # Process 'status' data received from ESP32
        
#         # Perform actions based on the 'status' (e.g., save to database, trigger events, etc.)
        
#         return JsonResponse({'message': 'Data received successfully'})  # Return a JSON response

#     return JsonResponse({'error': 'Invalid request method'}, status=400)

from django.http import JsonResponse
import json
@csrf_exempt
def esp32_data_handler(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            status = data.get('status')  # Extract 'status' sent by the ESP32
            distance = data.get('distance')  # Extract 'distance' sent by the ESP32
            
            # Process 'status' and 'distance' data received from ESP32
            # Perform actions based on the received data (e.g., save to database, trigger events, etc.)
            
            return JsonResponse({'message': 'Data received successfully'})  # Return a JSON response
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



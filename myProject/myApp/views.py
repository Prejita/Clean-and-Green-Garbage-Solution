from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import DustbinData  # Import the DustbinData model
from .models import Notification
from django.contrib.auth.decorators import login_required

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

@login_required
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

def addevents(request):
    context = {}
    return render(request, "myApp/addevents.html", context)

# @csrf_exempt
# def dustbin_data_receiver(request):
#     if request.method == 'POST':
#         try:
#             received_data = json.loads(request.body)
#             distance = received_data.get('distance')
#             status = received_data.get('status')

#             # Store the received data in the DustbinData model
#             DustbinData.objects.create(distance=distance, status=status)

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
#         'status': latest_data.status
#     }
#     return render(request, "myApp/dashboard.html", context)

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

@csrf_exempt
def dustbin_data_receiver(request):
    if request.method == 'POST':
        try:
            received_data = json.loads(request.body)
            distance = received_data.get('distance')
            status = received_data.get('status')
            kathmandu_time = received_data.get('kathmandu_time')  # Extract Kathmandu time
            location = received_data.get('location')  # Extract location data

            # Store the received data in the DustbinData model
            DustbinData.objects.create(distance=distance, status=status, kathmandu_time=kathmandu_time, location=location)

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
        'status': latest_data.status,
        'kathmandu_time': latest_data.kathmandu_time,  # Pass Kathmandu time to context
        'location': latest_data.location
    }
    return render(request, "myApp/dashboard.html", context)

def notifications(request):
    notification = Notification.objects.all()
    return render(request, 'myApp/notifications.html', {'notifications': notification})

@csrf_exempt
def delete_notification(request, notification_id):
    if request.method == 'POST':
        try:
            notification = Notification.objects.get(id=notification_id)
            notification.delete()
            return JsonResponse({'message': 'Notification deleted successfully'})
        except Notification.DoesNotExist:
            return JsonResponse({'error': 'Notification does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
def delete_all_notifications(request):
    if request.method == 'DELETE':
        try:
            # Delete all records from the Notification model
            Notification.objects.all().delete()
            return JsonResponse({'message': 'All notifications deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
# @csrf_exempt 
# def delete_notification(request):
#     if request.method == 'POST':
#         notification_id = request.POST.get('notification_id')
        
#         try:
#             # Perform deletion based on the notification ID
#             notification = Notification.objects.get(id=notification_id)
#             notification.delete()
#             return JsonResponse({'message': f'Notification ID {notification_id} deleted successfully'})
#         except Notification.DoesNotExist:
#             return JsonResponse({'error': 'Notification does not exist'}, status=404)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
    
#     return JsonResponse({'error': 'Invalid request'})
    
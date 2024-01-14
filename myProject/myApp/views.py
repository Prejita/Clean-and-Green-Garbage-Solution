from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import DustbinData  # Import the DustbinData model
from .models import Notification
from .models import Event
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone

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

def events(request):
    context = {}
    return render(request, "myApp/events.html", context)

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
    

def create_event(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        event_data = json.loads(request.body)
        
        # Create a new Event object
        new_event = Event(
            name=event_data['name'],
            organizer=event_data['organizer'],
            start_date=event_data['start_date'],
            end_date=event_data['end_date'],
            start_time=event_data['start_time'],  
            end_time=event_data['end_time'],
            location=event_data['location'],
            category=event_data['category'],
            description=event_data['description']
        )

        # Save the new event to the database
        new_event.save()

        return JsonResponse({'message': 'Event added successfully'}, status=201)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
    
def notify(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)

        # Convert the timestamp to the desired time zone (Asia/Kathmandu)
        timestamp_in_kathmandu_timezone = notification.timestamp.astimezone(timezone.get_current_timezone())

        # Format the timestamp in 12-hour format with AM/PM and show only the hour and minute
        formatted_time = timestamp_in_kathmandu_timezone.strftime('%I:%M %p')

        # Prepare email content with datetime information
        subject = 'FULL ALERT!'
        message = f'Alert! Dustbin 1 is full at {notification.location} on {formatted_time}.'

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['prejita14@gmail.com']

        send_mail(subject, message, from_email, recipient_list)

        messages.success(request, 'Email sent successfully!')
    
    except Exception as e:
        messages.error(request, 'Error sending email!')
    
    return redirect('notifications')


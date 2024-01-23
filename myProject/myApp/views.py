from email.message import EmailMessage
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import DustbinData 
from .models import Notification
from .models import Event
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from .models import Registration
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.decorators.http import require_POST


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

def register(request):
    event_name = request.GET.get('event', '')
    context = {'event_name': event_name}
    return render(request, "myApp/register.html", context)

def userrequest(request):
    registrations = Registration.objects.all()
    context = {'registrations': registrations}
    return render(request, 'myApp/userrequest.html', context)

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

# @csrf_exempt
# def delete_notification(request, notification_id):
#     if request.method == 'POST':
#         try:
#             notification = Notification.objects.get(id=notification_id)
#             notification.delete()
#             return JsonResponse({'message': 'Notification deleted successfully'})
#         except Notification.DoesNotExist:
#             return JsonResponse({'error': 'Notification does not exist'}, status=404)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=400)
    
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

def get_events(request):
    if request.method == 'GET':
        # Retrieve all events from the Event model
        events = Event.objects.all().values()

        # Convert QuerySet to list for serialization
        events_list = list(events)

        # Return events data in JSON format
        return JsonResponse(events_list, safe=False)

    # If the request method is not GET
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def submit_registration(request):
    if request.method == 'POST':
        # Extract data from the submitted form
        event_name = request.POST.get('eventName')
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        additional_info = request.POST.get('additionalInfo')

        # Save the registration data to the database (assuming you have a Registration model)
        Registration.objects.create(
            event_name=event_name,
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            additional_info=additional_info
        )

        # Optionally, you can add a success message
        messages.success(request, 'Registration submitted successfully.')

        # Redirect to a success page 
        return redirect('events') 
    
    # Handle cases where the form submission method is not POST
    return redirect('events')  

def clear_all_requests(request):
    try:
        # Delete all records from the Registration model
        Registration.objects.all().delete()
        return JsonResponse({'success': True, 'message': 'All requests cleared successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt  
def delete_registration(request):
    if request.method == 'POST':
        registration_id = request.POST.get('registration_id', '')
        try:
            registration = Registration.objects.get(id=registration_id)
            registration.delete()
            return JsonResponse({'message': 'Registration deleted successfully'})
        except Registration.DoesNotExist:
            return JsonResponse({'error': 'Registration does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def accept_registration(request):
    if request.method == 'POST':
        registration_id = request.POST.get('registration_id', '')

        try:
            # Get the registration record from the database
            registration = get_object_or_404(Registration, id=registration_id)

            # Mark the registration as accepted 
            registration.accepted = True
            registration.save()

            # Send acceptance email
            send_acceptance_email(registration)

            # Delete the registration from the database
            registration.delete()

            return JsonResponse({'message': 'Registration accepted successfully'})
        except Registration.DoesNotExist:
            return JsonResponse({'error': 'Registration does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def generate_invitation_pdf(username, eventname, event_start_date, event_start_time, event_location):
    # Create a BytesIO buffer to store the PDF content
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=(595.2755906, 841.8897638))  # A4 size in points

    # Set font
    p.setFont("Helvetica", 12)

    # Add content to the PDF
    p.drawString(50, 750, f"Dear {username},")
    p.drawString(50, 720, f"You are cordially invited to attend the event:")
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, 700, f"{eventname}")
    p.setFont("Helvetica", 12)
    p.drawString(50, 670, f"Date: {event_start_date}")
    p.drawString(50, 650, f"Time: {event_start_time}")
    p.drawString(50, 630, f"Location: {event_location}")

    p.drawString(50, 600, "We look forward to your participation.")
    p.drawString(50, 550, "Best regards,")
    p.drawString(50, 530, "GreenEase Team")

    # Close the PDF object cleanly
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer
    pdf_content = buffer.getvalue()
    buffer.close()

    return pdf_content

def send_acceptance_email(registration):
    # Compose the subject for the email
    subject = f'Registration Accepted for Event: {registration.event_name}'

    context = {
        'username': registration.full_name,
        'eventname': registration.event_name,
    }

    message = render_to_string('myApp/acceptance_email_body.txt', context)

    # Retrieve the event details
    event = get_object_or_404(Event, name=registration.event_name)

    # Generate the PDF content with event details
    pdf_content = generate_invitation_pdf(
        registration.full_name,
        registration.event_name,
        event.start_date,
        event.start_time,
        event.location
    )

    # Attach the PDF to the email
    pdf_filename = f'Invitation to {registration.event_name}.pdf'
    email = EmailMessage(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [registration.email],
    )
    email.attach(pdf_filename, pdf_content, 'application/pdf')

    # Send the email
    email.send()

@csrf_exempt
def decline_registration(request):
    if request.method == 'POST':
        registration_id = request.POST.get('registration_id', '')

        try:
            # Get the registration record from the database
            registration = get_object_or_404(Registration, id=registration_id)

            # Mark the registration as declined
            registration.accepted = False
            registration.save()

            # Send decline email
            send_decline_email(registration)

            # Delete the registration from the database
            registration.delete()

            return JsonResponse({'message': 'Registration declined successfully'})
        except Registration.DoesNotExist:
            return JsonResponse({'error': 'Registration does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def send_decline_email(registration):
    # Compose the subject for the email
    subject = f'Registration Declined for Event: {registration.event_name}'

    context = {
        'username': registration.full_name,
        'eventname': registration.event_name,
    }

    message = render_to_string('myApp/decline_email_body.txt', context)

    # Create an EmailMessage object
    email = EmailMessage(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [registration.email],
    )

    # Send the email
    email.send()

@csrf_exempt  
@require_POST
def delete_selected_notifications(request):
    try:
        data = json.loads(request.body)
        selected_notification_ids = data.get('selectedNotificationIds', [])

        # Perform deletion in the database
        Notification.objects.filter(id__in=selected_notification_ids).delete()

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
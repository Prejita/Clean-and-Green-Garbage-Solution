from email.message import EmailMessage
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import DustbinData 
from .models import Notification
from .models import Event
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import timezone
from .models import Registration, AcceptedRegistration,DeclinedRegistration
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

def blog_post5(request):
    context = {}
    return render(request, "myApp/blog-post-5.html", context)

def blog_post6(request):
    context = {}
    return render(request, "myApp/blog-post-6.html", context)

def blog_post7(request):
    context = {}
    return render(request, "myApp/blog-post-7.html", context)

def blog_post8(request):
    context = {}
    return render(request, "myApp/blog-post-8.html", context)

def blog(request):
    context = {}
    return render(request, "myApp/blog.html", context)

def blog2(request):
    context = {}
    return render(request, "myApp/blog2.html", context)

def contact(request):
    context = {}
    return render(request, "myApp/contact.html", context)

@login_required
def dashboard(request):
    messages_data = messages.get_messages(request)
    context = {'messages_data': messages_data}
    return render(request, "myApp/dashboard.html", context)

def termsandconditions(request):
    context = {}
    return render(request, "myApp/terms-and-conditions.html", context)

@staff_member_required
@login_required
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

def eventlist(request):
    context = {}
    return render(request, "myApp/eventlist.html", context)

def editevent(request):
    context = {}
    return render(request, "myApp/editevent.html", context)

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
   
# def create_event(request):
#     if request.method == 'POST':
#         # Retrieve data from the POST request
#         event_data = json.loads(request.body)
        
#         # Create a new Event object
#         new_event = Event(
#             name=event_data['name'],
#             organizer=event_data['organizer'],
#             start_date=event_data['start_date'],
#             end_date=event_data['end_date'],
#             start_time=event_data['start_time'],  
#             end_time=event_data['end_time'],
#             location=event_data['location'],
#             # latitude = event_data['latitude'],
#             # longitude = event_data['longitude'],
#             category=event_data['category'],
#             description=event_data['description']
#         )

#         # Save the new event to the database
#         new_event.save()

#         return JsonResponse({'message': 'Event added successfully'}, status=201)
#     else:
#         return JsonResponse({'message': 'Invalid request method'}, status=400)
def create_event(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        event_data = json.loads(request.body)
        
        # Check if an event with the same name already exists
        if Event.objects.filter(name=event_data['name']).exists():
            # Show a SweetAlert informing the user about the existing event
            return JsonResponse({'message': 'An event with this name already exists'}, status=400)

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

@csrf_exempt
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

        # Delete the notification after sending the email
        notification.delete()

        # Send success response
        return JsonResponse({'success': True, 'message': 'Email sent successfully!'})

    except Exception as e:
        # Send error response
        return JsonResponse({'success': False, 'error': str(e)})

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

csrf_exempt
def submit_registration(request):
    if request.method == 'POST':
        # Extract data from the submitted form
        event_name = request.POST.get('eventName')
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        additional_info = request.POST.get('additionalInfo')

        if request.method == 'POST':
            # Get form data
            event_name = request.POST.get('eventName')
            full_name = request.POST.get('fullName')
            email = request.POST.get('email')

            # Check if a registration already exists for this user and event
            existing_registration = Registration.objects.filter(event_name=event_name, full_name=full_name, email=email).exists()
            
            if existing_registration:
                # Return error response indicating duplicate registration
                return JsonResponse({'error': 'You have already registered for this event'}, status=400)

            # Save the registration data to the database (assuming you have a Registration model)
            Registration.objects.create(
                event_name=event_name,
                full_name=full_name,
                email=email,
                phone=phone,
                address=address,
                additional_info=additional_info
            )

            # Return a JSON response indicating success
            return JsonResponse({'success': True})

    # Handle cases where the form submission method is not POST
    return redirect('events')

@csrf_exempt 
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

            # Create a record in the AcceptedRegistration model
            accepted_registration = AcceptedRegistration.objects.create(
                event_name=registration.event_name,
                full_name=registration.full_name,
                email=registration.email,
                phone=registration.phone,
                address=registration.address,
                additional_info=registration.additional_info
            )

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

            # Create a record in the DeclinedRegistration model
            declined_registration = DeclinedRegistration.objects.create(
                event_name=registration.event_name,
                full_name=registration.full_name,
                email=registration.email,
                phone=registration.phone,
                address=registration.address,
                additional_info=registration.additional_info
                # Add any other fields you need
            )

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

@csrf_exempt     
@require_POST
def delete_events(request):
    try:
        # Assuming your request data is JSON with a list of event IDs
        data = json.loads(request.body.decode('utf-8'))
        event_ids = data.get('eventIds', [])

        # Perform the deletion in your database
        Event.objects.filter(id__in=event_ids).delete()

        # Return a success response
        response_data = {'success': True}
    except Exception as e:
        # Handle errors and return an error response
        print(f'Error deleting events: {e}')
        response_data = {'success': False}

    return JsonResponse(response_data)

def get_event_details(request, event_id):
    try:
        # Fetch the event details based on the provided event ID
        event = Event.objects.get(pk=event_id)

        # Serialize event details to a dictionary
        serialized_event = {
            'id': event.id,
            'name': event.name,
            'organizer': event.organizer,
            'start_date': str(event.start_date),
            'end_date': str(event.end_date),
            'start_time': event.start_time,
            'end_time': event.end_time,
            'location': event.location,
            'category': event.category,
            'description': event.description,
        }

        return JsonResponse(serialized_event)
    except Event.DoesNotExist:
        # Return a JSON response indicating that the event was not found
        return JsonResponse({'error': 'Event not found'}, status=404)

# @csrf_exempt  
# def edit_event(request):
#     if request.method == 'POST':
#         # Retrieve form data from POST request
#         event_id = request.POST.get('eventId')
#         event_name = request.POST.get('eventName')
#         event_organizer = request.POST.get('eventOrganizer')
#         event_start_date = request.POST.get('eventStartDate')
#         event_start_time = request.POST.get('eventStartTime')
#         event_end_date = request.POST.get('eventEndDate')
#         event_end_time = request.POST.get('eventEndTime')
#         event_location = request.POST.get('eventLocation')
#         # event_latitude = request.POST.get('latitude')
#         # event_longitude = request.POST.get('longitude')
#         event_category = request.POST.get('eventCategory')
#         event_description = request.POST.get('eventDescription')

#         # Get the existing event from the database
#         existing_event = Event.objects.get(id=event_id)

#         # Update the event with the new data
#         existing_event.name = event_name
#         existing_event.organizer = event_organizer
#         existing_event.start_date = event_start_date
#         existing_event.start_time = event_start_time
#         existing_event.end_date = event_end_date
#         existing_event.end_time = event_end_time
#         existing_event.location = event_location
#         existing_event.category = event_category
#         existing_event.description = event_description

#         # Save the updated event
#         existing_event.save()

#         # Return a JsonResponse indicating success
#         return JsonResponse({'success': True})

#     # Handle cases where the form is not submitted via POST
#     return JsonResponse({'success': False, 'error': 'Invalid request method'})
@csrf_exempt
def edit_event(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        event_id = request.POST.get('eventId')
        event_name = request.POST.get('eventName')

        # Check if the event name already exists (excluding the current event being edited)
        existing_events = Event.objects.exclude(id=event_id).filter(name=event_name)

        if existing_events.exists():
            # If an event with the same name exists, return an error response
            return JsonResponse({'success': False, 'error': 'Event name already exists'})

        # Proceed with updating the event
        event_organizer = request.POST.get('eventOrganizer')
        event_start_date = request.POST.get('eventStartDate')
        event_start_time = request.POST.get('eventStartTime')
        event_end_date = request.POST.get('eventEndDate')
        event_end_time = request.POST.get('eventEndTime')
        event_location = request.POST.get('eventLocation')
        event_category = request.POST.get('eventCategory')
        event_description = request.POST.get('eventDescription')

        # Get the existing event from the database
        existing_event = Event.objects.get(id=event_id)

        # Update the event with the new data
        existing_event.name = event_name
        existing_event.organizer = event_organizer
        existing_event.start_date = event_start_date
        existing_event.start_time = event_start_time
        existing_event.end_date = event_end_date
        existing_event.end_time = event_end_time
        existing_event.location = event_location
        existing_event.category = event_category
        existing_event.description = event_description

        # Save the updated event
        existing_event.save()

        # Return a JsonResponse indicating success
        return JsonResponse({'success': True})

    # Handle cases where the form is not submitted via POST
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def get_notification_count(request):
    notification_count = Notification.objects.count()

    return JsonResponse({'count': notification_count})

def get_total_user_count(request):
    total_users = Registration.objects.count()
    return JsonResponse({'total_users': total_users})

@csrf_exempt
def donate(request):
    if request.method == 'POST':
        print("call")
        data = json.loads(request.body)
        payment_token = data.get('payment_token')
        payment_amount = data.get('payment_amount')
        event_name = data.get('event_name') 
        print(payment_token, payment_amount,event_name)

        khalti_secret_key = "test_secret_key_cf0998dea28f4789ba00f302c09d3b21"
        verification_url = "https://khalti.com/api/v2/payment/verify/"
        headers = {
            'Authorization': f'key {khalti_secret_key}',
        }
        payload = {
            'token': payment_token,
            'amount': payment_amount,
        }
        print("success")
        response = requests.post(verification_url, headers=headers, json=payload)

        messages.success(request,'Donation Successful')
        print('hello')
        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
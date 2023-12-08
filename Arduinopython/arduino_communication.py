# import serial
# import requests
# from bs4 import BeautifulSoup

# # Define the Arduino's serial port and baud rate
# arduino_port = 'COM6'
# arduino_baudrate = 9600
# django_api_url = 'http://127.0.0.1:8000/handle_arduino_data/'

# # Open a serial connection to the Arduino
# ser = serial.Serial(arduino_port, arduino_baudrate)

# while True:
#     try:
#         arduino_data = '65'
#         THRESHOLD_VALUE = 50
#         data_to_send = {
#             'fill_level': arduino_data,
#             'status': 'full' if int(arduino_data) >= THRESHOLD_VALUE else 'not full',
#             'location': 'Herald College Kathmandu'
#         }
#         # Fetch CSRF token from the Django server
#         response = requests.get(django_api_url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

#         # Include the CSRF token in the request headers
#         headers = {'X-CSRFToken': csrf_token}
#         response = requests.post(django_api_url, json=data_to_send, headers=headers)
#         print (response.status_code)
#         if response.status_code == 200:
#             print("Data sent successfully")
#         else:
#             print("Failed to send data to Django")
#     except Exception as e:
#         print("An error occurred:", str(e))

# # Close the serial connection when done
# response = requests.post(django_api_url, json=data_to_send, headers={'X-CSRFToken': csrf_token})
# ser.close()

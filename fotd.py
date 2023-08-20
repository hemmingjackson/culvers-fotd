import requests, os, sys
from bs4 import BeautifulSoup
from twilio.rest import Client

# URL template for Culver's flavor of the day
url_template = 'https://www.culvers.com/restaurants/{}'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3' }

# Twilio credentials pulled from system environment variables
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
RECEIVER_NUMBER = os.environ.get('RECEIVER_NUMBER')

def get_fotd(city):
    # Construct the URL for the city's Culver's page
    url = url_template.format(city)
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Error: Unable to retrieve data for {city}. Status code: {response.status_code}')
        sys.exit(1)

    if response.url == 'https://www.culvers.com/flavor-of-the-day':
        print(f'Invalid store entered. Try searching at https://www.culvers.com/flavor-of-the-day')
        sys.exit(1)

    # Parse HTML content and extract flavor of the day
    soup = BeautifulSoup(response.content, 'html.parser')
    fotd = soup.strong.string
    return f'Today\'s flavor of the day at {city} is {fotd}!'

def send_sms(message):
    # Initialize Twilio client with credentials
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        # Send SMS message using Twilio
        message = client.messages.create(
            from_=TWILIO_NUMBER,
            body=message,
            to=RECEIVER_NUMBER
        )
        print('SMS sent successfully:', message.sid)
    except Exception as e:
        print('Error sending SMS:', str(e))


if __name__ == '__main__':
    # Check if the script is given the correct number of arguments
    if len(sys.argv) != 2:
        print('Usage: python fotd.py <city>')
        sys.exit(1)

    # Get the city name from the command-line argument
    city = sys.argv[1]

    # Get flavor of the day message and send SMS 
    message = get_fotd(city)
    send_sms(message)
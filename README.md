# culvers-fotd
- A simple web scraping program to find the Flavor of the Day at Culver's Restaurant and send it via SMS

## Installation
- Requires installation of BeatifulSoup library

Windows
```shell
pip install -r requirements.txt
setx TWILIO_ACCOUNT_SID "your_account_sid"
setx TWILIO_AUTH_TOKEN "your_auth_token"
setx TWILIO_NUMBER "your_twilio_phone_number"
setx RECEIVER_NUMBER "recipient_phone_number"
python fotd.py "city_name"
```

### TODO
Schedule SMS notification to go out daily/weekly/etc.
Add support for multiple devices to receive SMS.

# culvers-fotd
- A simple web scraping program to find the Flavor of the Day at Culver's Restaurant 

## Installation
- Requires installation of BeatifulSoup library

```shell
pip install BeautifulSoup twilio
setx TWILIO_ACCOUNT_SID "your_account_sid"
setx TWILIO_AUTH_TOKEN "your_auth_token"
setx TWILIO_NUMBER "your_twilio_phone_number"
setx RECEIVER_NUMBER "recipient_phone_number"
python fotd.py "city_name"
```

### TODO
Add ability for sending fotd via email/SMS

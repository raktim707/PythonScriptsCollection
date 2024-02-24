import os
import smtplib
from binance.client import Client

# Binance API credentials
api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_API_SECRET')

# Email credentials
email_address = os.environ.get('EMAIL_ADDRESS')
email_password = os.environ.get('EMAIL_PASSWORD')
recipient_email = os.environ.get('RECIPIENT_EMAIL')

# Cryptocurrency to monitor and threshold price
symbol = 'BTCUSDT'
threshold_price = 50000.0

def check_price():
    client = Client(api_key, api_secret)
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        price = float(ticker['price'])
        return price
    except Exception as e:
        print("Error:", e)
        return None

def send_email(subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(email_address, recipient_email, message)
        print("Email notification sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
    finally:
        server.quit()

if __name__ == "__main__":
    current_price = check_price()
    if current_price is not None:
        print(f"The current price of {symbol} is ${current_price:.2f}")
        if current_price > threshold_price:
            subject = f"Price Alert: {symbol} exceeds {threshold_price}"
            body = f"The current price of {symbol} is ${current_price:.2f}, which exceeds the threshold of ${threshold_price}."
            send_email(subject, body)

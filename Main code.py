import requests
import smtplib
from datetime import date
import datetime
import credentials

my_email = credentials.email
password = credentials.password
topic = "Delhi"
date_end = date.today()
date_start = date_end - datetime.timedelta(days=1)
api_key = credentials.api
# More parameters in de newsapi documentation
url = "https://newsapi.org/v2/everything?excludeDomains=removed.com&"\
      f"q={topic}&" \
      f"from={date_start}&"\
      f"to={date_end}&sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "ee26a25870b74596acec352dab18a49d&language=en"

# Make request
request = requests.get(url)
content = request.json()
#list of email addresses
recipients = ["recipient1@gmail.com", "recipient2@gmail.com"]


body = "Subject: News for You\n\n" #This will be the subject of our email
#This will be the body of our email
for article in content["articles"][:5]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
                   + article["description"] + "\n" + article["url"] + 2*"\n"
body = body.encode("utf-8")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    connection.login(user=my_email, password=password)
    for recipient in recipients: #iterate over all the recipients
        connection.sendmail(from_addr=my_email,
                           to_addrs=recipient,
                           msg=body)
    print("Emails sent successfully")

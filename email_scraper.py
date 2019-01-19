import re
from datetime import datetime

from bs4 import BeautifulSoup


def scrape(message_id, mime_msg):
    soup = None
    if mime_msg.is_multipart():
        for p in mime_msg.get_payload():
            if '<html>' in str(p):
                soup = BeautifulSoup(p.get_payload(decode=True), 'html.parser')
    else:
        soup = BeautifulSoup(mime_msg.get_payload(decode=True), 'html.parser')

    monies = map(lambda s: float(re.search(r'£\d+\.\d+', s).group(0)[1:]), soup.find_all(string=re.compile(r'£\d+\.\d+')))

    if len(list(monies)) < 1:
        print("No prices found")
        return

    money = max(monies)

    time = datetime.strptime(mime_msg['date'], '%a, %d %b %Y %H:%M:%S %z')

    subject = mime_msg['subject']

    email_link = "https://mail.google.com/mail/#inbox/{}".format(message_id)

    return -money, time, subject, email_link

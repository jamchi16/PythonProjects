import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()
content = ''

def extract_news(url):
    print('Extracting PokeBeach Stories...')
    cnt = ''
    cnt += ('<b>PokeBeach Current Stories:</b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('h2', attrs={'entry-title count-'})):
        cnt += (str(i + 1) + ' :: ' + '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>')
    return (cnt)


cnt = extract_news('https://www.pokebeach.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')
print('Composing Email...')
SERVER = 'smtp.gmail.com'
PORT = 587  # your port number
FROM = '*****@gmail.com'
TO = '*****@gmail.com'
appsPASS = '*****'
msg = MIMEMultipart()
msg['Subject'] = 'Current News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))
print('Initiating Server...')
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, appsPASS)
server.sendmail(FROM, TO, msg.as_string())
print('Email Sent...')
server.quit()
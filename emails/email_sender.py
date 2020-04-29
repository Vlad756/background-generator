import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Chaselane'
email['to'] = 'V.chelyadin2015@yandex.ru'
email['subject'] = 'You won 1,000,000 dollars!'

# email.set_content('I am a Pysthon Master!')
email.set_content(html.substitute({'name': 'Vlad'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('homerjayisgay@gmail.com', 'Vlad756166vlad')
    smtp.send_message(email)
    print('all good boss!')

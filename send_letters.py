from email.utils import formatdate

import openpyxl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

df = openpyxl.load_workbook('new_people.xlsx')
ws = df.active

# SERVER = "smtp.example.com"
EMAIL_HOST = ''
EMAIL_PORT = 

FROM = ""

SUBJECT = ""

server = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)

path_to_pdf = 'test.pdf'

with open(path_to_pdf, "rb") as f:
    attach = MIMEApplication(f.read(), _subtype="pdf")

attach.add_header('Content-Disposition', 'attachment',
                  filename='test.pdf')

for row in ws:
    msg = MIMEMultipart()
    TEXT = f"""

    """

    msg['From'] = FROM
    msg['To'] = row[1].value
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(TEXT))

    msg.attach(attach)

    server.sendmail(FROM, row[1].value, msg.as_string())

server.quit()

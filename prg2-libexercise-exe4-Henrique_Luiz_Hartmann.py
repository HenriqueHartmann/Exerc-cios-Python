# By: Henrique Luiz Hartmann BSI2
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import smtplib
import subprocess

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('joaosilvapires3@gmail.com', 'SenhaGmail_5@')
mail.list()
# Out: list of "folders" aka labels in gmail.
# connect to inbox.
mail.select("inbox")

result, data = mail.search(None, "ALL")
# data is a list.
ids = data[0]
# ids is a space separated string
id_list = ids.split()

# result of the command
finishResult = ''

# goes through all the ids
for id in id_list:
    result, data = mail.fetch(id, "(RFC822)")
    content = data[0][1].decode('utf-8')
    # verify if the key-word is found in the emails
    if 'Execute comando aula' in content:
        # starts the process of executing the command
        result = []
        process = subprocess.Popen('dir c:',
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        # prepare the encode of the result
        for line in process.stdout:
            result.append(line)
        errcode = process.returncode
        for line in result:
            string = line.decode('cp850')
            finishResult += string

# starts emailing process
# create message object instance
msg = MIMEMultipart()

# setup the parameters of the message
password = "SenhaGmail_5@"
msg['From'] = "joaosilvapires3@gmail.com"
msg['To'] = "joaosilvapires3@gmail.com"
msg['Subject'] = "TESTE PROGRAMA"

# add in the message body
msg.attach(MIMEText(finishResult, 'plain'))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send(_from=r'ietarmailtest@163.com',\
         password=r'test1234',\
         to=r'410473517@qq.com',\
         message=r'nothing',\
         title=r'来自smtp的问候......',\
         yourname=r'anonymous',\
         addressee=r'hello?',\
         debuglv=0):
    '''directly send an email'''

    if not isinstance(debuglv, int):
        raise ValueError('debuglv should be 0 or 1')

    smtp_server = r'smtp.' + _from.split(r'@')[1]

    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = _format_addr('{} <{}>'.format(yourname,_from))
    msg['to'] = _format_addr('{} <{}>'.format(addressee,to))
    msg['Subject'] = Header(title, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(debuglv)
    server.login(_from, password)
    server.sendmail(_from, [to], msg.as_string())
    server.quit()

if __name__ == '__main__':
    send()

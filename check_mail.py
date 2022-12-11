import imap_tools.errors
from imap_tools import MailBox
import imaplib
from bs4 import BeautifulSoup

providers = {
    "imap.rambler.ru": [
        'rambler.ru',
        'lenta.ru',
        'autorambler.ru',
        'myrambler.ru',
        'ro.ru',
        'rambler.ua'],
    "imap.mail.ru": ['mail.ru', 'internet.ru', 'bk.ru', 'inbox.ru', 'list.ru'],
    "imap.gmail.com": 'gmail.com',
    "imap.yandex.ru": 'yandex.ru'
}


def get_provider(mails: str):
    pr = mails.split("@")[-1]
    for key, value in providers.items():
        if pr in value:
            return key
    return f"imap.{pr}"


def check_mail1(mail, psw, _from):
    provider = get_provider(mail)
    page = None
    try:
        with MailBox(provider).login(mail, psw) as mailbox:
            for msg in mailbox.fetch():
                if msg.from_ == _from:
                    print(msg.html)
                    page = msg.html
            if page is None:
                with MailBox(provider).login(mail, psw, 'Spam') as mailboxs:
                    for msgs in mailboxs.fetch():
                        if msgs.from_ == _from:
                            page = msgs.html
            if page is None:
                print('Письмо ненайдено')
                return
    except:
        print('Ошибка логина\n')
        return 0

    soup = BeautifulSoup(page, 'lxml')
    raws = soup.findAll('a')
    ref_link = []
    for raw in raws:
        link = raw.get('href')
        ref_link.append(link)
    return ref_link


if __name__ == '__main__':
    print('Hello world')


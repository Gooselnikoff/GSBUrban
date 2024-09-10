# Онлайн-университет URBAN
# Домашняя работа по уроку "Способы вызова функции"

def chekc_email(email):
    email_ok = False
    if "@" in email:
        if email.endswith(".com") \
        or email.endswith(".ru") \
        or email.endswith(".net"):
            email_ok = True
    return email_ok

def send_email(message, recipient, sender="university.help@gmail.com"):
    if chekc_email(sender) and chekc_email(recipient):
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        else:
            if sender == "university.help@gmail.com":
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Пожалуйста, исправьте задание', 'urban.studentmail.ru', sender='urban.teacher@mail.uk')

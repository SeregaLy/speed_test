# Очень важно сгенерировать пароль приложения Google для своей учетной записи
# Gmail, так как вы будете отправлять автоматические электронные письма с
# использованием Python через свою учетную запись Gmail. После того, как вы
# сгенерировали пароль для своего приложения Google, вот как вы можете
# приступить к отправке электронных писем с помощью Python:
# В приведенном выше коде я определил функцию Python, которая будет
# автоматически отправлять электронные письма только что зарегистрированному
# пользователю. Эта функция запустится с запроса имени пользователя и адреса
# электронной почты. Тогда имя пользователя будет сохранено в сообщении. Затем
# в 12-й строке кода выше вам нужно заменить первый параметр на ваш адрес
# электронной почты, а второй параметр на пароль приложения Google, который вы
# создали ранее.  После этого просто запустите приведенный выше код, и вы
# увидите вывод, как показано ниже.


import os
import random
import smtplib


def automatic_email():
    user = input("Введите ваше имя >>: ")
    email = input("Введите свой адрес электронной почты >>: ")
    message = (f"Dear {user}, Welcome to Thecleverprogrammer")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail Account", "Your App Password")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Письмо отправлено!")


automatic_email()

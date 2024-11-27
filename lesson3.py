import os
import smtplib
from dotenv import load_dotenv
load_dotenv()
login = os.getenv('login')
password = os.getenv('password')
website = 'https://dvmn.org/profession-ref-program/akhmanaev90/uKrPL/'
friend_name = 'Кирилл'
my_name = 'Егор'
mail = '''Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub.Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
'''.format(friend_name=friend_name, my_name=my_name, website=website)
letter = '''From: {email_from}
To: akhmanaev90@mail.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

{mail}'''.format(mail=mail, email_from=login)
letter = letter.encode("UTF-8")

email_from = login
email_to = 'akhmanaev90@mail.ru'
message = letter

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()


# В приведенном коде:

# Сначала я определил функцию Python, в которой я запрашиваю три
# пользовательских ввода:
# г: год рождения
# м: месяц рождения
# д: дата рождения
# Затем я импортирую модуль datetime в Python внутри функции
# Затем в следующей строке я беру сегодняшнюю дату, используя метод
# datetime.now() модуля datetime.
# Затем я ввел новую переменную в следующей строке как dob, где я использую
# дату рождения в качестве ввода, предоставленного пользователем.
# Затем я вычитаю дату с сегодняшней датой, а затем делю ее на 365,25, что
# возвращает возраст пользователя.


def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365.25)
    print(age)


ageCalculator(1998, 9, 3)

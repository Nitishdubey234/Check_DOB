from datetime import date
today=date.today()
birth=date(2004,7,1)
age=today.year-birth.year
days=birth.strftime('%A')

name=input()
print('Person name is:',name)
print('Person date of births:',birth)
print('Person age is:',age)
print('person Birth of day is:',days)
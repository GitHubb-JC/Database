import datetime
import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

genre = Genre.objects.get(id=1)
genre.title = '액션'
genre.save()

## id 3 이 두번째 줄에 있어서 3을 불러와
# 2로 바꾸고 그 안에 드라마를 넣으려 했지만
# 아래 코드들을 실행하면 2가 드라마로 완전 새롭게 생성되고
# 3은 그대로 남아 있다.
genre = Genre.objects.get(id=3)
genre.id = 2
genre.title = '드라마'
genre.save()

genre = Genre.objects.get(id=3)
genre.title = '사극'
genre.save()

Genre.objects.create(title = '범죄')

Genre.objects.create(title = '스릴러')
Genre.objects.create(title = 'SF')
Genre.objects.create(title = '무협')
Genre.objects.create(title = '첩보')
Genre.objects.create(title = '재난')

director = Director.objects.all()
for director in director:
    print(director.name, end=' ')
    print(director.debut, end=' ')
    print(director.country)

director = Director.objects.get(country = 'USA')
print(director.name, end=' ')
print(director.debut, end=' ')
print(director.country)

director = Director.objects.filter(name = '봉준호')
print(director.debut, end=' ')
print(director.country)
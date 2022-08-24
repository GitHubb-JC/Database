import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 1. Artist 생성
import datetime 
artist = Artist() 
artist.name = '아이브'
# 2021년 12월 1일
artist.debut = datetime.date(2021, 12, 1)
artist.save()

artist = Artist() 
artist.name = '아이유'
artist.debut = '2019-12-26'
artist.save()

director = Director()
director.name = '봉준호'
director.debut = datetime.date(1993, 1, 1)
director.country = 'KOR'
director.save()

director = Director()
director.name = '김한민'
director.debut = '1993-01-01'
director.country = 'KOR'
director.save()

## 8. 
director = Director()
director.name = '최동훈'
director.debut = datetime.date(2004, 1, 1)
director.country = 'KOR'
director.save()

## 9. 
director = Director.objects.get(name = 'Joseph Kosinski')
director.country = 'USA'
director.save()

## 10.
director = Director.objects.get(country = 'KOR')

## 12.
director = Director.objects.filter(country = 'KOR')
for director in director:
    print(director.name, end=' ')
    print(director.debut, end=' ')
    print(director.country)

## 13.
director = Director.objects.get(name = '김철수')
director.delete()
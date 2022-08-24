import datetime
import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

director = Director()
director.name = '봉준호'
director.debut = datetime.date(1993, 1, 1)
director.country = 'KOR'
director.save()

director = Director()
director.id = 2
director.name = '김한민'
director.debut = '1993-01-01'
director.country = 'KOR'
director.save()

director = Director()
director.id = 3
director.name = '최동훈'
director.debut = datetime.date(2004, 1, 1)
director.country = 'KOR'
director.save()

director = Director()
director.id = 4
director.name = '이정재'
director.debut = datetime.date(2022, 1, 1)
director.country = 'KOR'
director.save()

director = Director()
director.id = 5
director.name = '이경규'
director.debut = datetime.date(1992, 1, 1)
director.country = 'KOR'
director.save()

director = Director()
director.id = 6
director.name = '한재림'
director.debut = datetime.date(2005, 1, 1)
director.country = 'KOR'
director.save()

director = Director()
director.id = 7
director.name = 'Joseph Kosinski'
director.debut = datetime.date(1999, 1, 1)
director.country = 'KOR'
director.save()

director = Director()
director.id = 8
director.name = '김철수'
director.debut = datetime.date(2022, 1, 1)
director.country = 'KOR'
director.save()

Director.objects.create(id = 9, name = '조창현', debut = datetime.date(1993, 11, 6), country = 'KOR')

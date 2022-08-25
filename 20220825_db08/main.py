from socket import TIPC_CLUSTER_SCOPE
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

# 1:N 관계에서의 Create

# 객체
# Class 정의를 genre로 했기 때문
album = Album()
album.name = '꽃'
# album.genre = 1
# ValueError: Cannot assign "1": "Album.genre" must be a "Genre" instance.       
genre = Genre.objects.get(id=1)
album.genre = genre
artist = Artist.objects.get(id=1)    
album.artist = artist
album.save()

# 값
# 테이블에 실제 필드는 _id가 붙어있기 때문
album = Album()
album.genre_id = 1
album.artist_id = 1
album.name = '미아'
album.save()

# N => 1 (참조)
# 앨범의 id가 1인 것의
album = Album.objects.get(id=1) # 앨범 객체
# 장르의 이름은..?
album.genre # 장르 객체
# <Genre: Genre object (1)>
album.genre.name
# '발라드'


# 1 => N (역참조)
# 클래스이름_set
# id가 1인 장르의 모든 앨범은?
g1 = Genre.objects.get(id=1)
g1.album_set.all() 
# <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>



###############################################################
#########                     #################################
#########   내 실습            #################################
#########                     #################################
###############################################################

## 3. #########################
directors = [
    ("봉준호","1993-01-01","KOR"),
    ("김한민","1999-01-01","KOR"),
    ("최동훈","2004-01-01","KOR"),
    ("이정재","2022-01-01","KOR"),
    ("이경규","1992-01-01","KOR"),
    ("한재림","2005-01-01","KOR"),
    ("Joseph Kosinski","1999-01-01","KOR"),
    ("김철수","2022-01-01","KOR")
]

for director in directors:
    name_ = director[0]
    debut_ = director[1]
    country_ = director[2]
    Director.objects.create(name = name_, debut = debut_, country = country_)

genres = ["액션","드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()

genres = [1,2,3,4,5,6,7,8,9]

for title_ in genres:
    genre = Genre()
    genre.id = title_
    genre.save()

genre = Genre.objects.get(id=1)
genre.delete()

genre = Genre.objects.get(id=11)
genre.id = 1
genre.save()

for i in range(11, 20):
    genre = Genre.objects.get(id=i)
    genre.delete()

genres = ["드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()

for i in range(20, 28):
    genre = Genre.objects.get(id=i)
    genre.delete()

genres = ["드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for i in range(2, 10):
    genre = Genre.objects.get(id=i)
    genre.title = genres[i - 2]
    genre.save()

genres = ["사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()

for i in range(29, 36):
    genre = Genre.objects.get(id=i)
    genre.id = i-26
    genre.save()

for i in range(29, 36):
    genre = Genre.objects.get(id=i)
    genre.delete()

genre = Genre.objects.get(id=28)
genre.delete()

## 4. #####################
director = Director.objects.get(id = 1)
print(f'id : {director.id}')
print(f'name : {director.name}')
print(f'debut : {director.debut}')
print(f'country : {director.country}')

## 5. #####################
genre = Genre.objects.get(title = '드라마')
print(f'id : {genre.id}')
print(f'title : {genre.title}')

## 6. #####################
director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

movie = Movie()

movie.director = director_
movie.genre = genre_
movie.title = '기생충'
movie.opening_date = datetime.date(2019, 5, 30)
movie.running_time = 132
movie.screening = False

movie.save()

movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for m in movies:
    director_ = Director.objects.get(name=m[0])
    genre_ = Genre.objects.get(title=m[1])
    title_ = m[2]
    opening_date_ = m[3]
    running_time_ = m[4]
    screening_ = m[5]

    movie = Movie()
    movie.director = director_
    movie.genre = genre_
    movie.title = title_
    movie.opening_date = opening_date_
    movie.running_time = running_time_
    movie.screening = screening_
    movie.save()


## 8. ################################
movie = Movie.objects.all()

for movie in movie:
    print(movie.director, end=' ')
    print(movie.genre, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)


## 9. #################################
movie = Movie.objects.all()

for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 10. #####################################
movie = Movie.objects.all()

for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 11. #################################
movie = Movie.objects.order_by('-opening_date')

for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 12. ##################################
movie = Movie.objects.order_by('opening_date')[0]

print(movie.director.name, end=' ')
print(movie.genre.title, end=' ')
print(movie.title, end=' ')
print(movie.opening_date, end=' ')
print(movie.running_time, end=' ')
print(movie.screening)

## 13. #################################
movie = Movie.objects.order_by('opening_date').filter(screening__contains=1)
for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 14. ##########################################
director_ = Director.objects.get(name='봉준호')
movie = Movie.objects.order_by('opening_date').filter(director=director_)
for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 15. ######################################
director_ = Director.objects.get(name='봉준호')
movie = Movie.objects.order_by('opening_date').filter(director=director_)[1]

print(movie.director.name, end=' ')
print(movie.genre.title, end=' ')
print(movie.title, end=' ')
print(movie.opening_date, end=' ')
print(movie.running_time, end=' ')
print(movie.screening)

## 16. #######################################
movie = Movie.objects.order_by('running_time').filter(running_time__gt=119)
for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 17. #########################################
movie = Movie.objects.order_by('running_time').filter(running_time__gte=119)
for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 18. ##########################################
movie = Movie.objects.order_by('opening_date').filter(opening_date__gte=datetime.date(2022, 1, 1))
for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 19. ############################################
director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title = '드라마')
movie = Movie.objects.order_by('opening_date').filter(director = director_, genre = genre_)
for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)

## 20. #########################################
director_ = Director.objects.get(name='봉준호')
movie = Movie.objects.order_by('opening_date').exclude(director = director_)
for movie in movie:
    print(movie.director.name, end=' ')
    print(movie.genre.title, end=' ')
    print(movie.title, end=' ')
    print(movie.opening_date, end=' ')
    print(movie.running_time, end=' ')
    print(movie.screening)
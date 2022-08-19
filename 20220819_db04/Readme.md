### 1. 모든 테이블의 이름을 출력하세요.
```sql
albums          employees       invoices        playlists   

artists         genres          media_types     tracks      

customers       invoice_items   playlist_track
```

### 2. 모든 테이블의 데이터를 확인해보세요.
| 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.

- ***노가다 말고 더 편한 방법은 없을까??***


### 3. 앨범(albums) 테이블의 데이터를 출력하세요.
| 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.

```sql
select * from albums
order by title
limit 5;

AlbumId  Title                                                         ArtistId      
-------  ------------------------------------------------------------  --------      
156      ...And Justice For All                                        50

257      20th Century Masters - The Millennium Collection: The Best o  179        
         f Scorpions

296      A Copland Celebration, Vol. I                                 230        

94       A Matter of Life and Death                                    90

95       A Real Dead One                                               90
```

### 4. 고객(customers) 테이블의 행 개수를 출력하세요.
| 단, 컬럼명을 `고객 수`로 출력하세요.
```sql
select count(*) from customers;

count(*)
--------
59
```

### 5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.
| 단, 각각의 컬럼명을 `이름`, `성`으로 출력하고, `이름`을 기준으로 내림차순으로 5개까지 출력하세요.

```sql
select firstname, LastName from customers
where Country = 'USA'
order by firstName desc
limit 5;

FirstName  LastName
---------  ----------
Victor     Stevens
Tim        Goyer
Richard    Cunningham
Patrick    Gray
Michelle   Brooks
```

### 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.
| 단, 컬렴명을 `송장수`로 출력하세요.

```sql
select count(*) as 송장수 from invoices
where BillingPostalCode is not null;

송장수
---
384
```

### 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.
| 단, `InvoiceDate`를 기준으로 내림차순으로 5개까지 출력하세요.
```sql
select * from invoices
where BillingState is null
order by InvoiceDate DESC
limit 5;

InvoiceId  CustomerId  InvoiceDate          BillingAddress                            BillingCity   BillingState  
---------  ----------  -------------------  ----------------------------------------  ------------  ------------    
412        58          2013-12-22 00:00:00  12,Community Centre                       Delhi                       
411        44          2013-12-14 00:00:00  Porthaninkatu 9                           Helsinki                     
410        35          2013-12-09 00:00:00  Rua dos Campeoes Europeus de Viena, 4350  Porto                       
404        6           2013-11-13 00:00:00  Rilska 3174/6                             Prague                       
403        56          2013-11-08 00:00:00  307 Macacha Guemes                        Buenos Aires                
```

### 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.
| `strftime`를 검색해서 활용해보세요.

```sql
select count(*) from invoices
where (InvoiceDate) like '2013%';

count(*)
--------
80
```

### 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.
| 단, 각각의 컬럼명을 `고객ID`, `이름`,`성`으로 출력하고, `고객ID`을 기준으로 오름차순으로 출력하세요.
```sql
select 
    CustomerId as 고객ID, 
    FirstName as 이름, 
    LastName as 성
from customers
where FirstName like 'L%'
    order by CustomerId;
    
고객ID  이름        성
----  --------  ---------
1     Luis      Goncalves
2     Leonie    Kohler
45    Ladislav  Kovacs
47    Lucas     Mancini
57    Luis      Rojas
```

### 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.
| 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.

```sql
select  
    count(*) as "고객 수",
    country as 나라
from customers
group by country
order by "고객 수" desc
limit 5;

고객 수  나라
----  -------
13    USA
8     Canada
5     France
5     Brazil
4     Germany
```

### 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.
```sql
select 
    ArtistId, 
    count(ArtistId) as "앨범 수" 
from albums
group by ArtistId
order by "앨범 수" desc
limit 1;

ArtistId  앨범 수
--------  ----
90        21
```

### 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요
| 단, 앨범 수를 기준으로 내림차순으로 출력하세요.
```sql 
select 
    ArtistId, 
    count(ArtistId) as "앨범 수"
from albums
group by ArtistId
having "앨범 수" >= 10
order by "앨범 수" desc;

ArtistId  앨범 수
--------  ----
90        21
22        14
58        11
50        10
150       10
```

### 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.
| 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.
```sql 
select count(*) as "고객 수", country, State
from customers
where state is not null
group by country, state
order by "고객 수" desc, country desc
limit 5;

고객 수  Country  State
----  -------  -----
3     USA      CA
3     Brazil   SP
2     Canada   ON
1     USA      WI
1     USA      WA
```

### 14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.
| 단, `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 

```sql 
SELECT
    CustomerId,
    CASE   
        when Fax is null then "x"
        when Fax is not null then "O"
    end as "Fax 유/무"
from customers
order by customerid
limit 5;

CustomerId  Fax 유/무
----------  -------
1           O
2           x
3           x
4           x
5           O
```

### 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.
| 단, 점원의 `LastName`, `FirstName`, `나이` 컬럼만 출력하고, `EmployeeId`를 기준으로 오름차순으로 출력하세요.

| cast(), strftime(), 오늘 날짜를 구하는 함수를 검색하고, 활용해보세요.

```sql 
select LastName, FirstName,
    (cast(strftime('%Y') as integer) - cast(BirthDate as integer) + 1) "나이"
from employees
order by EmployeeId;

LastName  FirstName  나이
--------  ---------  --
Adams     Andrew     61
Edwards   Nancy      65
Peacock   Jane       50
Park      Margaret   76
Johnson   Steve      58
Mitchell  Michael    50
King      Robert     53
Callahan  Laura      55
```

### 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.
| artists 테이블과 albums 테이블의 `ArtistId` 활용하세요.
```sql 
select Name from artists
WHERE   
    ArtistId = (
    select ArtistId from albums
    group by artistid
    order by count(artistid) DESC
    limit 1);
    
Name
-----------
Iron Maiden
```

### 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.
| genres 테이블과 tracks 테이블의 `GenreId` 활용하세요.
```sql 
select Name, GenreId
from genres
WHERE
    GenreId = (
    select genreId
    from tracks
    group by GenreId
    order by count(*));
    
Name   GenreId
-----  -------
Opera  25
```


### 자유롭게 문제를 만들어 보시고, 디스코드 채널에 공유해보세요!

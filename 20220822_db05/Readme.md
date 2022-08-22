### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
select *
from playlist_track
order by playlistId desc
limit 5;

PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select *
from tracks
order by TrackId
limit 5;

TrackId  Name                                     AlbumId  MediaTypeId  GenreId  Composer                                                      Milliseconds  Bytes     UnitPrice 
-------  ---------------------------------------  -------  -----------  -------  ------------------------------------------------------------  ------------  --------  --------- 
1        For Those About To Rock (We Salute You)  1        1            1        Angus Young, Malcolm Young, Brian Johnson                     343719        11170334  0.99      

2        Balls to the Wall                        2        2            1                                                                      342562        5510424   0.99      

3        Fast As a Shark                          3        2            1        F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman           230619        3990994   0.99      

4        Restless and Wild                        3        2            1        F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider &   252051        4331779   0.99      
                                                                                 W. Hoffman

5        Princess of the Dawn                     3        2            1        Deaffy & R.A. Smith-Diesel                                    375418        6290521   0.99
```

### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 

```sql
select playlist_track.playlistid, tracks.Name
from tracks inner join playlist_track
    on tracks.TrackId = playlist_track.TrackId
order by Name desc
limit 5;

PlaylistId  Name
----------  -------------------
1           Ultimo Pau-De-Arara
8           Ultimo Pau-De-Arara
1           Oia Eu Aqui De Novo
8           Oia Eu Aqui De Novo
1           Oculos
```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select playlist_track.PlaylistId, tracks.Name
from playlist_track inner join tracks
    on playlist_track.TrackId = tracks.TrackId
where playlist_track.PlaylistId = 10
order by Name DESC
limit 5;

PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
select count(*)
from tracks inner join artists
    on tracks.Composer = artists.Name;
    
count(*)
--------
402
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
select count(*)
from tracks left join artists
    on tracks.Composer = artists.Name;
    
count(*)
--------
3503
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
inner join 은 두 테이블에서 공통부분만을 출력하는 기능이지만 
left join은 왼쪽 테이블을 모두 출력하면서 왼쪽과 오른쪽의 공통부을 함께 표시해 주는 기능이라서 행의 개수가 다르게 나온다.
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
select InvoiceLineId, InvoiceId
from invoice_items
order by InvoiceId
limit 5;

InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2
```

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select InvoiceId, CustomerId
from invoices
order by InvoiceId
limit 5;

InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```sqlite
select invoice_items.InvoiceLineId, invoices.InvoiceId
from invoice_items left join invoices
    on invoice_items.InvoiceId = invoices.InvoiceId
order by invoice_items.InvoiceId desc
limit 5;

InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2239           411
2238           411
2237           411
2236           411
```


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select invoices.invoiceid, customers.CustomerId
from invoices left join customers
    on invoices.customerId = customers.CustomerId
order by invoices.InvoiceId DESC
limit 5;

InvoiceId  CustomerId
---------  ----------
412        58
411        44
410        35
409        29
408        25
```

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
select 
    invoice_items.InvoiceLineId,
    invoices.InvoiceId,
    customers.CustomerId
from invoice_items 
    left join invoices
        on invoice_items.InvoiceId = invoices.InvoiceId
    left join customers
        on invoices.CustomerId = customers.CustomerId
order by invoices.InvoiceId DESC
limit 5;

InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2226           411        44
2227           411        44
2228           411        44
2229           411        44
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
select customers.CustomerId, count(*)
from customers 
    left join invoices
        on customers.CustomerId = invoices.CustomerId
    left join invoice_items
        on invoices.InvoiceId = invoice_items.InvoiceId
group by customers.CustomerId
order by customers.CustomerId
LIMIT 5;

CustomerId  count(*)
----------  --------
1           38
2           38
3           38
4           38
5           38
```


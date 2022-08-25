select *
from users;

select age, count(*)
from users
group by age
order by age;

select avg(balance), count(*)
from users
WHERE
    balance > (
        select avg(balance)
        from users);

---------------------------------------------
select count(*), avg(balance), avg(age)
from users;

select last_name, first_name, age
from users
where (last_name, age) in(
    SELECT  
        last_name,
        min(age)
    from users
    group by last_name)
order by last_name;

----------------------------------
select
    id,
    case
        when gender = 1 then '남자'
        when gender = 2 then '여자'
        else '모름'
    END as '성별'
from healthcare
limit 5;

--------------------------------
select 
    last_name, first_name,
    age,
    CASE
        when age <= 18 then '청소년'
        when age <= 30 then '청년'
        when age <= 64 then '중장년'
        else '모름'
    end as '연령대'
from users
limit 5;

-----------------------------------
select last_name, first_name, min(age)
from users;

select count(*)
from users
where 
    age = (
    select min(age)
    from users);

--------------------------------
select avg(balance)
from users;

select count(*)
from users
where 
    balance >= (
    select avg(balance)
    from users);

------------------------------------------
select country
from users
where last_name = '유' and first_name = '은정';

select count(*)
from users
where 
    country = (
    select country
    from users
    where last_name = '유' and first_name = '은정'); 

------------------------------------
select count(*), avg(balance), avg(age)
from users;

SELECT
    (select count(*) from users) as 총인원,
    (select avg(balance) from users) AS 평균연봉,
    (select avg(age) from users) as 평균나이;

---------------------------------------
select country
from users
where last_name = '이' and first_name = '은정';

select count(*)
from users
where 
    country in (
    select country
    from users
    where last_name = '이' and first_name = '은정');

-----------------------------------------------------
select last_name, min(age)
from users
group by last_name;

select last_name, first_name, age
from users
where 
    (last_name, age) in (
    select last_name, min(age)
    from users
    group by last_name)
order by last_name;

-- 2. -------------------------------
select * from albums
where 
    nullif(AlbumId, '') is null or
    Title = '' OR
    ArtistId = '';

select * from artists
where 
    nullif(ArtistId, '') is null OR
    nullif(Name, '') is null;

select * from customers
where 
    nullif(CustomerId, '') is null or
    nullif(firstname, '') is null or
    nullif(LastName, '') is null or
    nullif(company, '') is null Or
    nullif(Address, '') is null or
    nullif(City, '') is null or
    nullif(State, '') is null or
    nullif(Country, '') is null or
    nullif(PostalCode, '') is null or
    nullif(Phone, '') is null or
    nullif(Fax, '') is null or
    nullif(Email, '') is null or
    nullif(SupportRepId, '') is null;

-- 3. ---------------------------------
select * from albums
order by title
limit 5;

-- 4. --------------------------------
select count(*) from customers;

-- 5. ------------------------------------
select firstname, LastName from customers
where Country = 'USA'
order by firstName desc
limit 5;

-- 6. ----------------------------------
select count(*) as 송장수 from invoices
where BillingPostalCode is not null;

-- 7. ---------------------------------
select * from invoices
where BillingState is null
order by InvoiceDate DESC
limit 5;

-- 8. ----------------------------------
select count(*) from invoices
where (InvoiceDate) like '2013%';

select strftime('y%', '2013')
from invoices
limit 5;

-- select count(*) from invoices
-- where InvoiceDate = (

-- 9. ---------------------------------
select 
    CustomerId as 고객ID, 
    FirstName as 이름, 
    LastName as 성
from customers
where FirstName like 'L%'
    order by CustomerId;

-- 10. -----------------------------------
select  
    count(*) as "고객 수",
    country as 나라
from customers
group by country
order by "고객 수" desc
limit 5;

-- 11. -----------------------------------
select 
    ArtistId, 
    count(ArtistId) as "앨범 수"
from albums
group by ArtistId
order by "앨범 수" desc
limit 1;

-- 12. -----------------------------------
select 
    ArtistId, 
    count(ArtistId) as "앨범 수"
from albums
group by ArtistId
having "앨범 수" >= 10
order by "앨범 수" desc;

-- 13. --------------------------------------
select count(*) as "고객 수", country, State
from customers
where state is not null
group by country, state
order by "고객 수" desc, country desc
limit 5;

-- 14. --------------------------------
SELECT
    CustomerId,
    CASE   
        when Fax is null then "x"
        when Fax is not null then "O"
    end as "Fax 유/무"
from customers
order by customerid
limit 5;

-- 15. ------------------------------------------
select LastName, FirstName,
    (cast(strftime('%Y') as integer) - cast(BirthDate as integer) + 1) "나이"
from employees
order by EmployeeId;

-- 16. ---------------------------------------
select ArtistId from albums
group by artistid
order by count(artistid) DESC
limit 1;

select Name from artists
WHERE   
    ArtistId = (
    select ArtistId from albums
    group by artistid
    order by count(artistid) DESC
    limit 1);

-- 17. ----------------------------------------
select genreId, count(*)
from tracks
group by GenreId
order by count(*);

select Name, GenreId
from genres
WHERE
    GenreId = (
    select genreId
    from tracks
    group by GenreId
    order by count(*));
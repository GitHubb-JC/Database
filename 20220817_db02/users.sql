-- SQLite
create table users (
    first_name text not null,
    last_name text not null,
    age integer not null,
    country text not null,
    phone text not null,
    balance integer not null
);

-- 1.
select smoking, count(smoking)
from healthcare
where smoking != ''
group by smoking;

-- 2. 
select is_drinking, count(is_drinking)
from healthcare
where is_drinking != ''
group by is_drinking;

-- 3. 
select is_drinking, count(*) as 'blood_pressure >= 200'
from healthcare
where blood_pressure >= 200 and blood_pressure != ''
group by is_drinking;

-- 4. 
select sido, count(*)
from healthcare
group by sido
having count(*) > 50000;

-- 5.
select height, count(*)
from healthcare
group by height
order by count(*) DESC
limit 5;

-- 6. 
select weight, height, count(*)
from healthcare
group by weight, height
order by count(*) DESC
limit 5;

-- 7. 
select is_drinking, round(avg(waist), 1), count(*)
from healthcare
where is_drinking != ''
group by is_drinking;

-- 8. 
select 
    gender, 
    round(avg(va_left), 2) as '평균 왼쪽 시력', 
    round(avg(va_right), 2) as '평균 오른쪽 시력'
from healthcare
group by gender;

-- 9. 
select 
    age, 
    round(avg(height), 1) as '평균 키', 
    round(avg(weight), 1) as '평균 몸무게'
from healthcare
group by age
having avg(height) >= 160 and avg(weight) >= 60;

-- 10. 
select 
    is_drinking, 
    smoking,
    round(avg((weight/((height * 0.01) * (height * 0.01)))), 1) as '평균 BMI'
from healthcare
where is_drinking != '' and smoking != ''
group by is_drinking, smoking;
-- 코드를 작성해주세요
with a as(
select if(length is null, 10, length) as l
from FISH_INFO
)

select round(avg(l) ,2) as AVERAGE_LENGTH
from a
;


-- 코드를 작성해주세요
select concat(LENGTH, 'cm') AS MAX_LENGTH
from FISH_INFO
order by LENGTH DESC
LIMIT 1
;
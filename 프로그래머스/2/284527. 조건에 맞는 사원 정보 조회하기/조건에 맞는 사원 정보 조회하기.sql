-- 코드를 작성해주세요

select made.SCORE
    , e.EMP_NO
    , e.EMP_NAME
    , e.POSITION
    , e.EMAIL
from HR_EMPLOYEES as e
    inner join (SELECT EMP_NO, sum(SCORE) as SCORE
                FROM HR_GRADE 
                group by EMP_NO
                order by SCORE desc
                limit 1) as made on e.EMP_NO = made.EMP_NO
    inner join HR_DEPARTMENT as d on e.DEPT_ID = d.DEPT_ID
;
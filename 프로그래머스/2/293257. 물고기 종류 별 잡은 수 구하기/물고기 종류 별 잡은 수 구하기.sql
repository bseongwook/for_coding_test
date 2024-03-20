-- 코드를 작성해주세요
# with a as (
#     select FISH_TYPE
#         ,count(FISH_TYPE) as FISH_COUNT
#     from FISH_INFO
#     group by FISH_TYPE
# )

# select a.FISH_COUNT as FISH_COUNT
#     , n.FISH_NAME as FISH_NAME
# from a
#     inner join FISH_NAME_INFO as n on a.FISH_TYPE = n.FISH_TYPE
# order by FISH_COUNT desc

SELECT
    COUNT(ID) FISH_COUNT
    , B.FISH_NAME
FROM
    FISH_INFO A
    INNER JOIN FISH_NAME_INFO B
        ON A.FISH_TYPE = B.FISH_TYPE
GROUP BY
    B.FISH_NAME
ORDER BY
    FISH_COUNT DESC
;
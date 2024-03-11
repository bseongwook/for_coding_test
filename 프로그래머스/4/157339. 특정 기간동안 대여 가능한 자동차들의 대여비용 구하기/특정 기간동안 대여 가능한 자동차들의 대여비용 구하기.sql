-- 코드를 입력하세요
# SELECT CC.CAR_ID
#     , CC.CAR_TYPE
#     , ROUND(30 * (1 - DP.DISCOUNT_RATE/100) * CC.DAILY_FEE) AS 'FEE'
# FROM CAR_RENTAL_COMPANY_CAR AS CC
#     LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS RH 
#         ON CC.CAR_ID = RH.CAR_ID 
#             AND RH.END_DATE >= '2022-11-01' AND RH.START_DATE <= '2022-11-30'
#     INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS DP 
#         ON CC.CAR_TYPE = DP.CAR_TYPE 
#             AND DP.DURATION_TYPE = '30일 이상'
#             AND CC.CAR_TYPE = '세단' OR CC.CAR_TYPE = 'SUV'
#     WHERE ROUND(30 * (1 - DP.DISCOUNT_RATE/100) * CC.DAILY_FEE) BETWEEN 500000 AND 1999999
#         AND RH.CAR_ID IS NULL
# ORDER BY FEE DESC, CC.CAR_TYPE, CC.CAR_ID DESC
# ;

# 정답
SELECT c.car_id, c.car_type,
       FLOOR(c.daily_fee * 30 * (1 - p.discount_rate/100)) fee
FROM CAR_RENTAL_COMPANY_CAR c
INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
ON c.car_type = p.car_type
   AND p.duration_type = '30일 이상'
   AND c.car_type IN ('SUV', '세단')
LEFT OUTER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
ON c.car_id = h.car_id
   AND h.end_date >= '2022-11-01' AND h.start_date <= '2022-11-30'
WHERE ROUND(c.daily_fee * 30 * (1 - p.discount_rate/100)) BETWEEN 500000 AND 1999999
      AND h.car_id IS NULL
ORDER BY fee DESC, c.car_type, c.car_id DESC;
;
'''
* 앱스토어 리뷰 변화를 통한 앱 만족도 요소 분석
'''
import data from playstore as reviews

WITH t1 as (
SELECT date_trunc('month', created_at) as term, app_id, app_name, review_content, star_rating
FROM reviews
WHERE created_at > '2010-01-01'
GROUP BY 1
ORDER BY 1,2 ASC
)
# 좋아하는 키워드
SELECT term, star_rating, review_content_word, mentioned_count, app_id
FROM t1
WHERE start_rating >= 4
GROUP BY 1,2,3
HAVING mentioned_count > 30
ORDER BY 1, 2, 4

# 싫어하는 키워드
SELECT term, star_rating, review_content_word, mentioned_count, app_id
FROM t1
WHERE start_rating <= 2
GROUP BY 1,2,3
HAVING mentioned_count > 30
ORDER BY 1, 2, 4



'''

'''

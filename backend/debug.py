import sys

sys.path.append('/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend')
sys.path.append('/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend/CrawlMaster')
sys.path.append('/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend/database')
from QuotaCalculate.timeQuota import TimeQuota
from QuotaCalculate.SensitiveQuota import SensitiveQuota
"""
x = TimeQuota()
x.update_all_quota(
    databaseLoc="/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend/database/example_data/巴以冲突B站视频500条详细评论清洗版.csv",
)
print(x.q)
print(x.getDateList('bilibili', 1))
"""
x = SensitiveQuota()
print(x.wordBase)
print(x.sensitiveWordCheck(""))
print("end")
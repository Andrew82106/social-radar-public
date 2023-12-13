# --coding:utf-8--
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current_path))
sys.path.append(os.path.join(os.path.dirname(current_path), '/CrawlMaster'))
sys.path.append(os.path.join(os.path.dirname(current_path), '/database'))
sys.path.append(os.path.join(os.path.dirname(current_path), '/SparkModel_V30'))
sys.path.append(os.path.join(os.path.dirname(current_path), '/CrawlMaster/Utils'))


try:
    from database.EventQuota import EventQuota
    from database.UserQuota import UserQuota
    from database.globalConfig import SupportedPlatform, commentList, newsList, userList
    from database.EventList import EventLst
    from database.Search import Search
    from database.ServerStatus import ServerStatus
    from database.SummaryData import SummaryData
    from database.AutoCache import Cache
    from SparkModel_V30.SparkApi import SparkChatModel
    from QuotaCalculate.timeQuota import TimeQuota
    from QuotaCalculate.SensitiveQuota import SensitiveQuota
    from QuotaCalculate.EmotionEvaluationQuota import EmotionEvaluationQuota
    from QuotaCalculate.OpinionQuota import OpinionQuota
    from QuotaCalculate.UserBeliefQuota import UserBQuota
    from QuotaCalculate.summaryQuota import SummaryQuota
except:
    from ..database.EventQuota import EventQuota
    from ..database.UserQuota import UserQuota
    from ..database.globalConfig import SupportedPlatform, commentList, newsList, userList
    from ..database.EventList import EventLst
    from ..database.Search import Search
    from ..database.ServerStatus import ServerStatus
    from ..database.SummaryData import SummaryData
    from ..database.AutoCache import Cache
    from ..SparkModel_V30.SparkApi import SparkChatModel
    from ..QuotaCalculate.timeQuota import TimeQuota
    from ..QuotaCalculate.SensitiveQuota import SensitiveQuota
    from ..QuotaCalculate.EmotionEvaluationQuota import EmotionEvaluationQuota
    from ..QuotaCalculate.OpinionQuota import OpinionQuota
    from ..QuotaCalculate.UserBeliefQuota import UserBQuota
    from ..QuotaCalculate.summaryQuota import SummaryQuota

from Utils.sequenceDrawer import plot_time_series
from Utils.dataSaver import DataSaver


ss = SummaryQuota()
yyy = UserBQuota()
x = SensitiveQuota()
y1 = OpinionQuota()
y = EmotionEvaluationQuota()
EventID = 2


def SensitiveDataOverAll():
    eventID = EventID
    return x.calcOverAllSensitiveQuota(eventID)


def UserQuotaOverAll():
    eventID = EventID
    return yyy.calcUserQuotaOverall(eventID)


def OpinionQuotaOverAll():
    eventID = EventID
    return y1.calcOPQuotaOverall(eventID)


def SummaryQuotaOverAll():
    eventID = EventID
    return ss.calcSQOverall(eventID)


def getTimeSeq():
    eventID = EventID
    a = TimeQuota()
    a.getDateListofAllPlatform(eventID, 'date')
    return a.fetch()


def EmotionQuotaOverAll():
    eventID = EventID
    return y.calcEQOverall(eventID)


if __name__ == '__main__':
    saver = DataSaver()
    saver.addData(SensitiveDataOverAll()['data'], 'Sensitive')
    saver.addData(UserQuotaOverAll()['data'], 'UserQuota')
    saver.addData(OpinionQuotaOverAll()['data'], 'OpinionQuota')
    saver.addData(SummaryQuotaOverAll()['data'], 'SummaryQuota')
    saver.addData(getTimeSeq()['data'], 'TimeQuota')
    saver.addData(EmotionQuotaOverAll()['data'], 'EmotionQuota')

    plot_time_series(SensitiveDataOverAll()['data'], title=f'SensitiveData EventID:{EventID}', save=f'./labPicture/SensitiveData.jpg')
    plot_time_series(UserQuotaOverAll()['data'], title=f'UserQuota EventID:{EventID}', save=f'./labPicture/UserQuota.jpg')
    plot_time_series(OpinionQuotaOverAll()['data'], title=f'OpinionQuota EventID:{EventID}', save=f'./labPicture/OpinionQuota.jpg')
    plot_time_series(SummaryQuotaOverAll()['data'], title=f'SummaryQuota EventID:{EventID}', save=f'./labPicture/SummaryQuota.jpg')
    plot_time_series(getTimeSeq()['data'], title=f'TimeQuota EventID:{EventID}', save=f'./labPicture/TimeQuota.jpg')
    plot_time_series(EmotionQuotaOverAll()['data'], title=f'EmotionQuota EventID:{EventID}', save=f'./labPicture/EmotionQuota.jpg')



    print("end")
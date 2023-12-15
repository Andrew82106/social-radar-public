from datetime import datetime, timedelta
import pandas as pd


class DataSaver:
    def __init__(self):
        self.data = {
            "timeSeq": {}
        }

    @staticmethod
    def formatTime(Time: str):
        try:
            return datetime.strftime(datetime.strptime(Time.split(" ")[0].replace("/", "-"), "%Y-%m-%d"), "%Y-%m-%d")
        except:
            return Time

    def findDataIndex(self, Data, colName):
        try:
            Data = self.formatTime(Data)
        except:
            Data = Data
        for ID in self.data[colName]:
            if self.data[colName][ID] == Data:
                return ID
        return -1

    def insert(self, data: str, colName: str, ID=-1):
        if colName not in self.data:
            self.data[colName] = {}
        if ID == -1:
            ID = 0
            for I in self.data[colName]:
                ID = max(I, ID)
            ID += 1
        self.data[colName][ID] = data

    def addData(self, D: dict, colName: str):
        for Date in D:
            Date = self.formatTime(Date)
            if self.findDataIndex(Date, 'timeSeq') == -1:
                self.insert(Date, 'timeSeq')
            ID = self.findDataIndex(Date, 'timeSeq')
            self.insert(D[Date], colName, ID)

    def saveData(self, route='./Output.xlsx'):
        # 获取时间序列列中的日期列表并排序
        time_seq_dates = list(self.data['timeSeq'].values())
        time_seq_dates.sort()

        # 获取列名（除timeSeq外）
        columns = list(self.data.keys())
        columns.remove('timeSeq')

        # 创建空的字典来存储补全数据
        complete_data = {'timeSeq': []}
        for col in columns:
            complete_data[col] = []

        # 遍历日期范围，补全数据
        start_date = datetime.strptime(time_seq_dates[0], '%Y-%m-%d')
        end_date = datetime.strptime(time_seq_dates[-1], '%Y-%m-%d')
        current_date = start_date

        while current_date <= end_date:
            formatted_date = current_date.strftime('%Y-%m-%d')

            # 检查当前日期是否在原始数据中，如果不在则补全
            if formatted_date not in time_seq_dates:
                complete_data['timeSeq'].append(formatted_date)
                for col in columns:
                    complete_data[col].append(0)
            else:
                complete_data['timeSeq'].append(formatted_date)
                for col in columns:
                    ID = self.findDataIndex(formatted_date, 'timeSeq')
                    complete_data[col].append(self.data[col].get(ID, 0))

            current_date += timedelta(days=1)

        # 将补全的数据存储到DataFrame并导出到Excel
        df = pd.DataFrame(complete_data)
        df.sort_values(by='timeSeq', inplace=True)  # 按照时间序列列排序
        df.to_excel(route, index=False)
        print(f"data saved to {route}")
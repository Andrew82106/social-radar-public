from datetime import datetime
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
        if ID == -1:
            ID = 0
            for I in self.data[colName]:
                ID = I + 1
        if colName not in self.data:
            self.data[colName] = {}
        self.data[colName][ID] = data

    def addData(self, D: dict, colName: str):
        for Date in D:
            Date = self.formatTime(Date)
            if self.findDataIndex(Date, 'timeSeq') == -1:
                self.insert(Date, 'timeSeq')
            ID = self.findDataIndex(Date, 'timeSeq')
            self.insert(D[Date], colName, ID)

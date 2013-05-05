'''
Created on 2011-6-30

@author: haines
'''
from tracker.trace import TrackerFactory

class MonitorHistory(object):
    def __init__(self, monitorName):
        self.monitorName = monitorName
        
    def lastRun(self):
        index = self.__findLastIndex()
        return self.__findHistory(index)
    
    def thisRun(self, index):
        return self.__findHistory(index);
    
    def allHistory(self, pageIndex=0, pageSize=0):
        terms = {"name":self.monitorName}
        TrackerFactory().getTracker().allMonitorTrace(terms, [], pageIndex, pageSize)
    
    def __findLastIndex(self):
        return 0
    
    def __findHistory(self, index):
        return {"index": index}
    
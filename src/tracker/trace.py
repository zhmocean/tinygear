'''
Created on 2011-5-9

@author: Administrator
'''

class Tracker(object):
    '''
    classdocs
    '''

    def __init__(self, config):
        self.__parseTracker(config)
        
    def trace(self, data):
        print ""
        
    def allTrace(self, traceType, terms, sort, pageIndex=0, pageSize=0):
        return []

    def __parseTracker(self, config):
        self.server = ""

class MysqlTracker(Tracker):
    def __init__(self):
        print 'MysqlTracker'
    
class MongoTracker(Tracker):
    def __init__(self):
        print 'MongoTracker'
    
class SqliteTracker(Tracker):
    def __init__(self):
        print 'SqliteTracker'
        
class TrackerFactory():
    def getTracker(self):
        return MongoTracker()
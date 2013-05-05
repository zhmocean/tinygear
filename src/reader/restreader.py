#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
import json
from util.url import urlGet
import datetime

class RestReader(object):
    def __init__(self, config):
        self.targetHost = config["targetHost"]
        self.appName = config["appName"]
        self.errorTackerHost = config["host"]
        self.hour = config["hour"]
        if config.has_key("type"):
            self.type = config["type"]
        else:
            self.type = []
        
    def __todayAllInfo(self, hour):
        '''
            get all count at LAST hour if hour is 1
        '''
        url = "http://"
        if hour <= -1:
            url = url+ self.errorTackerHost+"/rest/"+self.targetHost+"/"+self.appName
        else:
            url = url+ self.errorTackerHost+"/rest/"+self.targetHost+"/"+self.appName+"?hour=" + str(hour)
            
        print url
        return urlGet(url)
    
    def __todayAllInfoWithType(self, hour):
        '''
            get all count at LAST hour if hour is 1
        '''
        url = "http://"
        if hour <= -1:
            url = url+ self.errorTackerHost+"/rest/"+self.targetHost+"/"+self.appName
        else:
            url = url+ self.errorTackerHost+"/rest/"+self.targetHost+"/"+self.appName+"?hour=" + str(hour)
            
        print url
        return urlGet(url)

    def __parseStatJsonDataCount(self, str):
        rs = json.loads(str)
        dataCount = len(rs["data"])
       
        if dataCount >0:
            return int(rs["data"][0]["count"])
        else:
            return 0
        
    def __parseStatJsonDataTime(self, str):
        rs = json.loads(str)
        dataCount = len(rs["data"])
        
        if dataCount >0:
            return datetime.datetime.strptime(rs["data"][0]["time"], '%Y-%m-%d %H:%M:%S')
        else:
            return datetime.datetime.today()
        
    def touch(self):
        hour = int(self.hour)
        response = self.__todayAllInfoWithType(hour)
        try:
            rs = json.loads(response)
            count = 0
            orgcount = 0
            ignoreList = []

            for t in rs["data"]:
                orgcount += t["count"]

                if not self.__exsThisType(t, self.type):
                    #记录该type
                    count += t["count"]
                else:
                    #记录被忽略的type
                    ignoreList.append(t)
                    
            return {"head":{"hour":hour, "time":datetime.datetime.today()}, "body":[{"count":count,"orgcount":orgcount}]}
        except:
            return {"head":{"state":"error", "time":datetime.datetime.today()}, "body":[{}]}
            
    def __exsThisType(self, type, exs):
        for exItem in exs:
            if self.__exThisType(type, exItem):
                return True
        return False
        
    def __exThisType(self, type, ex):   
        if len(ex.keys())==0:
            #排除空条件，避免忽略所有
            return False

        for key in ex.keys():
            if (not type.has_key(key)) or  (not type[key] == ex[key]):
                return False
            
        return True
                
if __name__ == "__main__":
    config = {"host":"localhost/error", "targetHost":"127.0.0.1", "appName":"myprod"}
    er = RestReader(config)
    args = {"hour": 24}
    print er.touch(args)
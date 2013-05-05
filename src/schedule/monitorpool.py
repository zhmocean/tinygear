'''
Created on 2011-5-27

@author: Administrator
'''
from condition.jsonparser import JsonCondition

from logger.logger import Logger
from schedule.sandglass import SandGlass
from reader.readerfactory import ReaderFactory
from publish.publisher import PublisherFactory
import threading
from schedule.history import MonitorHistory

class Monitor(object):
    def __init__(self, name, config):
        self.__name = name
        self.reload(config)
        self.__history = MonitorHistory(self.__name)

    def __doTouch(self):
        data = self.__read()
        if(self.__check(data)):
            print "warn!"
            self.__publish(data)

    def __check(self, data):
        return JsonCondition(self.__checker).check(data)

    def __publish(self, data):
        self.__publisher.do(data, {})

    def __read(self):
        return self.__reader.touch()

    def reload(self, config):
        self.__reader = config["reader"]
        self.__publisher = config["publisher"]
        self.__sandglass = config["sandglass"]
        self.__checker = config["checker"]

    @property
    def myName(self):
        return self.__name

    @property
    def history(self):
        return self.__history

    @property
    def sandGlass(self):
        return self.__sandglass


    def go(self):
        print self.__name+" willGo!"
        self.t = threading.Thread(target=self.__doTouch, args=())
        self.t.start()

class MonitorFactory(object):
    def monitor(self, config):
        s = self.parseSandGlass(config["sandglass"])
        r = ReaderFactory().createReader(config["reader"])
        p = PublisherFactory().createPublisher(config["publisher"])      

        return Monitor(config["name"],
                  {"sandglass":s,
                   "reader":r,
                   "publisher":p,
                   "checker":config.get("checker")
                   })
        
    def parseSandGlass(self, config):
        return SandGlass(config)

        
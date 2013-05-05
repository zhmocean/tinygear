'''
Created on 2011-4-6

@author: Administrator
'''
import threading
import time
import datetime

from config.localmonbox import LocalMonitorBox
from schedule.monitorpool import MonitorFactory

class MonitorSchedule(object):
    def __init__(self):
        self.mlist = {}
        self.slist = {}
        self.t = threading.Thread(target=self.__run, args=())
        self.delay = 5
        
    def __run(self):
        while (self.runflag):
            for key in self.slist.keys():
                if self.slist.get(key).invert(datetime.datetime.today()):
                    m = MonitorFactory().monitor(self.mlist.get(key))
                    m.go()
                    
            time.sleep(self.delay);
            
    def registeMonitor(self, monitor):
        self.mlist[monitor["name"]] = monitor
        self.slist[monitor["name"]] = MonitorFactory().parseSandGlass(monitor["sandglass"])
        
    def registeMonitors(self, monitors):
        for m in monitors:
            self.registeMonitor(m)
            
    def reload(self, monitorBox):
        self.mlist.clear()
        self.slist.clear()
        self.registeMonitors(monitorBox.monitors())
            
    def monitor(self, name):
        return self.mlist[name]
    
    def monitors(self):
        return self.mlist
    
    def removeMonitor(self, m):
        if(self.mlist.has_key(m.name)):
            del self.mlist[m.name]
        
    def go(self):
        self.runflag = True
        self.t.start()
        
    def stop(self):
        self.runflag = False

if __name__ == "__main__":
    ms = MonitorSchedule()
    ms.registeMonitors(LocalMonitorBox().monitors())
    
    ms.go()
    time.sleep(20)
    ms.yu()
    
    
    
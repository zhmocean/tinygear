'''
Created on 2011-4-8

@author: Administrator
'''
import datetime
import time

class SandGlass(object):
    def __init__(self, config):
        self.delay = config["delay"]
        self.last = datetime.datetime.today()
        
    def invert(self, now):
        return self.__iWillInvert(now)
    
    def __iWillInvert(self, now):
        if (now - self.last).seconds > self.delay:
            self.last = now
            return True
        else:
            return False
        
if __name__ == "__main__":
    config = {"delay":6}
    s = SandGlass(config)
    
    for i in range(0, 100):
        print s.invert(datetime.datetime.today())
        time.sleep(2)
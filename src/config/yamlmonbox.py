'''
Created on 2011-4-11

@author: Administrator
'''
import yaml

class YamlMonitorBox(object):
    '''
    classdocs
    '''
    def __init__(self, cfgfile):
        self.cfgfile = cfgfile
        
    def monitors(self):
        return self.__mconfigs()

    def __mconfigs(self):
        f = file(self.cfgfile, 'r')
        ret = yaml.load(f)
        f.close()
        return ret
                
if __name__ == "__main__":
    lmb = YamlMonitorBox('../conf/monitor.yaml')
    print lmb.monitors()
    lmb.monitors()[0].go()
    lmb.monitors()[1].go()
    lmb.monitors()[2].go()
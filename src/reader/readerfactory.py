'''
Created on 2011-5-30

@author: Administrator
'''

from reader.mysql import MysqlCmdReader
from reader.restreader import RestReader


class ReaderFactory(object):
    def createReader(self, config):
        if config["type"] == "db":
            return self.__parseDbReader(config)
        elif config["type"] == "rest":
            return self.__parseRestReader(config)
        else:
            return self.__parseDefaultReader(config)
        
    def __parseDbReader(self, config):
        if config["driver"] == "mysql":
            return MysqlCmdReader(config)
        else:
            return None
        
    def __parseRestReader(self, config):
        return RestReader(config)
        
    def __parseDefaultReader(self, config):
        return None
        
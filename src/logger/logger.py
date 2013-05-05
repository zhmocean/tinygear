'''
Created on 2011-5-9

@author: Administrator
'''

class Logger(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def info(self, message):
        print "[INFO]" +message
        
    def warn(self, message):
        print "[WARN]" +message
        
    def error(self, message):
        print "[ERROR]" +message
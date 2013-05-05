'''
Created on 2011-4-11

@author: Administrator
'''


class LocalMonitorBox(object):
    '''
    classdocs
    '''
        
    def monitors(self):
        return self.__mconfigs()

    
    
    def __mconfigs(self):
        return [
                 {"name":"monitor1",
                 "reader":{ "type":"db",
                            "driver":"mysql",
                            "host":"localhost",
                            "dbname":"p",
                            "username":"user",
                            "password":"pwd",
                            "sql":"select count(*) from table"
                           },
                 "publisher":{"who":"monitor1_publisher"
                              },
                 "sandglass":{"delay":7 },
                 "checker": {
                    "count(*)": {"$gt":10000000}
                 }
                },
                
                {   "name":"monitor2",
                    "reader":{ "type":"db",
                            "driver":"mysql",
                            "sql":"select count(*) from table where state='success'",
                            "host":"localhost",
                            "dbname":"p",
                            "username":"user",
                            "password":"pwd"

                           },
                    "publisher":{"who":"monitor2_publisher"
                              },
                    "sandglass":{"delay":3
                              },
                    "checker": {
                        "body.0.count(*)": {"$gt":10000000}
                    }
                },
                
                {   "name":"monitor3",
                    "reader":{"type":"rest",
                               "host":"localhost:8080/error",
                               "targetHost":"localhost",
                               "appName":"myproduct",
                               "hour": -1
                               },
                    "publisher":{"who":"monitor3_publisher"
                                  },
                    "sandglass":{"delay":2
                                  },
                    "checker": {
                        "body.0.count": {"$gt":0}
                    }
                }
                ]
                
if __name__ == "__main__":
    lmb = LocalMonitorBox()
    print lmb.monitors()
    lmb.monitors()[0].go()
    lmb.monitors()[1].go()
    lmb.monitors()[2].go()
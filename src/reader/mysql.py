'''
Created on 2011-4-6

@author: Administrator
'''
import subprocess

class MysqlCmdReader(object):
    def __init__(self, config):
        self.host = config["host"]
        self.dbname = config["dbname"]
        self.username = config["username"]
        self.password = config["password"]
        self.config = config
        
    def touch(self):
        model = "cmd"
        if self.config.has_key("model"):
            model = self.config["model"]
        data = self.__touchSql(model, self.config["sql"])
        
        return {"data": data, "head":{"count":len(data), "sql": self.config["sql"]}}

    def __touchSql(self, model, sql):
        print sql
        if model == "cmd": 
            rs = self.__touchCmd(sql)
            return self.__parseCmd(rs)
        else:
            return self.__touchConn(sql)
        
    def __touchConn(self, sql):
        return []
    
    def __prepareMysql(self, host, dbname, username, password):
        return "mysql -u "+username+" -p"+password+"  -h"+host+" "+dbname
        
    def __touchCmd(self, sql): 
        cmdline = self.__prepareMysql(self.host, self.dbname, self.username, self.password) + " -e \"" + sql + "\""
        return subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines()
    
    def __parseCmd(self, data):
        result = []
        for i in range(1, len(data)):
            result.append(self.__str2Map(data[0], data[i]))
            
        return result
            
    def __str2Map(self, columns, data):
        print data
        try:
            result = {}
            cs = columns.split()
            ds = data.split()
            for i in range(0, len(columns.split())):
                result[cs[i]] = str(ds[i]).strip()
            
            return result
        except:
            return {}
    
    def _testStr2Map(self, columns, data):
        return self.__str2Map(columns, data)
    
    def _testParseCmd(self, data):
        return self.__parseCmd(data)
    
if __name__ == "__main__":
    r = MysqlCmdReader("", "", "", "")
    print r._testStr2Map("adfs    sadfad    aaa", "1    saf1    23adf")
    m = ["adfs    sadfad    aaa"]
    m.append("1    saf1    23adf")
    m.append("2    saf2    23dfadf")
    m.append("3    saf3    23dfadgf")
    
    print r._testParseCmd(m)
    
    r = MysqlCmdReader("localhost", "p", "user", "pwd")
    args = {"sql":"select * from table limit 3"}
    print r.touch(args)
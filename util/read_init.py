#coding:utf-8
import os
import sys
import configparser
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../config")
sys.path.append(path)

class ReadIni:
    def __init__(self,filepath=None):
        if filepath==None:
            self.filepath=path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini=configparser.ConfigParser()
        read_ini.read(self.filepath+"//LocalElement.ini") 
        return read_ini

    def get_value(self,session,key):
        try:
            value = self.data.get(session,key)
        except:
            value = None
        return value

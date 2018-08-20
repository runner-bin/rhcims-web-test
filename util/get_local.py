# coding:utf-8
from util.read_init import ReadIni

# 此类封装driver.find_element_by_meyhod
class GetLocal:
    def __init__(self,driver):
        self.driver= driver
    def get_element(self,session,key):
        value = ReadIni().get_value(session,key)
        if value!=None:
            by = value.split('>')[0]
            local_by = value.split('>')[1]
            if by =="id":
                return self.driver.find_element_by_id(local_by)
            elif by =="className":
                return self.driver.find_element_by_id(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None
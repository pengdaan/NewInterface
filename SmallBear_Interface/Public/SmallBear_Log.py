# -*- coding: utf-8 -*-
import logging,time,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGFile=parentdir+'\TestLog'
__author__ = 'leo'
class SmallBear_Log():
    def __init__(self,title):
        self.day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        self.logger=logging.Logger(title)
        filepath=os.path.join(LOGFile+'\\%s.log'%self.day)
        # 指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
        self.logger.setLevel(logging.INFO)
        # 创建一个handler，用于写入日志文件
        self.logfile=logging.FileHandler(filepath)
        self.logfile.setLevel(logging.INFO)
        # 再创建一个handler，用于输出到控制台
        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        # 定义handler的输出格式（formatter）
        self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 给handler添加formatter
        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)
        # 给logger添加handler
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)

    def debugInfo(self, message):
        self.logger.debug(message)
    def info_log(self, message):
        self.logger.info(message)
    def ware_log(self, message):
        self.logger.warn(message)
    def error_log(self, message):
        self.logger.error(message)
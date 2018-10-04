# 必要的一些常用函数
import datetime
import os

# 计时工具，记录某个操作的时间
class timingTool():
    startTime = 0

    def __init__(self):
        self.startTime = datetime.datetime.now()

    def timmingGet(self):
        return datetime.datetime.now() - self.startTime

    def getNow(self):
        return datetime.datetime.now()
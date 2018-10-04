import datetime
# 记录工具


class logTool():

    path = ""
    reader = ""

    def __init__(self, path):
        print(path)
        self.path = path
        self.open()
        self.close()

    def writer(self, note):
        self.open()
        print(note, file=self.reader)
        self.close()

    def open(self):
        self.reader = open(self.path, "a")

    def close(self):
        self.reader.close()

    def info(self, note):
        self.open()
        print("[INFO:%s] : %s" %
              (datetime.datetime.now(), note), file=self.reader)
        self.close()

    def error(self, note):
        self.open()
        print("[ERROR:%s] : %s" %
              (datetime.datetime.now(), note), file=self.reader)
        self.close()
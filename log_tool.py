import datetime
# 记录工具


class logTool():

    path = ""
    reader = ""

    basic_msg = ""

    def __init__(self, path, basic_msg=""):
        print(path)
        self.path = path
        self.basic_msg = basic_msg
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

    def info(self, note, isPrint=1):
        self.open()
        print("[INFO:%s]%s : %s" %
              (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.basic_msg, note), file=self.reader)
        if isPrint:
            print("[INFO:%s]%s : %s" %
                  (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.basic_msg, note))
        self.close()

    def error(self, note, isPrint=1):
        self.open()
        print("[ERROR:%s]%s : %s" %
              (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.basic_msg, note), file=self.reader)
        if isPrint:
            print("[ERROR:%s]%s : %s" %
                  (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.basic_msg, note))
        self.close()
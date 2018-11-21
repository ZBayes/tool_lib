from log_tool import logTool
import os


class res_tab():

    path = ""
    eval_idx = []
    reader = ""
    log_tool_path = ""

    def __init__(self, path, eval_idx, log_tool_path=""):
        check_tmp = self.check_exist(path, eval_idx)
        log = ""
        if log_tool_path == "":
            print("warning: log_tool_path has not been setted")
        else:
            log = logTool(log_tool_path, basic_msg="RES_TAB")
        log.info("result input: %s" % log_tool_path)
        self.path = path
        self.eval_idx = eval_idx
        self.eval_idx.append("msg")
        self.open()
        if check_tmp == "error_file":
            idx = eval_idx[:]
            print("\t".join(idx), file=self.reader)
        self.close()

    def check_exist(self, path, eval_idx):
        if os.path.exists(path):
            with open(path) as f:
                check = f.readlines()
                if len(check) == 0:
                    os.remove(path)
                    print("it is error file and we have made a new one")
                    return "error_file"
                check = check[0].strip().split('\t')
                tmp_form = eval_idx[:]
                tmp_form.append("msg")
                for idx in range(len(check)):
                    if check[idx] != tmp_form[idx]:
                        raise res_tab_error(
                            "init: import length error, %s-%s" % (check, tmp_form))
                return "done"
        return "error_file"

    def open(self):
        self.reader = open(self.path, "a")

    def close(self):
        self.reader.close()

    def write(self, eval_res, msg):
        if type([]) != type(eval_res):
            raise res_tab_error("init: import length error, %s" % eval_res)
            return 
        if len(eval_res) + 1 != len(self.eval_idx) and len(self.eval_idx) > 0:
            raise res_tab_error("init: import length error, %s, %s" % (len(eval_res), len(self.eval_idx)))
            return
        self.open()
        print('\t'.join([str(i) for i in eval_res]) + '\t' + msg, file=self.reader)
        self.close()


class res_tab_error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

import threading
import collections
import re
import datetime


def print_info(note, basic_msg = ""):
	print("[INFO:%s]%s : %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), basic_msg, note))

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def multi_thread(data_list, func, ex_arg=[], thread_numbers=64):
    threads = []
    data_group = []

    for i in range(thread_numbers):
        data_group.append([])

    for idx in range(len(data_list)):
        group_index = idx % thread_numbers
        data_group[group_index].append(data_list[idx])

    thread_id = 0
    for group_item in data_group:
        thread_id = thread_id + 1
        args_get = [group_item] + ex_arg + [thread_id]
        thread = MyThread(func, args_get, thread_id)
        # thread = threading.Thread(target=t)
        threads.append(thread)

    for thread in threads:
        thread.daemon = True
        thread.start()

    for thread in threads:
        thread.join()

    result = []
    for item in threads:
        result = result + item.get_result()

    return result


def thread_run(data_list, thread_id):
	# print_info("init thread %s with %s pieces of data" % (thread_id, len(data_list)))
	result = []
	for line_text in data_list:
		result.append(clean_text(line_text))
	return data_list

def clean_text(line_text):
	res = ""
	for i in range(1000):
		re_str = "[\s+\.\!\/_,$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）》「」”》]+"
		res = re.sub(re_str,"",line_text)
	return res

if __name__ == '__main__':
	
	DATA_PATH = 'test_data.txt'
	DATA_PATH = 'test_data_all'
	print_info("data_init: %s" % DATA_PATH)

	data_list = []
	with open(DATA_PATH) as f:
		for line in f:
			data_list.append(line.strip())

	print_info("NO multi-thread BEGIN!!!!!")
	res = []
	for item in data_list:
		res.append(clean_text(item))
	print_info("NO multi-thread FINISH: %s" % len(res))

	print_info("MULTI-THREAD BEGIN!!!!!")
	result = multi_thread(data_list, thread_run)
	print_info("MULTI-THREAD FINISH: %s" % len(result))
	# multi_thread(data_list, clean_text)



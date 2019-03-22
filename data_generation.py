fout = open("test_data_all", "w")
with open("test_data.txt") as f:
    for line in f:
	    idx = 0
	    while idx < 1000000:
	        fout.write("%s%s" % (idx, line))
	        idx = idx + 1
fout.close()
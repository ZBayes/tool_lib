import csv
import xlwt

# csvReader读取文件
def csvRead(csvPath):
    csvFile = csv.reader(open(csvPath, 'r', encoding="utf8"))
    return csvFile

# csv写文件
def csvWrite(csvPath):
    csvFile = open(csvPath, 'w', encoding='utf8', newline='')
    writer = csv.writer(csvFile)
    return writer

# csv转化为excel
def csv_to_xlsx(readPath,writePath):
    with open(readPath, 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')  # 创建一个sheet表格
        l = 0
        for line in read:
            r = 0
            for i in line:
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1

        workbook.save(writePath)  # 保存Excel

readPathList=['resultlabelB1','resultlabelB5','resultlabelB10','resultlabelF1','resultlabelF5','resultlabelF10']
for readPath in readPathList:
    rPath='../data/%s.csv'%readPath
    wPath='../data/%s.xls'%readPath
    csv_to_xlsx(rPath,wPath)
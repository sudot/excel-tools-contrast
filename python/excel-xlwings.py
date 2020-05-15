import argparse
import os
from datetime import datetime

import psutil as psutil
import xlwings as xw

parser = argparse.ArgumentParser(description='执行此命令需要以下参数')
parser.add_argument('--file', '-f', help='要测试的文件', default='../data/small.xlsx')
args = parser.parse_args()

date = datetime.now()
wb = xw.Book(args.file)
open_date = datetime.now() - date

sheet = wb.sheets.active
rows = sheet.used_range.last_cell.row
for row in sheet.range('A1:A{rows}'.format(rows=rows)):
    print(row.value)
wb.close()

print(open_date, datetime.now() - date)

process = psutil.Process(os.getpid())
print('Used Memory:', process.memory_info().rss / 1024 / 1024, 'MB')

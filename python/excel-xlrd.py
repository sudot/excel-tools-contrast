import argparse
import os
from datetime import datetime

import psutil
from xlrd import open_workbook

parser = argparse.ArgumentParser(description='执行此命令需要以下参数')
parser.add_argument('--file', '-f', help='要测试的文件', default='../data/small.xlsx')
args = parser.parse_args()

date = datetime.now()
workbook = open_workbook(args.file)
open_date = datetime.now() - date

worksheet = workbook.sheet_by_index(0)
for rIndex in range(1, worksheet.nrows):
    print(worksheet.cell_value(rIndex, 0))

print(open_date, datetime.now() - date)

process = psutil.Process(os.getpid())
print('Used Memory:', process.memory_info().rss / 1024 / 1024, 'MB')

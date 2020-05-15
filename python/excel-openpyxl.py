import argparse
import os
from datetime import datetime

import psutil
from openpyxl import open

parser = argparse.ArgumentParser(description='执行此命令需要以下参数')
parser.add_argument('--file', '-f', help='要测试的文件', default='../data/small.xlsx')
args = parser.parse_args()

date = datetime.now()
workbook = open(args.file)
open_date = datetime.now() - date

sheet = workbook.active
for row in sheet['A1':'A{rows}'.format(rows=sheet.max_row)]:
    print(row[0].value)

print(open_date, datetime.now() - date)
process = psutil.Process(os.getpid())
print('Used Memory:', process.memory_info().rss / 1024 / 1024, 'MB')

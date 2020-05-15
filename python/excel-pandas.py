import argparse
import os
from datetime import datetime

import pandas
import psutil

parser = argparse.ArgumentParser(description='执行此命令需要以下参数')
parser.add_argument('--file', '-f', help='要测试的文件', default='../data/small.xlsx')
args = parser.parse_args()

date = datetime.now()
excel = pandas.read_excel(args.file)
open_date = datetime.now() - date

rows = excel.values
for index in range(0, len(rows)):
    print(rows[index][0])

print(open_date, datetime.now() - date)
process = psutil.Process(os.getpid())
print('Used Memory:', process.memory_info().rss / 1024 / 1024, 'MB')

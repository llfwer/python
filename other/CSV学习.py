# coding=utf-8
import csv

file_path = 'D:\\test.csv'


def write_list():
    with open(file_path, 'w', encoding='utf_8_sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['A', 'B', 'C', 'D'])
        w.writerow(['好', '好', '学', '习'])
        f.close()


def read_list():
    with open(file_path, 'r', encoding='utf_8_sig') as f:
        r = csv.reader(f)
        for i in r:
            print(i)
        f.close()


read_list()

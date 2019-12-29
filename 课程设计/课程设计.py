import matplotlib.pyplot as plt
import pandas

file_name = 'score.xlsx'


# 格式化输出列表
def print_list(lists):
    length = len(lists)
    for i in range(length):
        if i == length - 1:
            end = '\n'
        else:
            end = '\t\t'
        print(lists[i], end=end)


# 格式化输出行对象
def print_row(row):
    print(row['学号'], '\t\t', row['姓名'], '\t\t', row['英语'], '\t\t', row['高数'], '\t\t', row['C语言'], '\t\t', row['总分'])


# 读取文件数据
def read_data(file):
    data = pandas.read_excel(file)

    print_list(data.columns.values)

    columns = data.columns.size
    rows = len(data)

    print_list(data.loc[0].values)
    print_list(data.loc[1].values)
    print_list(data.loc[2].values)

    print('[{0}行 x {1}列]'.format(3, columns))

    print_list(data.columns.values)

    print_list(data.loc[rows - 2].values)
    print_list(data.loc[rows - 1].values)

    print('[{0}行 x {1}列]'.format(2, columns))

    print('数据读取成功')


# 数据处理(新增一列“总分”列，值为前三列成绩之和，写回excel)(注意:to_excel会删除其他的sheet，所以运行前请做好备份)
def handle_data(file):
    data = pandas.read_excel(file)

    data['总分'] = None

    for i in range(len(data)):
        item = data.loc[i]

        english = item.loc['英语']
        math = item.loc['高数']
        program = item.loc['C语言']

        data.loc[i, '总分'] = english + math + program

    data.to_excel(file, sheet_name='Sheet1', index=False, header=True)

    print('数据处理成功')


# 按总分排序(从高到低)输出(注意:排序之后若通过loc[index]来取值的话，还是按照原来的顺序输出的，所以这里换一种遍历方式)
def sort_total_score(file):
    data = pandas.read_excel(file)

    data.sort_values(by='总分', ascending=False, inplace=True)

    for index, row in data.iterrows():
        print_row(row)

    print('数据排序成功')


# 统计每门课最高分，最低分，平均分，并输出
def statistics_score(file):
    data = pandas.read_excel(file)

    max_english = 0
    min_english = 0
    max_math = 0
    min_math = 0
    max_program = 0
    min_program = 0

    for i in range(len(data)):
        item = data.loc[i]

        score_english = item.loc['英语']
        score_math = item.loc['高数']
        score_program = item.loc['C语言']

        if i == 0:
            max_english = score_english
            min_english = score_english
            max_math = score_math
            min_math = score_math
            max_program = score_program
            min_program = score_program

        if max_english < score_english:
            max_english = score_english
        if min_english > score_english:
            min_english = score_english

        if max_math < score_math:
            max_math = score_math
        if min_math > score_math:
            min_math = score_math

        if max_program < score_program:
            max_program = score_program
        if min_program > score_program:
            min_program = score_program

    print('英语-最高分:{0},最低分:{1}'.format(max_english, min_english))
    print('高数-最高分:{0},最低分:{1}'.format(max_math, min_math))
    print('C语言-最高分:{0},最低分:{1}'.format(max_program, min_program))


# 查找学生成绩信息
def find_student(file, name):
    data = pandas.read_excel(file)

    for i in range(len(data)):
        item = data.loc[i]

        if item.loc['姓名'] == name:
            print('查到到结果:')
            print_list(data.columns.values)
            print_list(item.values)
            return

    print('没有该同学')


# 画成绩分布图
def map_distribution(file):
    data = pandas.read_excel(file)

    list_english = [0 for x in range(0, 10)]
    list_math = [0 for x in range(0, 10)]
    list_program = [0 for x in range(0, 10)]

    for i in range(len(data)):
        item = data.loc[i]

        score_english = item.loc['英语']
        score_math = item.loc['高数']
        score_program = item.loc['C语言']

        if 0 <= score_english < 10:
            list_english[0] += 1
        if 10 <= score_english < 20:
            list_english[1] += 1
        if 20 <= score_english < 30:
            list_english[2] += 1
        if 30 <= score_english < 40:
            list_english[3] += 1
        if 40 <= score_english < 50:
            list_english[4] += 1
        if 50 <= score_english < 60:
            list_english[5] += 1
        if 60 <= score_english < 70:
            list_english[6] += 1
        if 70 <= score_english < 80:
            list_english[7] += 1
        if 80 <= score_english < 90:
            list_english[8] += 1
        if 90 <= score_english <= 100:
            list_english[9] += 1

        if 0 <= score_math < 10:
            list_math[0] += 1
        if 10 <= score_math < 20:
            list_math[1] += 1
        if 20 <= score_math < 30:
            list_math[2] += 1
        if 30 <= score_math < 40:
            list_math[3] += 1
        if 40 <= score_math < 50:
            list_math[4] += 1
        if 50 <= score_math < 60:
            list_math[5] += 1
        if 60 <= score_math < 70:
            list_math[6] += 1
        if 70 <= score_math < 80:
            list_math[7] += 1
        if 80 <= score_math < 90:
            list_math[8] += 1
        if 90 <= score_math <= 100:
            list_math[9] += 1

        if 0 <= score_program < 10:
            list_program[0] += 1
        if 10 <= score_program < 20:
            list_program[1] += 1
        if 20 <= score_program < 30:
            list_program[2] += 1
        if 30 <= score_program < 40:
            list_program[3] += 1
        if 40 <= score_program < 50:
            list_program[4] += 1
        if 50 <= score_program < 60:
            list_program[5] += 1
        if 60 <= score_program < 70:
            list_program[6] += 1
        if 70 <= score_program < 80:
            list_program[7] += 1
        if 80 <= score_program < 90:
            list_program[8] += 1
        if 90 <= score_program <= 100:
            list_program[9] += 1

    name_list = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100']

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure()
    plt.bar(name_list, list_english)
    plt.title('英语成绩分布图')
    plt.xlabel('分数段')
    plt.ylabel('人数')

    plt.figure()
    plt.bar(name_list, list_math)
    plt.title('高数成绩分布图')
    plt.xlabel('分数段')
    plt.ylabel('人数')

    plt.figure()
    plt.bar(name_list, list_program)
    plt.title('C语言成绩分布图')
    plt.xlabel('分数段')
    plt.ylabel('人数')

    plt.show()

    print(list_english)
    print(list_math)
    print(list_program)


if __name__ == '__main__':
    map_distribution(file_name)

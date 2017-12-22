import datetime
import fileinput
import os

path = r'C:\Users\John Smith\Desktop\人生回溯局.txt'


# 大文件读取方式一
def read_large_txt1():
    index = 1
    for line in fileinput.input(path):
        print(index, ' : ', line)
        index = index + 1


# 大文件读取方式二
def read_large_txt2():
    index = 1
    with open(path, 'r') as f:
        for line in f:
            print(index, ' : ', line)
            index = index + 1
        f.close()


# 文本处理去除空行
def clear_empty_line():
    file_path, full_name = os.path.split(path)
    file_name, file_ext = os.path.splitext(full_name)
    out = open(os.path.join(file_path, file_name + '_去除空行' + file_ext), 'w')
    for line in fileinput.input(path):
        if line == '\n':
            continue
        out.write(line)
    out.close()


# 文本处理去除空行、替换广告
def clear_empty_ad():
    start = datetime.datetime.now()
    file_path, full_name = os.path.split(path)
    file_name, file_ext = os.path.splitext(full_name)
    target = file_name + '_处理' + file_ext
    out = open(os.path.join(file_path, target), 'w')
    ad_list = [
        '天才壹秒記住『新♂無♂錯÷小△說→網wWw。XqUleDu。Com』，為您提供精彩小說閱讀。',
        '【新↑無→錯△小↓說。網Ww W.xQUlEDu.coM】',
        '【新↑無。錯△小↓說△網W wW.xQUlEDu.coM】',
        '天才壹秒記住『新♂無♂錯÷小△說→網wWw。XqUleDu。Com』，為您提供精彩小說閱讀。',
        '手機用戶請浏覽m.xquledu.com閱讀，更優質的閱讀體驗。'
    ]
    for line in fileinput.input(path):
        if line == '\n':
            continue
        for ad in ad_list:
            if ad in line:
                line = line.replace(ad, '')
        out.write(line)
    out.close()
    end = datetime.datetime.now()
    print((end - start).seconds)


# 文本处理去除空行、替换广告
def clear(path_param):
    file_path, full_name = os.path.split(path_param)
    target_path = os.path.join(file_path, 'result')
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    out = open(os.path.join(target_path, full_name), 'w')
    ad_list = [
        '天才壹秒記住『新♂無♂錯÷小△說→網wWw。XqUleDu。Com』，為您提供精彩小說閱讀。',
        '【新↑無→錯△小↓說。網Ww W.xQUlEDu.coM】',
        '【新↑無。錯△小↓說△網W wW.xQUlEDu.coM】',
        '天才壹秒記住『新♂無♂錯÷小△說→網wWw。XqUleDu。Com』，為您提供精彩小說閱讀。',
        '手機用戶請浏覽m.xquledu.com閱讀，更優質的閱讀體驗。'
    ]
    for line in fileinput.input(path_param):
        if line == '\n':
            continue
        for ad in ad_list:
            if ad in line:
                line = line.replace(ad, '')
        out.write(line)
    out.close()


clear(r'C:\Users\John Smith\Desktop\牧神记(第三百九十五章 殿下生猛).txt')
clear(r'C:\Users\John Smith\Desktop\疯骑士的宇宙时代(第二百零五章 剧中剧).txt')
clear(r'C:\Users\John Smith\Desktop\你管这也叫金手指(第四十五章 伯伦特与伊迪).txt')

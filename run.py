def Writer():
    print('随机点名程序(made by wsr)')
Writer()

import guide
with open(r'.\data\name_base.txt', 'r', encoding='utf-8') as f:
    g = f.read()
    if g != '':
        name_base = g
    else:
        guide.name_input()
        with open(r'.\data\name_base.txt', 'r', encoding='utf-8') as f:
            g = f.read()

import random
import time

name_base = eval(g)
title = 'name_base>>>'
old_list = name_base[:]
r = None

def get1():
    global r, name_base
    r = 'get'
    return random.choice(name_base)

def gets(num):
    global r, name_base
    r = 'get'
    if len(name_base) >= num:
        return random.sample(name_base, k=num)
    else:
        return '没有足够的名字'

def add_name(name):
    global r, name_base, old_list
    r = 'add'
    old_list = name_base[:]
    name_base.append(name)

def add_names(name_list):
    global r, name_base, old_list
    r = 'add'
    old_list = name_base[:]
    name_base.extend(name_list)

def del_name(name):
    global r, name_base, old_list
    r = 'del'
    old_list = name_base[:]
    try:
        name_base.remove(name)
    except ValueError as e:
        guide.error_log(e)
        print(str(name) + 'is not exist in' + str(name_base))

def del_names(name_list):
    global r, name_base, old_list
    r = 'del'
    old_list = name_base[:]
    for name in name_list:
        try:
            name_base.remove(name)
        except ValueError as e:
            guide.error_log(e)
            print(str(name) + 'is not exist in' + str(name_base))

def save():
    global r, name_base, title
    r = 'save'
    i_list = []
    for i in title:
        i_list.append(i)
    list = i_list[:-3]
    if list == 'name_base':
        with open(r'.\data\name_base.txt', 'w', encoding='utf-8') as f:
            f.write(str(name_base))
    else:
        with open('.\\data\\group_' + list[0] + '.txt', 'w', encoding='utf-8') as f:
            f.write(str(name_base))

def new_group(group_name):
    global r, name_base, chosed
    print('新建分组：' + group_name)
    r = 'new_group'
    guide.new_group(group_name)
    chosed = False

chosed = False
while True:
    with open('.\\data\\numbers.txt', 'r', encoding='utf-8') as f:
        n = f.read()
        n_int = int(n)

    if n_int == 1 and chosed == False:
        title = 'name_base>>>'
        p = input(title)
        try:
            q = eval(p)
        except Exception as e:
            guide.error_log(e)
            q = e
        print(q)

    elif n_int > 1 and chosed == False:
        with open('.\\data\\group_names.txt', 'r', encoding='utf-8') as f:
            g = f.read().splitlines()
        g = list(set(g))
        g.append('name_base')
        h = input('chose group here: ' + str(g))
        while h not in g:
            print(h + ' is not exist in' + str(g))
            h = input('chose group here: ' + str(g))
        title = h + '>>>'
        chosed = True
        continue

    if chosed == True:
        p = input(title)
        try:
            q = eval(p)
        except Exception as e:
            guide.error_log(e)
            q = e
        print(q)

    if r == 'get':
        with open(r'.\log\get_log_' + str(time.time()) + '.txt', 'w', encoding='utf-8') as f:
            f.write('from ' + str(name_base) + ' get names: ' + str(q))

    elif r == 'add':
        with open(r'.\log\add_log_' + str(time.time()) + '.txt', 'w', encoding='utf-8') as f:
            f.write('add name: ' + str(p) + ' to ' + str(old_list) + ' , now it becomes:' + str(name_base))

    elif r == 'del':
        with open(r'.\log\del_log_' + str(time.time()) + '.txt', 'w', encoding='utf-8') as f:
            f.write('del name: ' + str(p) + ' to ' + str(old_list) + ' , now it becomes:' + str(name_base))

    elif r == 'save':
        with open(r'.\log\save_log_' + str(time.time()) + '.txt', 'w', encoding='utf-8') as f:
            f.write('save data:' + str(name_base))

    elif r == 'new_group':
        with open(r'.\log\group_log_' + str(time.time()) + '.txt', 'w', encoding='utf-8') as f:
            f.write('create new group: ' + str(p))

    else:
        with open(r'.\log\other_log_' + str(time.time()) + '.txt', 'w', encoding='utf-8') as f:
            f.write('operate:\n' + 'input:' + str(p) + '\noutput:' + str(q))

    r = None

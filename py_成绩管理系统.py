# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:48:38 2021

@author: Nana
"""
""
import sys
import operator


def instruct():
    print('\n')
    print('*********************')
    print('欢迎进入成绩管理系统！')
    print('1、添加学生信息')
    print('2、删除学生信息')
    print('3、修改学生信息')
    print('4、查找学生信息')
    print('5、查看全部学生信息')
    print('6、按指定操作进行排序')
    print('7、退出成绩管理系统')
    print("********************")


def add(students):  # 增
    a = input('请输入你想添加的姓名:')
    b = input('请输入学号:')
    c = input('请输入数学成绩:')
    d = input('请输入英语成绩：')
    student = {}
    student = {'姓名': a, '学号': b, '数学成绩': c, '英语成绩': d}
    students.append(student)
    print('添加成功！')


def delete(students):  # 删
    flag = 0
    want_del = input('请输入你想删除的学生姓名或学号：')
    for i in students:
        if i['姓名'] == want_del or i['学号'] == want_del:
            flag = 1
            a = students.index(i)
            students.pop(a)
            print('删除成功！')
    if flag == 0:
        print('没有找到您想删除的学生信息!')


def change(students):  # 改
    want_chage = input('请输入你想修改的学生的姓名或者学号：')
    flag = 0
    for i in students:
        flag = 2
        if i['姓名'] == want_chage or i['学号'] == want_chage:
            wan_chos = input("请输入您想修改的学生信息：（姓名,学号，数学成绩，英语成绩）")
            for j in i:
                if j == wan_chos:
                    new_value = input('请输入修改后的值：')
                    i[j] = new_value
                    flag = 1
                    print('修改学生信息成功！')
    if flag == 0:
        print('您想要修改的学生不存在')
    elif flag != 1:
        print('修改学生信息不成功！')


def find(students):  # 查
    flag = 0
    the_find = input('请输入你想查找的姓名或学号：')
    for i in students:
        if i['姓名'] == the_find or i['学号'] == the_find:
            flag = 1
            for j in i:
                print("%s为：%s" % (j, i[j]))
    if flag == 0:
        print('没有找到该学生！')


def findAll(students):  # 打印所有
    count = 1
    for i in students:
        print('第%d个学生的信息为：' % count)
        for j in i:
            print(j + ": " + i[j])
        count += 1


def sort(students):
    flag = 0
    a = input('您想以什么顺序进行排序？(姓名、学号、数学成绩、英语成绩)')
    for i in students:
        for j in i:
            if a == j:
                flag = 1
    if flag == 1:
        count = 1
        print('排序后的结果为：')
        sorted_stu = sorted(students, key=operator.itemgetter(a))
        for i in sorted_stu:
            print('按%s排序%d名为：' % (a, count))
            for j in i:
                print(j + ": " + i[j])
            count += 1
    else:
        print('您的输入有误！')


students = []

while True:
    instruct()
    a = int(input('请输入你想要选择的序号！'))
    if a == 7:
        print("退出学生管理系统成功！")
        sys.exit(0)
    elif a == 1:
        add(students)
    elif a == 2:
        delete(students)
    elif a == 3:
        change(students)
    elif a == 4:
        find(students)
    elif a == 5:
        findAll(students)
    elif a == 6:
        sort(students)
    elif a >= 8 or a < 0:
        print('illegal input')



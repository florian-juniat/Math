#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## 105
## File description:
## 105
##

import math
import sys
from sys import argv, exit
import os.path

tab = [];
len_n = 0;

for arg in sys.argv:
    if (len_n != 0):
        tab.append(arg);
    len_n = len_n + 1;

if (len_n < 3):
    exit(84)
if (len_n == 3):
    try:
        a = int(argv[2])
    except ValueError:
        exit(84)
if (len_n > 4):
    exit(84)

def create_mat(x, y, n):
    ret = []
    for i in range(y):
        one = []
        for j in range(x):
            one.append(n)
        ret.append(one)
    return (ret)

def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if (j != (len(mat[i]) - 1)):
                print(str(mat[i][j]) + " ", end = '')
            else:
                print(mat[i][j])

def mult_mat(mat1, mat2):
    ret = create_mat(len(mat1), len(mat1), 0)
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            nb = 0
            for k in range(len(mat1)):
                nb += mat1[i][k] * mat2[k][j]
            ret[i][j] = nb
    return (ret)





def parse(filll):
    file = filll.split("\n", -1)
    str = []
    for i in range(len(file)):
        str.append((file[i]).split(" is friends with ", -1))
    name = []
    for i in range(len(str)):
        if (len(str[i][0]) > 0 and (str[i][0]) not in name):
            name.append(str[i][0])
        if (len(str[i]) > 1 and (str[i][1]) not in name):
            name.append(str[i][1])
    name.sort()
    mat = create_mat(len(name), len(name), 0)
    for i in range(len(str)):
        if (len(str[i][0]) < 1):
            break
        x = name.index(str[i][0])
        y = name.index(str[i][1])
        mat[x][y] = 1
        mat[y][x] = 1
    return name, mat

def main(file, argv):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        exit(84)
    str = f.read()
    name, mat = parse(str)
    if (len_n == 3):
        for i in range(len(name)):
            print(name[i])
        print()
        print_mat(mat)
        print()
        ret = mat.copy()
        for i in range(1):
            ret = mult_mat(ret, mat)
        print_mat(ret)




if __name__ == "__main__":
    main(argv[1], argv)

#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## 304pacman.py
## File description:
## pacman
##

import math
import sys
from sys import argv, exit
import os.path

tab = [];
ac = 0;

for arg in sys.argv:
    if (ac != 0):
        tab.append(arg);
    ac = ac + 1;

if (ac != 4):
    exit(84)

try:
    f = open(argv[1], "r")
except FileNotFoundError:
    exit(84)

file = f.read()

if (len(file) == 0):
    exit(84)

file = file.split("\n")

while (len(file[len(file) - 1]) == 0):
    del file[-1]

def error(file, char_wall, char_empty):
    if (len(char_wall) != 1 or len(char_empty) != 1):
        exit(84)
    if (char_wall == char_empty):
        exit(84)
    if (len(file[0]) < 1):
        exit(84)
    for i in range(len(file)):
        if (len(file[i]) != len(file[0])):
            exit(84)
    count_ghost = 0
    count_pac = 0
    for i in range(len(file)):
        for j in range(len(file[i])):
            if (file[i][j] == 'F'):
                count_ghost += 1
            if (file[i][j] == 'P'):
                count_pac += 1
    if (count_ghost != 1 or count_pac != 1):
        exit(84)

def get_x_y(file):
    for i in range(len(file)):
        for j in range(len(file[i])):
            if (file[i][j] == 'F'):
                return (j, i)

def create_work_map(file):
    ret = []
    wall = []
    for i in range(len(file[0]) + 2):
        wall.append(-2)
    ret.append(wall)
    for i in range(len(file)):
        ret_two = []
        ret_two.append(-2)
        for j in range(len(file[i])):
            if (file[i][j] == '0'):
                ret_two.append(-1)
            elif (file[i][j] == '1'):
                ret_two.append(-2)
            elif (file[i][j] == 'P'):
                ret_two.append(-9)
            else:
                ret_two.append(0)
        ret_two.append(-2)
        ret.append(ret_two)
    ret.append(wall)
    return (ret)

def create_node(x, y, nb):
    return [x, y, nb]


def main(file, char_wall, char_empty):
    error(file, char_wall, char_empty)
    x, y = get_x_y(file)
    work = create_work_map(file)

    find = 0
    nb_pass = 0
    node = []
    node.append(create_node(x + 1, y + 1, 0))
    while (find == 0 and nb_pass < len(work) * len(work)):
        node2 = []
        for i in range(len(node)):
            x = node[i][0]
            y = node[i][1]
            nb = node[i][2]
            if (work[y - 1][x] == -9):
                find = 1
                break;
            if (work[y - 1][x] == -1 or work[y - 1][x] > nb + 1):
                work[y - 1][x] = nb + 1
                node2.append(create_node(x, y - 1, nb + 1))
            if (work[y][x + 1] == -9):
                find = 1
                break;
            if (work[y][x + 1] == -1 or work[y][x + 1] > nb + 1):
                work[y][x + 1] = nb + 1
                node2.append(create_node(x + 1, y, nb + 1))
            if (work[y + 1][x] == -9):
                find = 1
                break;
            if (work[y + 1][x] == -1 or work[y + 1][x] > nb + 1):
                work[y + 1][x] = nb + 1
                node2.append(create_node(x, y + 1, nb + 1))
            if (work[y][x - 1] == -9):
                find = 1
                break;
            if (work[y][x - 1] == -1 or work[y][x - 1] > nb + 1):
                work[y][x - 1] = nb + 1
                node2.append(create_node(x - 1, y, nb + 1))
        for i in range(len(node2)):
            node.append(node2[i])
        nb_pass += 1
    ret = []
    for i in range(len(file)):
        ret_two = []
        for j in range(len(file[i])):
            if (work[i + 1][j + 1] > 0):
                ret_two.append(str(work[i + 1][j + 1] % 10))
            elif (file[i][j] == '0'):
                ret_two.append(char_empty)
            elif (file[i][j] == '1'):
                ret_two.append(char_wall)
            else:
                ret_two.append(file[i][j])
        ret.append(ret_two)
    for i in range(len(ret)):
        for j in range(len(ret[i])):
            print(ret[i][j], end = '')
        print()



if __name__ == "__main__":
    main(file, argv[2], argv[3])

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

if (ac != 2):
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

def check_first(tab):
    ret = []
    for i in range(len(tab)):
        ret.append(tab[i][0])
    x = ret[0]
    del ret[0]
    while (len(ret) != 0):
        if x in ret:
            exit(84)
        x = ret[0]
        del ret[0]

def check_third(tab):
    for i in range(len(tab)):
        try:
            a = int(tab[i][2])
        except ValueError:
            exit(84)

def check_four(tab):
    ret = []
    for i in range(len(tab)):
        ret.append(tab[i][0])
    check = 0
    for i  in range(len(tab)):
        if (len(tab[i]) > 3):
            for j in range(3, len(tab[i])):
                if tab[i][j] not in ret:
                    exit(84)
        else:
            check = 1
    if (check == 0):
        exit(84)
            

def error_case(tab):
    for i in range(len(tab)):
        if (len(tab[i]) < 3):
            exit(84)
    check_first(tab)
    check_third(tab)
    check_four(tab)


def transform_tab(tab):
    ret = []
    for i in range(len(tab)):
        ret2 = []
        ret2.append(tab[i][0])
        ret2.append(tab[i][2])
        ret3 = []
        if (len(tab[i]) > 3):
            for j in range(3, len(tab[i])):
                ret3.append(tab[i][j])
        ret2.append(ret3)
        ret.append(ret2)
    return (ret)


def total(name, tab):
    index = -1
    for i in range(len(tab)):
        if (tab[i][0] == name):
            index = i
    if (index == -1):
        return (-1)
    if (len(tab[index][2]) == 0):
        return (int(tab[index][1]))
    ret = []
    for i in range(len(tab[index][2])):
        ret.append(total(tab[index][2][i], tab))
    max = -1
    for i in range(len(ret)):
        if (ret[i] > max):
            max = ret[i]
    return (max + int(tab[index][1]))


def get_total(tab):
    ret = []
    for i in range(len(tab)):
        try:
            ret.append(total(tab[i][0], tab))
        except RecursionError as re:
            exit(84)
    max = -1
    for i in range(len(ret)):
        if (ret[i] > max):
            max = ret[i]
    return max

def get_begin(tab, tot_ref):
    ret = []
    for i in range(len(tab)):
        x = 0
        tab[i][3] = total(tab[i][0], tab) - int(tab[i][1])
        tot = tot_ref
        while (tot == tot_ref):
            tab[i][1] = str(int(tab[i][1]) + 1)
            tot = get_total(tab)
            x += 1
        tab[i][1] = str(int(tab[i][1]) - x)
        x -= 1
        tab[i][4] = x
    tab.sort()
    for i in range(len(tab)):
        for j in range(len(tab)):
            if (tab[i][3] < tab[j][3]):
                inter = tab[i]
                tab[i] = tab[j]
                tab[j] = inter
            if (tab[i][3] == tab[j][3] and tab[j][4] > tab[i][4]):
                inter = tab[i]
                tab[i] = tab[j]
                tab[j] = inter
    for i in range(len(tab)):
        if (tab[i][4] == 0):
            print(str(tab[i][0]) + " must begin at t=" + str(tab[i][3]))
        else:
            print(str(tab[i][0]) + " must begin between t=" + str(tab[i][3])
                    + " and t=" + str(tab[i][3] + tab[i][4]))
    return (tab)


def main(file):
    error_case(file)
    file = transform_tab(file)
    tot = get_total(file)
    print("Total duration of construction: " + str(tot) + " weeks")
    for i in range(len(file)):
        file[i].append(0)
        file[i].append(0)
        #print(file[i])
    #print("-------")
    print()
    tab = get_begin(file, tot)
    print()
    for i in range(len(tab)):
        print(tab[i][0] + "\t(" + str(tab[i][4]) + ")\t", end =  '')
        for j in range(tab[i][3]):
            print(" ", end = '')
        for j in range(int(tab[i][1])):
            print("=", end = '')
        print()


file2 = []
for i in range(len(file)):
    file2.append(file[i].split(";", -1))


main(file2)

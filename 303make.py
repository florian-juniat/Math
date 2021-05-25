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
i = 0;

for arg in sys.argv:
    if (i != 0):
        tab.append(arg);
    i = i + 1;

def error(ac, av):
    if (ac != 2 and ac != 3):
        return (1)
    exist = os.path.exists(av[1])
    if (exist):
        return (0)
    else:
        return (1)
    return (0)

if (i == 2):
    if ("-h" in tab[0]):
        print("USAGE")
        print("    ./303make makefile [file]")
        print()
        print("DESCRIPTION")
        print("    makefile       name of the makefile")
        print("    file           name of the recently modified file")

def splitMyLine(myChaine):
    rec = ""
    for i in range (len(myChaine)):
        #if (myChaine[i] != ':'):
        rec += myChaine[i]
    rec = rec.split(" ")
    return rec

def searchAllWords(mySplit, first, second):
    mySplit.reverse()
    rec = []
    recTwo = []
    cop = ""
    trans = ""
    i = 0
    while i < len(mySplit) - 1:
        cop = splitMyLine(mySplit[i])
        j = len(cop) - 1
        while j >= 0:
            if (any(cop[j] in s for s in rec)):
                rec = rec
            else:
                if (cop[j][len(cop[j]) - 2] == '.' or cop[j][len(cop[j]) - 1] == ':'):
                    rec.append(cop[j])
            j -= 1
        i += 1
    for i in range (len(rec)):
        for j in range (len(rec[i])):
           if (rec[i][j] != ':'):
               trans += rec[i][j]
        rec[i] = trans
        trans = ""
    return rec

def diviseTwo(first, second, mySplit):
    for i in range (len(mySplit)):
        if (i % 2 == 0):
            first.append(mySplit[i])
        else:
            second.append(mySplit[i])

def sousPoint(myString):
    rec = ""

    for i in range (len(myString)):
        if (myString[i] != ':'):
            rec += myString[i]
    return rec

def checkNumber(first, info):
    counter = 0
    j = 0

    for i in range(len(first)):
        rec = splitMyLine(first[i])
        while j < len(rec):
            if (info == rec[j]):
                counter += 1
            j += 1
        j = 0
    return counter

def theHeartOfTheBeast(first, info):
    counter = checkNumber(first, info)
    j = 1
    comp = 0
    check = 0
    if (counter != comp):
        print(info + " -> ", end='')
    else:
        print(info)
    if (info[len(info) - 2] == '.'):
        for i in range (len(first)):
            rec = splitMyLine(first[i])
            while j < len(rec):
                if (info == rec[j] and check == 0):
                    check = 1
                    theHeartOfTheBeast(first, sousPoint(rec[0]))
                j += 1
            j = 1

def theHeartOfTheBeastTwo(first, second, info, add):
    j = 1
    check = 0

    for i in range(len(first)):
        rec = splitMyLine(first[i])
        while j < len(rec):
            if (info == rec[j] and check == 0):
                check = 1
                add.append(second[i])
                theHeartOfTheBeastTwo(first, second, sousPoint(rec[0]), add)
            j += 1
        j = 1
    return add

def newSplit(first, info, number):
    myNewSplit = []
    counter = 0
    value = 0
    j = 0

    for i in range(len(first)):
        rec = splitMyLine(first[i])
        while (j < len(rec)):
            if (info == rec[j]):
                counter += 1
                if (counter == number):
                    value = i
            j += 1
        j = 0

    if (number == 1):
        value = 0
    while value < len(first):
        myNewSplit.append(first[value])
        value += 1
    return myNewSplit

def checkList(second, rec):
    tri = []
    lastTri = []

    for i in range (len(rec)):
        if (any(rec[i] in s for s in tri)):
            tri = tri
        else:
            tri.append(rec[i])
    for i in range (len(second)):
        if (any(second[i] in s for s in tri)):
            print(second[i])

def repertiture(mySplit, first, second, info):
    first.reverse()
    k = 0

    print()
    while (k < len(info)):
        j = 0
        while (j < checkNumber(first, info[k])):
            theHeartOfTheBeast(newSplit(first, info[k], j + 1), info[k])
            j += 1
        k += 1

def errorEntre(first, key):
    k = 0
    check = 0

    for i in range (len(first)):
        rec = splitMyLine(first[i])
        while k < len(rec):
            if (sousPoint(rec[k]) == key):
                check = 1
            k += 1
        k = 0
    if (check == 0):
        exit(84)
    if (key[len(key) - 2] != '.'):
        print()
        exit(0)

def repertitureTwo(mySplit, first, second, info, key):
    first.reverse()
    second.reverse()
    rec = []
    j = 0
    
    errorEntre(first, key)
    while (j < checkNumber(first, key)):
        rec = theHeartOfTheBeastTwo(newSplit(first, key, j + 1), second, key, rec)
        j += 1
    rec = checkList(second, rec)

def parse(start):
    start_two_point = []
    for i in range(len(start)):
        if (":" in start[i]):
            start_two_point.append(start[i])
    ret = []
    name = []
    for i in range(len(start_two_point)):
        one_element = []
        sp_point = start_two_point[i].split(":")
        if (sp_point[0] not in name):
            name.append(sp_point[0])
        one_element.append(sp_point[0])
        second_element = []
        two = sp_point[1].split(" ")
        for j in range(len(two)):
            if (len(two[j]) != 0):
                second_element.append(two[j])
                if (two[j] not in name):
                    name.append(two[j])
        one_element.append(second_element)
        ret.append(one_element)
    name.sort()
    return ret, name

def mat_n(n):
    ret = []
    for i in range(n):
        sec = []
        for j in range(n):
            sec.append(0)
        ret.append(sec)
    return (ret)

def create_mat(tab, name):
    mat = mat_n(len(name))
    for i in range(len(tab)):
        x = name.index(tab[i][0])
        for j in range(len(tab[i][1])):
            y = name.index(tab[i][1][j])
            mat[y][x] = 1
    for i in range(len(mat)):
        print("[", end='')
        for j in range(len(mat)):
            if (j != len(mat) - 1):
                print(str(mat[i][j]) + " ", end = '')
            else:
                print(str(mat[i][j]), end ='')
        print("]")

def main(Makefile, Key):
    f = open(Makefile, "r")
    myList = f.read()
    mySplit = myList.split("\n")

    while (len(mySplit[len(mySplit) - 1]) == 0):
        del mySplit[-1]
    j = 0
    first = []
    second = []
    for i in range (len(mySplit) - 1):
        if (mySplit[j] == ""):
            mySplit.pop(j)
            j -= 1
        j += 1
    diviseTwo(first, second, mySplit)
    if (Key == ""):
        tab, name = parse(mySplit)
        create_mat(tab, name)
        repertiture(mySplit, first, second, searchAllWords(mySplit, first, second))
    else:
        repertitureTwo(mySplit, first, second, searchAllWords(mySplit, first, second), Key)

if __name__ == "__main__":
    if (error(len(argv), argv)):
        exit(84)
    if (len(argv) == 2):
        main(argv[1], "")
    else:
        main(argv[1], argv[2])











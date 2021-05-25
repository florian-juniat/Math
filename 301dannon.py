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


if (i == 2):
    if ("-h" in tab[0]):
        print("USAGE")
        print("    ./301dannon file")
        print()
        print("DESCRIPTION")
        print("    file       file that contains the numbers to be sorted, separated by spaces")

def checkError(myList):
    inter = myList.split("\n")
    myChain = (inter[0]).split(" ")
    rec = ""

    for i in range(len(myChain)):
        rec = ""
        for j in range(0, len(myChain[i])):
            if (myChain[i][j] != '.' and myChain[i][j] != '-'):
                rec = rec + myChain[i][j]
        if rec.isdigit() == False:
            exit(84)

def error(ac, av):
    if (ac != 2):
        return (1)
    exist = os.path.exists(av[1])
    if (exist):
        return (0)
    else:
        return (1)
    return (0)

def selection(myChain2):
    myChain = []
    for i in range(len(myChain2)):
        myChain.append(myChain2[i])
    count = 0
    jMin = 0
    rec = 0

    for i in range(len(myChain)):
        jMin = i
        for j in range(i + 1, len(myChain)):
            if myChain[jMin] > myChain[j]:
                jMin = j
            count += 1
        rec = myChain[jMin]
        myChain[jMin] = myChain[i]
        myChain[i] = rec
    
    return (str(count))


def insertion(myChain2):
    myChain = []
    for i in range(len(myChain2)):
        myChain.append(myChain2[i])
    list = []
    count = 0
    for i in range(len(myChain)):
        if (len(list) == 0):
            list.append(myChain[i])
        else:
            k = 0
            stop = 0
            while (k < len(list) and stop == 0):
                count = count + 1
                if (list[k] > myChain[i]):
                    list.insert(k, myChain[i])
                    stop = 1
                if (stop == 0):
                    k = k + 1
            if (k == len(list)):
                list.append(myChain[i])
    return str(count)


def bubble(myChain2):
    myChain = []
    for i in range(len(myChain2)):
        myChain.append(myChain2[i])
    count = 0
    rec = 0

    for i in range(len(myChain)):
        for j in range(len(myChain) - i - 1):
            if myChain[j] > myChain[j + 1]:
                rec = myChain[j]
                myChain[j] = myChain[j + 1]
                myChain[j + 1] = rec
            count += 1

    return (str(count))


count_quick = [0]

def quick(arr, min, max): 
    if (min < max):
        nb = min - 1
        for j in range(min, max):
            count_quick[0] += 1
            if (arr[j] < arr[max]):
                nb += 1
                inter = arr[nb]
                arr[nb] = arr[j]
                arr[j] = inter
        inter2 = arr[nb + 1]
        arr[nb + 1] = arr[max]
        arr[max] = inter2
        nb += 1
        quick(arr, min, nb - 1)
        quick(arr, nb + 1, max)

count_merge = [0]

def merge_sort(left, right):
    ret = []
    i = 0
    j = 0
    while (i < len(left) and j < len(right)):
        count_merge[0] += 1
        if (left[i] < right[j] or j == len(right)):
            ret.append(left[i])
            i = i + 1
        else:
            ret.append(right[j])
            j = j + 1
    while (i < len(left) or j < len(right)):
        if (i < len(left)):
            ret.append(left[i])
            i += 1
        if (j < len(right)):
            ret.append(right[j])
            j += 1
    return (ret)

def merge(arr):
    if (len(arr) > 1):
        mid = int(len(arr) / 2)
        arr_copy = arr.copy()
        left = arr_copy[:mid]
        right = arr_copy[mid:]
        one = merge(left)
        two = merge(right)
        last = merge_sort(one, two)
        return (last)
    else:
        return (arr)

def parser(myList):
    rec = ""
    check = 0

    for i in range(len(myList)):
        if myList[i].isdigit() == True or (myList[i] == '.' and myList[i + 1].isdigit() == True and myList[i - 1].isdigit() == True) or (myList[i] == '-' and myList[i + 1].isdigit() == True):
            if check == 1 and len(rec) > 0:
                rec = rec + " "
            rec = rec + myList[i]
            check = 0
        else:
            check = 1
    return rec


def myPrint(myList) :
    myChain = myList.split(" ")
    myChain = list(map(float, myChain))
    test = myChain.copy()
    merg = myChain.copy()
    if (len(myChain) <= 1):
        print(str(len(myChain)) + " element")
    else:
        print(str(len(myChain)) + " elements")
    print("Selection sort: " + selection(myChain) + " comparisons")
    print("Insertion sort: " + insertion(myChain) + " comparisons")
    print("Bubble sort: " + bubble(myChain) + " comparisons")
    quick(test, 0, len(myChain) - 1)
    print("Quicksort: " + str(count_quick[0]) + " comparisons")
    merg = merge(merg)
    print("Merge sort: " + str(count_merge[0]) + " comparisons")


def main(file):
    f = open(file, "r")
    myList = f.read()
    myList = parser(myList)
    checkError(myList)
    myPrint(myList)

if __name__ == "__main__":
    if (error(len(argv), argv)):
        exit(84)
    main(argv[1])

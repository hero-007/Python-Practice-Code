#!/bin/python3

import sys

def fac(num):
    fac = 1
    for i in range(2,num+1,1):
        fac *= i
    return fac

def combination(n,r):
    ncr = fac(n)/(fac(r)*fac(n-r))
    return ncr

def otp(atr):
    finl_list = []
    for i in atr:
        c=0
        if len(finl_list)!=0:
            for j in finl_list:
                if i[0] in j:
                    j.append(i[1])
                    c = 1
                    break
            if c!=1:
                finl_list.append([i[0],i[1]])
                c = 0
        else:
            finl_list.append(i)
    return finl_list

def finl_ans (list_comp):
    asum = 0
    
    for i in range(0,len(list_comp),1):
        for j in range(i+1,len(list_comp),1):
            c1 = combination(len(list_comp[i]),1)
            c2 = combination(len(list_comp[j]),1)
            asum += (c1*c2)
    return asum


def journeyToMoon(n, astronaut):
    finl_list_otp = otp(astronaut)
    list_done = []
    for j in range(0,n,1):
        c = 0
        for i in finl_list_otp:
            if j in i:
                c = 1
                break
        if c!= 1:
            list_done.append([j])

    for k in finl_list_otp:
        list_done.append(k)
    ans = finl_ans(list_done)
    return ans
    

if __name__ == "__main__":
    n, p = input().strip().split(' ')
    n, p = [int(n), int(p)]
    astronaut = []
    for astronaut_i in range(p):
       astronaut_t = [int(astronaut_temp) for astronaut_temp in input().strip().split(' ')]
       astronaut.append(astronaut_t)
    result = journeyToMoon(n, astronaut)
    print(int(result))

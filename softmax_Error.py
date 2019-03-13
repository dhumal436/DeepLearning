# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:42:48 2019

@author: shubhshubham
"""

import numpy as np

L=[1,2,3,4,5]

def softmaxL(l):
    expo=np.exp(l)
    sumExpo=sum(expo)
    result=[]
    for i in expo:
        result.append(np.divide(i*1.0,sumExpo))
    return result

print(softmaxL(L))
    
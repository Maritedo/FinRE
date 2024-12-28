#!/usr/bin/env python
#encoding=utf-8
import sys
import os
import json

def get_results(filename):
    res=[]
    with open(filename,"r") as fin:
        for line in fin:
            data=json.loads(line)
            if data['label']!=0:
                res.append((data['id'],data['label']))
    return set(res)

if __name__=='__main__':
    pred=sys.argv[1]
    golden=sys.argv[2]
    if not os.path.exists(pred) or not os.path.exists(golden):
        exit(-1)
    pred=get_results(pred)
    golden=get_results(golden)
    correct=len(pred & golden)
    p=1.0*correct/len(pred)
    r=1.0*correct/len(golden)
    f1=2.0*p*r/(p+r)
    print(json.dumps({"precision":p,"recall":r,"f1":f1}))

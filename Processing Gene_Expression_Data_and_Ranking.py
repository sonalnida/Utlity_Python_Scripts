import collections
from collections import OrderedDict

d = {}
same_key_dic = {}

with open('yng_res_edit.txt', 'r') as f1:
    for line1 in f1:
        line1 = line1.rstrip()
        exp = line1.split("\t")
        f_key = exp[1]
        f_value = exp[0]
        
        if f_key in d.keys():
            geneExprVal = float(exp[0])
            d[f_key][geneExprVal] = 0
        else:
            vals = {}
            geneExprVal = float(exp[0])
            vals[geneExprVal] = 0
            d[f_key] = vals

rankedDict = {}

for keyIdentity in d:
    rankDict = sorted(d[keyIdentity].items(), reverse=True)
    rankedDict[keyIdentity] = rankDict

for rankedKey in rankedDict:
    rank = 1000
    stepSize = int(1000 / len(rankedDict[rankedKey])) if len(rankedDict[rankedKey]) > 0 else 0
    for rankValue in rankedDict[rankedKey]:
        print(f"{rankedKey} {rankValue[0]} {rank}")  # Correct print syntax
        rank -= stepSize

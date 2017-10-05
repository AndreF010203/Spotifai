from numpy import *
from pandas import *

tracksfinal=read_csv("tracks_final.csv",sep="\t").values
templist=[]
for t in tracksfinal:
    tempvar=[]
    tempvar.append(t[0])
    tags=t[5]
    if(tags!="[]"):
        modtags=list(map(lambda x:int(x),tags.replace("'","").replace("[","").replace("]","").split(",")))
        modtags+=[0]*(5-len(modtags))
        for x in modtags:
            tempvar.append(x)
        templist.append(tempvar)
    else:
        for x in range(5):
            tempvar.append(0)
        templist.append(tempvar)
myarr=array(templist)
save("tracks_with_tags.npy",myarr)

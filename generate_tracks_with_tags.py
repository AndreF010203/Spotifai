from numpy import *
from pandas import *

tracksfinal=read_csv("tracks_final.csv",sep="\t").values
templist=[]
for t in tracksfinal:
    tempvar=[]
    tempvar.append(t[0])
    tags=t[4]
    if(tags!="[]" and tags!="[None]"):
        tempvar=tags.replace("[","").replace("]","")
        templist.append(tempvar)
    else:
        tempvar=0
        templist.append(tempvar)
myarr=array(templist)
save("tracks_with_album.npy",myarr)


# coding: utf-8

# In[1]:


from numpy import *
from scipy.sparse import *
from scipy.sparse.linalg import *
from sklearn.preprocessing import *


# In[2]:


P=load_npz("target_playlist_tags_TF_IDF.npz")
P=normalize(P)
M=load_npz("reducedTargetT.npz")


# In[7]:


URM = load_npz("all_playlist_with_tracks_URM.npz").astype("float")


# In[8]:


k=80
U, S, VT = svds(URM, k)
print("svd computed")


# In[9]:


S=diag(S)


# In[10]:


SVT = S.dot(VT)


# In[45]:


PLIDs = load("all_45k_playlist_ordered_by_ID.npy")
test = load_npz("all_playlists_with_tracks.npz")
TIDs = load("all_100k_tracks_ordered_by_ID.npy")

PLIDs = ravel(PLIDs)[0].getcol(0).data


# In[47]:


monoArtist=load("target_playlist_mono_artist.npy")
monoArtistPlID=monoArtist[:,0]
monoArtistArtistID=monoArtist[:,1]
artistIndexes=load("uniqueArtists_NeededToIndexThe_ArtistReducedMatrices.npy")
artistTracks=load_npz("artists_with_tracksID_ordered_by_occurrencies.npz")
target_playlists=genfromtxt("target_playlists.csv",skip_header=1)
playlists_with_tracks=load("playlists_with_tracks.npy")
target_tracks_ordered = load("targetTracksOrdered.npy")
def getsimil(pls, similrow, n):
    maxi = flip(argsort(similrow), axis=0)
    r = []
    for m in maxi:
        if(not isin(target_tracks_ordered[m], pls[1:])):
           r.append(target_tracks_ordered[m])
           if(len(r)==n):
               return r


# In[ ]:


PlwithArtist = load_npz("targetPlaylistArtistReduced.npz")
PlwithArtist = normalize(PlwithArtist, norm="max")
tTracksWithArtist = load_npz("targetTracksArtistReduced.npz")
PlTrackSimByArtist = PlwithArtist * tTracksWithArtist.T


# In[54]:


Utarget = U[isin(PLIDs, target_playlists)]


# In[56]:


Pred = Utarget.dot(SVT)


# In[59]:


TargetPred = Pred[:, isin(TIDs, target_tracks_ordered)]
print("model ready")


# In[ ]:


IDFplaylists = load_npz("target_playlist_tags_TF_IDF.npz")
IDFsim = IDFplaylists * M.T


# In[ ]:


f = TargetPred + PlTrackSimByArtist
FinalPred = f + IDFsim

print("sum ready")


# In[ ]:


def compute_s(fname, finalPlSim):
    with open(fname,"a") as myfile:
        myfile.write("playlist_id,track_ids\n")
        for pl, similsum in zip(playlists_with_tracks, finalPlSim):
            plID=pl[0]
            s = str(int(plID))
            s += ","
            if(isin(plID,monoArtistPlID)):#guarda se c'è un artista solo
                artist=monoArtistArtistID[where(monoArtistPlID==plID)[0][0]]#l'unico artista della playlist
                artistIndex=where(artistIndexes==artist)[0][0]#cerca la sua posizione nella matrice delle tracce
                thisArtistTracks=artistTracks.getrow(artistIndex).data#prende le sue tracce
                rr=array([t for t in thisArtistTracks if t not in pl[1:] and isin(t, target_tracks_ordered)])#prende tutte quelle non già presenti

                if(len(rr)>=5):
                    r = array(rr).take(range(5))
                else:
                    r4 = getsimil(pl, ravel(similsum.todense()), 5)
                    r4 = array([el for el in r4 if el not in rr])
                    r = concatenate((rr, r4.take(range(5-len(rr)))))
            else:
                r = getsimil(pl, ravel(similsum.todense()), 5)#non c'è un artista solo quindi guarda solo i tag
            for el in r:
                s+=str(el)
                s+=" "
            myfile.write(s + "\n")
            
            
def compute(fname, finalPlSim):
    with open(fname,"a") as myfile:
        myfile.write("playlist_id,track_ids\n")
        for pl, similsum in zip(playlists_with_tracks, finalPlSim):
            plID=pl[0]
            s = str(int(plID))
            s += ","
            if(isin(plID,monoArtistPlID)):#guarda se c'è un artista solo
                artist=monoArtistArtistID[where(monoArtistPlID==plID)[0][0]]#l'unico artista della playlist
                artistIndex=where(artistIndexes==artist)[0][0]#cerca la sua posizione nella matrice delle tracce
                thisArtistTracks=artistTracks.getrow(artistIndex).data#prende le sue tracce
                rr=array([t for t in thisArtistTracks if t not in pl[1:] and isin(t, target_tracks_ordered)])#prende tutte quelle non già presenti

                if(len(rr)>=5):
                    r = array(rr).take(range(5))
                else:
                    r4 = getsimil(pl, ravel(similsum), 5)
                    r4 = array([el for el in r4 if el not in rr])
                    r = concatenate((rr, r4.take(range(5-len(rr)))))
            else:
                r = getsimil(pl, ravel(similsum), 5)#non c'è un artista solo quindi guarda solo i tag
            for el in r:
                s+=str(el)
                s+=" "
            myfile.write(s + "\n")


# In[ ]:


print("start printing")
#compute("SVDonURM.csv", TargetPred)
compute("SVDonURMplusArtist.csv", FinalPred)


# In[ ]:





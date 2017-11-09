from numpy import *
from scipy.sparse import *
from sparsesvd import sparsesvd as svd

# utili filtri di Facchini
def filterTarget(m):
    PLIDs = load("fucking_ordered_playlist.npy")
    TIDs = load("fucking_ordered_tracks.npy")
    target_playlists=genfromtxt("target_playlists.csv",skip_header=1)
    target_tracks=genfromtxt("target_tracks.csv", skip_header=1)
    k = m[isin(PLIDs, target_playlists)]
    k = k[:, isin(TIDs, target_tracks)]
    return k

def filterPLrow(m):
    PLIDs = load("fucking_ordered_playlist.npy")
    target_playlists=genfromtxt("target_playlists.csv",skip_header=1)
    k = m[isin(PLIDs, target_playlists)]
    return k 

def filterTcol(m):
    TIDs = load("fucking_ordered_tracks.npy")
    target_tracks=genfromtxt("target_tracks.csv", skip_header=1)
    k = m[:, isin(TIDs, target_tracks)]
    return k

URM=load_npz("all_playlist_with_tracks_URM.npz")
print("faccio svd, 7000 sono tanti quindi stai calmo che tra un po' finisco")
ut100, s100, vt100 = svd(URM,7000)
print("svd finito")
S=diags(s100)

U=lil_matrix(ut100).T
U=filterPLrow(U)

VT=lil_matrix(vt100)
VT=filterTcol(VT)

A=U*S.power(1/2)

B=S.power(1/2)*VT
print("RR = A x B")
RR=A*B

print("ora tolgo le tracce già presenti")

URM_target=filterTarget(URM)

RR=RR-URM_target
print("abbiamo i rating, ora si comincia a fare sul serio")

targetPlaylist=unique(genfromtxt("target_playlists.csv",skip_header=1,dtype=int32))

targetTrack=unique(genfromtxt("target_tracks.csv",dtype=int32,skip_header=1))

with open("dalCloudConFuroreConKappaQuasiOverNinethousand.csv","w") as f:
    f.write("playlist_id,track_ids\n")
    for plID,sims in zip(targetPlaylist,RR):
        f.write(str(plID)+",")
        suggestions=targetTrack[flip(argsort(sims.todense()),1).take(range(5))]
        for t in suggestions[0]:
            f.write(str(t)+" ")
        f.write("\n")

# Spotifai

> O ci sei o ci fai

---

## Files guide

### track_artist.npy
(*all 100k tracks ordered as in tracks_final.csv*)

array([

[IDtrack1, IDartist1],

[IDtrack2, IDartist2],

... ])

### ordered_tracks.npy
(*all 100k IDtracks ordered by occurrency count*)

array([IDtrack1, IDtrack2, ... ])

### tracks_with_tags.npy
(*all 100k tracks ordered as in tracks_final.csv*)

array([

[IDtrack1, tag1.1, tag1.2, tag 1.3, tag 1.4, tag 1.5]

[IDtrack2, tag2.1, tag2.2, tag2.3, tag2.4, tag2.5]

... ])

### indexsortedDESCENDENT.npy
(*index of all 100k songs ordered by occurrency, applicable to tracks_final.csv ordering*)

array([index1, index2, ... ])

### orderedTargetIndexes.npy
(*index of only target songs (subset of indexsortedDESCENDENT.npy) ordered by occurrency, applicable to tracks_final.csv ordering*)

array([index1, index2, ... ])

### playlists_with_tracks.npy
(*ordered as in target_playlists.csv*)

array([

[IDplaylist1, IDtrack1.1, IDtrack1.2, ... ],

[IDplaylist2, IDtrack2.1, IDtrack2.2, ... ],

... ])

### idsong_playcount_populartiy.npy

(*all 100k songs ordered as in tracks_final.csv*)

array([

[IDtrack1, playcount1, occurrencies1, playcount1+occurrencies1 ],

[IDtrack2, playcount2, occurrencies2, playcount2+occurrencies2 ],

... ])

### tracks_with_tags_bincount_ordered.npz
(*all 100k tracks ordered by occurrency, bincount of all tags from 0 to 276614, without IDtrack*)

matrix([

[bincountTag1, bincountTag2, ... ],

[bincountTag1, bincountTag2, ... ],

... ])

### tracks_ordered_tags_reduced.npz
(*subset of tracks_with_tags_bincount_ordered.npz, all 100k tracks ordered by occurrency, but only nonzero columns are kept, only existing tags*)

matrix([

[bincountTag1, bincountTag2, ... ],

[bincountTag1, bincountTag2, ... ],

... ])

### reducedTargetT.npz
(*subset of tracks_ordered_tags_reduced.npz, only target tracks are kept, ordered by occurrency*)

matrix([

[bincountTag1, bincountTag2, ... ],

[bincountTag1, bincountTag2, ... ],

... ])

### playlists_with_tags.npz
(*all 10k playlists ordered as in target_playlists.csv, bincount of all tags from 0 to 276614, without IDplaylist*)

matrix([

[bincountTag1, bincountTag2, ... ],

[bincountTag1, bincountTag2, ... ],

... ])

### playlist_reduced.npz
(*subset of playlists_with_tags.npz, the same non zero bincount column of tracks_ordered_tags_reduced.npz are kept*)

matrix([

[bincountTag1, bincountTag2, ... ],

[bincountTag1, bincountTag2, ... ],

... ])

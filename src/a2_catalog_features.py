# A2: Catalog Feature Creation

import numpy as np
import pandas as pd

gaia_df = pd.read_csv("data/gaia_catalog_star_centroids_2.csv")

ra = np.deg2rad(gaia_df["ra"].values)
dec = np.deg2rad(gaia_df["dec"].values)

vec_cat = np.vstack([
    np.cos(dec) * np.cos(ra),
    np.cos(dec) * np.sin(ra),
    np.sin(dec)
]).T

ang_cat = np.arccos(np.clip(vec_cat @ vec_cat.T, -1, 1))

def angular_features(ang_mat, k=3):
    feats, idxs = [], []
    for i in range(len(ang_mat)):
        d = np.sort(ang_mat[i][ang_mat[i] > 0])
        if len(d) >= k:
            feats.append(d[:k])
            idxs.append(i)
    return np.array(feats), np.array(idxs)

feat_cat, cat_idx = angular_features(ang_cat, k=3)

np.save("data/catalog_vectors.npy", vec_cat)
np.save("data/catalog_features.npy", feat_cat)
np.save("data/catalog_indices.npy", cat_idx)

print("A2 complete — catalog features:", feat_cat.shape)

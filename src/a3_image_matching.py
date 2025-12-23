# A3: Image Feature Creation & Matching

import numpy as np
import pandas as pd
from scipy.spatial import KDTree

# ---- Load centroids ----
df = pd.read_csv("data/star_centroids_2.csv")
df = df.sort_values("brightness", ascending=False).iloc[:25].reset_index(drop=True)

# ---- Camera model ----
IMAGE_W, IMAGE_H = 1024, 1024
FOCAL_MM = 4912
PIXEL_UM = 3.6

cx, cy = IMAGE_W/2, IMAGE_H/2
f_pix = (FOCAL_MM * 1e3) / PIXEL_UM

dx = df["x_centroid"].values - cx
dy = df["y_centroid"].values - cy

vec_img = np.vstack([dx, dy, np.ones_like(dx)*f_pix]).T
vec_img /= np.linalg.norm(vec_img, axis=1)[:, None]

ang_img = np.arccos(np.clip(vec_img @ vec_img.T, -1, 1))

def angular_features(ang_mat, k=3):
    feats, idxs = [], []
    for i in range(len(ang_mat)):
        d = np.sort(ang_mat[i][ang_mat[i] > 0])
        if len(d) >= k:
            feats.append(d[:k])
            idxs.append(i)
    return np.array(feats), np.array(idxs)

feat_img, img_idx = angular_features(ang_img, k=3)

# ---- Load catalog features ----
feat_cat = np.load("data/catalog_features.npy")
cat_idx = np.load("data/catalog_indices.npy")

tree = KDTree(feat_cat)

used_catalog = set()
matches = []

for i, f in enumerate(feat_img):
    dist, j = tree.query(f, distance_upper_bound=0.03)
    if np.isfinite(dist) and j not in used_catalog:
        used_catalog.add(j)
        matches.append((img_idx[i], cat_idx[j]))

np.save("data/initial_matches.npy", matches)
np.save("data/image_vectors.npy", vec_img)

print("A3 complete — initial matches:", len(matches))

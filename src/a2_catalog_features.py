# A2: Catalog Feature Creation

import numpy as np
import pandas as pd

# ------------------------------------------------------------------
# Load Gaia catalog (RA, DEC in degrees)
# ------------------------------------------------------------------
gaia_df = pd.read_csv("data/gaia_catalog_star_centroids_2.csv")

ra = np.deg2rad(gaia_df["ra"].values)
dec = np.deg2rad(gaia_df["dec"].values)

# ------------------------------------------------------------------
# Convert (RA, DEC) → unit vectors in Cartesian coordinates
# ------------------------------------------------------------------
vec_cat = np.vstack([
    np.cos(dec) * np.cos(ra),
    np.cos(dec) * np.sin(ra),
    np.sin(dec)
]).T

# ------------------------------------------------------------------
# Compute angular separation matrix
# ------------------------------------------------------------------
ang_cat = np.arccos(np.clip(vec_cat @ vec_cat.T, -1.0, 1.0))

# ------------------------------------------------------------------
# Extract k-nearest angular features
# ------------------------------------------------------------------
def angular_features(ang_mat, k=3):
    feats, idxs = [], []
    for i in range(len(ang_mat)):
        d = np.sort(ang_mat[i][ang_mat[i] > 0])  # exclude self-angle
        if len(d) >= k:
            feats.append(d[:k])
            idxs.append(i)
    return np.array(feats), np.array(idxs)

feat_cat, cat_idx = angular_features(ang_cat, k=3)

# ------------------------------------------------------------------
# Save outputs (NumPy + CSV)
# ------------------------------------------------------------------
np.save("data/catalog_vectors.npy", vec_cat)
np.save("data/catalog_features.npy", feat_cat)
np.save("data/catalog_indices.npy", cat_idx)

# Save catalog features as CSV for inspection / portability
features_df = pd.DataFrame(
    feat_cat,
    columns=[f"theta_{i+1}" for i in range(feat_cat.shape[1])]
)
features_df["catalog_index"] = cat_idx

features_df.to_csv("data/catalog_features.csv", index=False)

print("A2 complete — catalog features shape:", feat_cat.shape)
print("Saved:")
print(" - data/catalog_vectors.npy")
print(" - data/catalog_features.npy")
print(" - data/catalog_indices.npy")
print(" - data/catalog_features.csv")

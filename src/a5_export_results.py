# A5: Export Final Matched Star Data

import pandas as pd
import numpy as np
matched_df = pd.DataFrame({
    "x_centroid": df.loc[img_indices, "x_centroid"].values,
    "y_centroid": df.loc[img_indices, "y_centroid"].values,
    "brightness": df.loc[img_indices, "brightness"].values,
    "ra": gaia_df.loc[cat_indices, "ra"].values,
    "dec": gaia_df.loc[cat_indices, "dec"].values,
    "magnitude": gaia_df.loc[cat_indices, "phot_g_mean_mag"].values
})

matched_df

df = pd.read_csv("data/star_centroids_2.csv")
gaia = pd.read_csv("data/gaia_catalog_star_centroids_2.csv")

matches = np.load("data/initial_matches.npy", allow_pickle=True)
inliers = np.load("data/inliers.npy")

rows = []

for (img_i, cat_i), ok in zip(matches, inliers):
    if ok:
        rows.append([
            df.loc[img_i,"x_centroid"],
            df.loc[img_i,"y_centroid"],
            df.loc[img_i,"brightness"],
            gaia.loc[cat_i,"ra"],
            gaia.loc[cat_i,"dec"],
            gaia.loc[cat_i,"phot_g_mean_mag"]
        ])

out = pd.DataFrame(
    rows,
    columns=["x_centroid","y_centroid","brightness","ra","dec","magnitude"]
)

out.to_csv("data/matched_star_data_star_centroids_2.csv", index=False)
print("A5 complete — final CSV saved")
import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.scatter(
    gaia_df["ra"],
    gaia_df["dec"],
    s=15,
    alpha=0.3,
    label="Catalog stars"
)

plt.scatter(
    matched_df["ra"],
    matched_df["dec"],
    s=60,
    facecolors="none",
    edgecolors="red",
    label="Matched stars"
)

plt.xlabel("RA (deg)")
plt.ylabel("DEC (deg)")
plt.title("Sky Projection of Matched Stars")
plt.gca().invert_xaxis()
plt.legend()
plt.tight_layout()
plt.show()

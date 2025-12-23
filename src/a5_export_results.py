import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/star_centroids_2.csv")
gaia_df = pd.read_csv("data/gaia_catalog_star_centroids_2.csv")

matches = np.load("data/initial_matches.npy", allow_pickle=True)
inliers = np.load("data/inliers.npy")

# Build rows safely
rows = []

for (img_i, cat_i), ok in zip(matches, inliers):
    if ok:
        rows.append({
            "x_centroid": df.loc[int(img_i), "x_centroid"],
            "y_centroid": df.loc[int(img_i), "y_centroid"],
            "brightness": df.loc[int(img_i), "brightness"],
            "ra": gaia_df.loc[int(cat_i), "ra"],
            "dec": gaia_df.loc[int(cat_i), "dec"],
            "magnitude": gaia_df.loc[int(cat_i), "phot_g_mean_mag"]
        })

matched_df = pd.DataFrame(rows)

matched_df
matched_df.to_csv(
    "data/matched_star_data_star_centroids_2.csv",
    index=False
)

print("A5 complete — final CSV saved")
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


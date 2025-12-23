from astroquery.gaia import Gaia
import matplotlib.pyplot as plt
# ---- Metadata ----
RA0_DEG  = 101.812
DEC0_DEG = -48.565
FOV_X_DEG = 0.429
FOV_Y_DEG = 0.429
MAG_LIMIT = 11.5

query = f"""
SELECT ra, dec, phot_g_mean_mag
FROM gaiadr3.gaia_source
WHERE
  CONTAINS(
    POINT('ICRS', ra, dec),
    BOX('ICRS', {RA0_DEG}, {DEC0_DEG}, {FOV_X_DEG}, {FOV_Y_DEG})
  ) = 1
AND phot_g_mean_mag < {MAG_LIMIT}
ORDER BY phot_g_mean_mag ASC
"""

job = Gaia.launch_job(query)
gaia_df = job.get_results().to_pandas()

gaia_df.to_csv("data/gaia_catalog_star_centroids_2.csv", index=False)
print("A1 complete — GAIA stars:", len(gaia_df))

#------Catalog plots------
plt.figure(figsize=(5,5))
plt.scatter(gaia_df["ra"], gaia_df["dec"], s=30)
plt.xlabel("RA (deg)")
plt.ylabel("DEC (deg)")
plt.title("GAIA DR3 Stars in FoV")
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()

plt.figure(figsize=(5,3))
plt.hist(gaia_df["phot_g_mean_mag"], bins=10)
plt.xlabel("G Magnitude")
plt.ylabel("Count")
plt.title("Magnitude Distribution")
plt.tight_layout()
plt.show()

# Star-tracker
Star matching and astrometry pipeline for SSA star tracker assessment

#Repository structure
```text
digantara-star-tracker-astrometry/
│
├── src/
│   ├── a1_catalog_download.py
│   ├── a2_catalog_features.py
│   ├── a3_image_matching.py
│   ├── a4_verification.py
│   └── a5_export_results.py
│
├── notebooks/
│   └── star_tracker_pipeline.ipynb
│
├── data/
│   ├── star_centroids_2.csv
│   ├── gaia_catalog_star_centroids_2.csv
│   └── matched_star_data_star_centroids_2.csv
│
├── report.pdf
├── requirements.txt
└── README.md
```
**Methodology Summary**

The pipeline follows the structure specified in the assessment (A1–A5):

A1 – Catalog Download

-GAIA DR3 catalog queried using provided RA, DEC, and rectangular FoV

-Magnitude filtering applied to retain detectable stars

-Catalog stored in CSV format

A2 – Catalog Feature Creation

-Catalog stars converted to unit direction vectors

-Rotation-invariant angular-distance features generated

-Feature dimensionality adaptively reduced due to sparse star field

A3 – Image Feature Creation & Matching

-Brightest detected centroids selected for reliability

-Pixel coordinates converted to camera-frame unit vectors

-Feature matching performed using KD-tree

-One-to-one matching enforced to avoid degenerate solutions

A4 – Verification & Orientation Estimation

-Global orientation estimated by solving Wahba’s problem using SVD

-Angular residuals computed to reject false matches

-RMS angular error (arcseconds) used as accuracy metric

A5 – Final Output

-Verified star correspondences exported as CSV

-Mapping provided from image centroids to catalog coordinates

**How to Run**

Option 1: Run the Notebook (Recommended)

Open and execute the notebook:

notebooks/star_tracker_pipeline.ipynb

The notebook is self-contained and installs required dependencies when run in Google Colab.

Option 2: Run Scripts Sequentially
```text
pip install -r requirements.txt
python src/a1_catalog_download.py
python src/a2_catalog_features.py
python src/a3_image_matching.py
python src/a4_verification.py
python src/a5_export_results.py
```



**Requirements.txt**
```text
numpy
pandas
matplotlib
scipy
astropy
astroquery
```

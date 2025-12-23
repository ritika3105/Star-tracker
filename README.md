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
#Requirements
```text
numpy
pandas
matplotlib
scipy
astropy
astroquery
```

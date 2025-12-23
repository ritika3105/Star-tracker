# A4: Verification & Orientation Estimation

import numpy as np

vec_img = np.load("data/image_vectors.npy")
vec_cat = np.load("data/catalog_vectors.npy")
matches = np.load("data/initial_matches.npy", allow_pickle=True)

V_img = np.array([vec_img[m[0]] for m in matches])
V_cat = np.array([vec_cat[m[1]] for m in matches])

def solve_rotation(A, B):
    H = B.T @ A
    U, _, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T
    if np.linalg.det(R) < 0:
        Vt[-1] *= -1
        R = Vt.T @ U.T
    return R

R = solve_rotation(V_img, V_cat)
V_rot = (R @ V_cat.T).T

res = np.arccos(np.clip(np.sum(V_img * V_rot, axis=1), -1, 1))
res_arcsec = res * 180/np.pi * 3600

inliers = res_arcsec < 300
np.save("data/inliers.npy", inliers)

print("A4 complete — RMS (arcsec):", np.sqrt(np.mean(res_arcsec[inliers]**2)))
import matplotlib.pyplot as plt
plt.hist(res_arcsec, bins=10)
plt.xlabel("Residual (arcsec)")
plt.ylabel("Count")
plt.title("Verification Residuals")
plt.tight_layout()
plt.show()

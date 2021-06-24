import cv2
from glob import glob
from pathlib import Path
from pydicom import dcmread
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
from utils import dicom_utils, draw_utils
import json


def main():
    image_level = pd.read_csv("data/radiographs/train_image_level.csv")
    study_level = pd.read_csv("data/radiographs/train_study_level.csv")
    imgs = glob("data/radiographs/*.dcm")
    for imgpath in imgs:
        imgpath = Path(imgpath)
        img_image_level = image_level.loc[image_level["id"] == f"{imgpath.stem}_image"].to_dict(orient="list")
        img_image_level["boxes"] = json.loads(img_image_level["boxes"][0].replace("'", '"'))
        img_study_level = study_level.loc[study_level["id"] == f"{imgpath.stem}_study"].to_dict(orient="list")
        # imgpath = imgs[0]
        dicom_img = dcmread(imgpath)
        img_2d_scaled = dicom_utils.dicom2png(dicom_img)
        # img_2d_scaled = Image.fromarray(img_2d_scaled)

        draw_utils.draw_boxes(img_2d_scaled, img_image_level)

        plt.imshow(img_2d_scaled, cmap=plt.cm.gray)
        plt.show()


if __name__ == "__main__":
    main()


"""
%load_ext autoreload
%autoreload 2
"""

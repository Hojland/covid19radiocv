import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

color_palletes = [
    (123, 141, 245),
    (123, 193, 239),
    (230, 193, 239),
    (230, 79, 239),
    (71, 79, 239),
    (71, 170, 90),
    (201, 170, 38),
    (201, 47, 46),
    (201, 240, 219),
    (0, 43, 255),
    (0, 255, 255),
    (102, 114, 41),
    (255, 242, 235),
    (54, 0, 0),
]


def draw_boxes(img, img_meta, plot_rad=False, figsize=(10, 15), return_img=False):
    labels = re.split(r"[a-z]+\s", img_meta["label"][0])[1:]
    class_names = re.findall(r"[a-z]+", img_meta["label"][0])
    for i, box in enumerate(img_meta["boxes"]):
        x1, y1, x2, y2, cls_name = (
            int(box["x"]),
            int(box["y"]),
            int(box["x"] + box["width"]),
            int(box["y"] + box["height"]),
            class_names[i],
        )

        c = color_palletes[5]
        cv2.rectangle(img, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=6)
        # if plot_rad:
        #    rad_id = row["rad_id"]
        #    cv2.putText(img, cls_name + "-" + rad_id, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.7, c, 2)
        # else:
        cv2.putText(img, cls_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, fontScale=2.4, color=(0, 255, 0), thickness=4)

    if not return_img:
        plt.figure(figsize=figsize)
        plt.imshow(img)
    else:
        return img


def show_values_on_bars(axs, h_v="v", space=0.4):
    def _show_on_single_plot(ax):
        if h_v == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height()
                value = int(p.get_height())
                ax.text(_x, _y, value, ha="center")
        elif h_v == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height()
                value = int(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)
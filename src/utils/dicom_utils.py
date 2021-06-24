import pydicom
from pydicom.dataset import FileDataset
import numpy as np
import png
import os
from pathlib import Path


def dicom2png(dicom_obj: FileDataset, output_folder: str = None):
    try:
        shape = dicom_obj.pixel_array.shape

        # Convert to float to avoid overflow or underflow losses.
        image_2d = dicom_obj.pixel_array.astype(float)

        # Rescaling grey scale between 0-255
        image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max()) * 255.0

        # Convert to uint
        image_2d_scaled = np.uint8(image_2d_scaled)

        if not output_folder:
            return image_2d_scaled
        else:
            # Write the PNG file
            filepath = Path(dicom_obj.filename)
            with open(os.path.join(output_folder, filepath.stem) + ".png", "wb") as png_file:
                w = png.Writer(shape[1], shape[0], greyscale=True)
                w.write(png_file, image_2d_scaled)
    except:
        print(f"Could not convert: {dicom_obj.filename}")

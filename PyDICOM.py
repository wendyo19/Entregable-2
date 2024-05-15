import os
import pydicom
import matplotlib.pyplot as plt
import time
class DICOMViewer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.image_files = self._load_images()

    def _load_images(self):
        image_files = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.dcm'):
                image_files.append(os.path.join(self.folder_path, filename))
        return sorted(image_files) 

    
    def display_images(self):
        for image_file in self.image_files:
            dataset = pydicom.dcmread(image_file)
            image = dataset.pixel_array
            plt.imshow(image, cmap='gray')
            plt.title(f"Image {self.image_files.index(image_file) + 1}")
            plt.axis('off')
            plt.show()
            time.sleep(1)

folder_path = "archivosdcm"
viewer = DICOMViewer(folder_path)
viewer.display_images()

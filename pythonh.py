import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Gallery")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.LEFT)

        self.load_button = tk.Button(self.button_frame, text="Load Images", command=self.load_images)
        self.load_button.pack(side=tk.LEFT)

        self.images = []
        self.current_image_index = 0

    def load_images(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.images = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                           if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            if self.images:
                self.current_image_index = 0
                self.show_image()

    def show_image(self):
        if self.images:
            image_path = self.images[self.cu

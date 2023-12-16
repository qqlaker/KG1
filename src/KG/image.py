from PIL import Image as Im

class Image:
    def __init__(self, image_path):
        img = self.load_image(image_path)
        self.img_size = img[0]
        self.img_matrix = img[1]
        self.img_mode = img[2]
        
    def load_image(self, image_path):
        img = Im.open(image_path)
        img = img.convert("L")
        img_matrix = list(img.getdata())
        return img.size, img_matrix, img.mode
    
    def save_image(self, image_path):
        im2 = Im.new(self.img_mode, self.img_size)
        im2.putdata(self.img_matrix)
        im2.save(image_path)
        
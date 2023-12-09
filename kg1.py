from PIL import Image as Im
import numpy as np

class Image:
    def __init__(self, image_path):
        tup = self.load_image(image_path)
        self.img_size = tup[0]
        self.img_matrix = tup[1]
        self.img_mode = tup[2]
        
    def load_image(self, image_path):
        img = Im.open(image_path)
        img = img.convert("L")
        img_matrix = list(img.getdata())
        return img.size, img_matrix, img.mode

    def process_image_laplas(self):
        width, height = self.img_size
        result_matrix = [0] * (width * height)
        laplacian_operator = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
        for y in range(height):
            for x in range(width):
                # вычисляем индекс текущего пикселя в матрице
                index = y * width + x
                
                if x > 0 and y > 0 and x < width - 1 and y < height - 1:
                    # вычисляем новое значение пикселя с помощью оператора Лапласа
                    new_value = sum([self.img_matrix[(y + j) * width + (x + i)] * laplacian_operator[j * 3 + i] for j in range(-1, 2) for i in range(-1, 2)])
                    
                    result_matrix[index] = new_value
        self.img_matrix = result_matrix\
            
    def process_image_roberts(self):
        width, height = self.img_size
        result_matrix = [0] * (width * height)

        # маска оператора Робертса
        roberts_operator_x = [1, 0, 0, -1]
        roberts_operator_y = [-1, 0, 0, 1]

        for y in range(height):
            for x in range(width):
                # индекс текущего пикселя в матрице
                index = y * width + x

                if x > 0 and y > 0 and x < width - 1 and y < height - 1:
                    # вычисляем новое значение пикселя с помощью оператора Робертса
                    gx = abs(self.img_matrix[y * width + x] * roberts_operator_x[0] - self.img_matrix[(y + 1) * width + x] * roberts_operator_x[1] - self.img_matrix[y * width + x + 1] * roberts_operator_x[2] + self.img_matrix[(y + 1) * width + x + 1] * roberts_operator_x[3])
                    gy = abs(self.img_matrix[y * width + x] * roberts_operator_y[0] - self.img_matrix[(y + 1) * width + x] * roberts_operator_y[1] - self.img_matrix[y * width + x + 1] * roberts_operator_y[2] + self.img_matrix[(y + 1) * width + x + 1] * roberts_operator_y[3])
                    
                    new_value = int((gx ** 2 + gy ** 2) ** 0.5)
                    result_matrix[index] = new_value

        self.img_matrix = result_matrix

    def process_image_sobel(self):
        width, height = self.img_size
        result_matrix = [0] * (width * height)

        # операторы Собела для вычисления градиента по горизонтали и вертикали
        sobel_x = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
        sobel_y = [-1, -2, -1, 0, 0, 0, 1, 2, 1]

        # проходим по всем пикселям изображения
        for y in range(height):
            for x in range(width):
                # вычисляем индекс текущего пикселя в матрице
                index = y * width + x

                # проверяем, что текущий пиксель не находится на границе изображения
                if x > 0 and y > 0 and x < width - 1 and y < height - 1:
                    # вычисляем новое значение пикселя с помощью операторов Собела
                    gx = self.img_matrix[(y - 1) * width + x - 1] * sobel_x[0] + self.img_matrix[(y - 1) * width + x] * sobel_x[1] + self.img_matrix[(y - 1) * width + x + 1] * sobel_x[2] + self.img_matrix[y * width + x - 1] * sobel_x[3] + self.img_matrix[y * width + x] * sobel_x[4] + self.img_matrix[y * width + x + 1] * sobel_x[5] + self.img_matrix[(y + 1) * width + x - 1] * sobel_x[6] + self.img_matrix[(y + 1) * width + x] * sobel_x[7] + self.img_matrix[(y + 1) * width + x + 1] * sobel_x[8]
                    gy = self.img_matrix[(y - 1) * width + x - 1] * sobel_y[0] + self.img_matrix[(y - 1) * width + x] * sobel_y[1] + self.img_matrix[(y - 1) * width + x + 1] * sobel_y[2] + self.img_matrix[y * width + x - 1] * sobel_y[3] + self.img_matrix[y * width + x] * sobel_y[4] + self.img_matrix[y * width + x + 1] * sobel_y[5] + self.img_matrix[(y + 1) * width + x - 1] * sobel_y[6] + self.img_matrix[(y + 1) * width + x] * sobel_y[7] + self.img_matrix[(y + 1) * width + x + 1] * sobel_y[8]
                    new_value = int((gx ** 2 + gy ** 2) ** 0.5)

                    # сохраняем новое значение пикселя в результат
                    result_matrix[index] = new_value
        self.img_matrix = result_matrix

    def save_processed_image(self):
        im2 = Im.new(self.img_mode, self.img_size)
        im2.putdata(self.img_matrix)
        im2.save("sobel.png")


image = Image("test.png")
image.process_image_laplas()
image.process_image_roberts()
image.process_image_sobel()
image.save_processed_image()
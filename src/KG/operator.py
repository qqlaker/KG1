from KG.image import Image


def process_image_laplas(img: Image) -> Image:
    width, height = img.img_size
    result_matrix = [0] * (width * height)
    laplacian_operator = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
    for y in range(height):
        for x in range(width):
            # вычисляем индекс текущего пикселя в матрице
            index = y * width + x
            
            if x > 0 and y > 0 and x < width - 1 and y < height - 1:
                # вычисляем новое значение пикселя с помощью оператора Лапласа
                new_value = sum([img.img_matrix[(y + j) * width + (x + i)] * laplacian_operator[j * 3 + i] for j in range(-1, 2) for i in range(-1, 2)])
                
                result_matrix[index] = new_value
    img.img_matrix = result_matrix
    return img
        
def process_image_roberts(img: Image) -> Image:
    width, height = img.img_size
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
                gx = abs(img.img_matrix[y * width + x] * roberts_operator_x[0] - 
                         img.img_matrix[(y + 1) * width + x] * roberts_operator_x[1] - 
                         img.img_matrix[y * width + x + 1] * roberts_operator_x[2] + 
                         img.img_matrix[(y + 1) * width + x + 1] * roberts_operator_x[3])
                
                gy = abs(img.img_matrix[y * width + x] * roberts_operator_y[0] - 
                         img.img_matrix[(y + 1) * width + x] * roberts_operator_y[1] - 
                         img.img_matrix[y * width + x + 1] * roberts_operator_y[2] + 
                         img.img_matrix[(y + 1) * width + x + 1] * roberts_operator_y[3])
                
                new_value = int((gx ** 2 + gy ** 2) ** 0.5)
                result_matrix[index] = new_value

    img.img_matrix = result_matrix
    return img

def process_image_sobel(img: Image) -> Image:
    width, height = img.img_size
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
                gx = img.img_matrix[(y - 1) * width + x - 1] * sobel_x[0] + \
                    img.img_matrix[(y - 1) * width + x] * sobel_x[1] + \
                    img.img_matrix[(y - 1) * width + x + 1] * sobel_x[2] + \
                    img.img_matrix[y * width + x - 1] * sobel_x[3] + \
                    img.img_matrix[y * width + x] * sobel_x[4] + \
                    img.img_matrix[y * width + x + 1] * sobel_x[5] + \
                    img.img_matrix[(y + 1) * width + x - 1] * sobel_x[6] + \
                    img.img_matrix[(y + 1) * width + x] * sobel_x[7] + \
                    img.img_matrix[(y + 1) * width + x + 1] * sobel_x[8]
                
                gy = img.img_matrix[(y - 1) * width + x - 1] * sobel_y[0] + \
                    img.img_matrix[(y - 1) * width + x] * sobel_y[1] + \
                    img.img_matrix[(y - 1) * width + x + 1] * sobel_y[2] + \
                    img.img_matrix[y * width + x - 1] * sobel_y[3] + \
                    img.img_matrix[y * width + x] * sobel_y[4] + \
                    img.img_matrix[y * width + x + 1] * sobel_y[5] + \
                    img.img_matrix[(y + 1) * width + x - 1] * sobel_y[6] + \
                    img.img_matrix[(y + 1) * width + x] * sobel_y[7] + \
                    img.img_matrix[(y + 1) * width + x + 1] * sobel_y[8]
                    
                new_value = int((gx ** 2 + gy ** 2) ** 0.5)

                # сохраняем новое значение пикселя в результат
                result_matrix[index] = new_value
                
    img.img_matrix = result_matrix
    return img
    
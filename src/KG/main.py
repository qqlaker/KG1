from KG.image import Image
from KG.operator import *

# Лаплас
image_object = Image("src/KG/input/test_logo.png")
process_image_laplas(image_object)
image_object.save_image("src/KG/output_1/laplas.png")

# Робертс
image_object = Image("src/KG/input/test_logo.png")
process_image_roberts(image_object)
image_object.save_image("src/KG/output_1/roberts.png")

# Собель
image_object = Image("src/KG/input/test_logo.png")
process_image_sobel(image_object)
image_object.save_image("src/KG/output_1/sobel.png")
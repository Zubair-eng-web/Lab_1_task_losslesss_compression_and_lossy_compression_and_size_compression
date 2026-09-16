from PIL import Image

image = Image.open("my_image.jpeg")

image.save("compressed.png", compress_level=9)

print("Lossless compression completed!")
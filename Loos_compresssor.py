from PIL import Image

image = Image.open("my_image.jpeg")

image.save("compressed2.jpg", quality=40)

print("Lossy compression completed!")

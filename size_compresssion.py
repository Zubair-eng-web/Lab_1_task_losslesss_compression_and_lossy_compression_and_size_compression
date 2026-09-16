from PIL import Image

image = Image.open("my_image.png")

image.save("my_image3_compressed.jpg", quality=30)

print("Lossy compression completed!")
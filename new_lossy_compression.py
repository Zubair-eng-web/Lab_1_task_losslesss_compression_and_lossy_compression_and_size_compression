from PIL import Image

image = Image.open("zubair_image.jpeg")

image.save("zubai2_compressed.png", compress_level=9)

print("Lossless compression completed!")
from PIL import Image
image = Image.open("image.jpg")
image = image.convert("RGB")
red, green, blue = image.split()

coordinates_1 = (100, 0, red.width, red.height)
coordinates_2 = (50, 0, red.width-50, red.height)
red_image = Image.blend(red.crop(coordinates_1), red.crop(coordinates_2), 0.3)

coordinates_1 = (0, 0, blue.width-100, blue.height)
coordinates_2 = (50, 0, blue.width-50, blue.height)
blue_image = Image.blend(blue.crop(coordinates_1), blue.crop(coordinates_2), 0.3)

coordinates = (50, 0, green.width-50, green.height)
green_image = green.crop(coordinates)

new_image = Image.merge("RGB", (red_image, blue_image, green_image))
new_image.save("new_image.jpg")

new_image.thumbnail((80, 80))
new_image.save("new_image_80.jpg")
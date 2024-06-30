from PIL import Image, ImageDraw

desktop_size = (1920, 1080)

# Create a new image with RGB mode
image = Image.new("RGB", desktop_size, "white")

# Draw on the image
draw = ImageDraw.Draw(image)
draw.rectangle([100, 100, 300, 300], outline="black", width=5)

# Save image
image.save("./output/output.png")
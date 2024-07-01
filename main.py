from PIL import Image, ImageDraw, ImageFont

def parse_config(txt_file):
    with open(txt_file, "r") as file:
        config = {}
        for line in file:
            if line.startswith("#"):
                continue

            key, value = line.split("=")
            config[key.strip()] = value.strip()

    return config

def parse_input(txt_file):
    with open(txt_file, "r") as file:
        text = file.read()
    
    return text

if __name__ == "__main__":
    TEXT = parse_input(txt_file = "input.txt")
    CONFIG = parse_config(txt_file = "config.txt")

    # Create image
    desktop_height = int(CONFIG['desktop_height'])
    desktop_width = int(CONFIG['desktop_width'])
    desktop_size = (desktop_width, desktop_height)
    image = Image.new("RGB", (int(CONFIG['desktop_width']), int(CONFIG['desktop_height'])), CONFIG['background_color'])

    # Draw on the image
    draw = ImageDraw.Draw(image)

    # Draw Text on Image
    text_position = (desktop_width // 2, desktop_height // 2)
    text_color = CONFIG['text_color']
    text_size = int(CONFIG['text_size'])

    # Dynamically change text size based on number of lines in the text
    # lines = TEXT.split("\n")
    # num_lines = len(lines)
    # text_size = text_size - (num_lines - 1) * 8

    # Create a font object with the desired size
    font = ImageFont.truetype("arial.ttf", text_size)

    draw.multiline_text(text_position, TEXT, fill=text_color, font=font, anchor='mm')

    # Save image
    image.save("./output/output.png")

    # TODO
    # - Read Text from TXT File
    # - Draw Text on Image
    # - Dynamically change text size based on number of lines in the text

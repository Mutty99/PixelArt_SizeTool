from PIL import Image, ImageDraw


def process_image(input_image_path):
    img = Image.open(input_image_path)
    img = img.convert('RGBA')
    width, height = img.size
    square_size = 9  # Edit value as needed: this is n, with a single "pixel" size being 'n x n' actual pixels

    if width % square_size != 0 or height % square_size != 0:
        raise ValueError("Input error!")

    rows = width // square_size
    columns = height // square_size
    color_map = []

    for i in range(0, height, square_size):
        row_colors = []
        for j in range(0, width, square_size):
            square = img.crop((j, i, j + square_size, i + square_size))
            avg_color = tuple(int(sum(c) / len(c)) for c in zip(*list(square.getdata())))
            row_colors.append(avg_color)
        color_map.append(row_colors)
    return color_map, width, height, rows, columns


def create_pixel_art():
    resolution = 100  # Edit value as needed: this is the new square_size
    color_map, width, height, rows, columns = process_image('test.png')

    new_width = rows * resolution
    new_height = columns * resolution
    image = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    square_width = resolution
    square_height = resolution

    for y in range(columns):
        for x in range(rows):
            color = color_map[y][x]
            if color[3] != 0:
                top_left = (x * square_width, y * square_height)
                bottom_right = ((x + 1) * square_width, (y + 1) * square_height)
                draw.rectangle([top_left, bottom_right], fill=color[:-1])

    image.save("output.png")
    image.show()


create_pixel_art()

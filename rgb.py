from PIL import Image
import statistics


def get_image():
    im = input("Image: ")
    image = Image.open(im, "r")

    pixel_counts = image.getdata()

    return pixel_counts


def get_info(n, pixel_counts):
    pixels = [i[n] for i in pixel_counts]

    image_median = statistics.median(pixels)

    return pixels, image_median


def get_background(pixels, image_median):
    background_pixels = [i for i in pixels if i <= image_median]

    background_mean = statistics.mean(background_pixels)

    return background_mean


def get_star(pixels, image_median, background_mean):
    star_pixels = [i-background_mean for i in pixels if i > image_median]

    star_mean = statistics.mean(star_pixels)

    return star_mean


def get_star_rgb():
    pixel_counts = get_image()

    rgb = [0, 1, 2]
    star_rgb = []

    for i in rgb:
        pixels, image_median = get_info(i, pixel_counts)
        background_mean = get_background(pixels, image_median)
        star_mean = get_star(pixels, image_median, background_mean)

        star_rgb.append(star_mean)

    return star_rgb


def reduce_star_rgb():
    star_rgb = get_star_rgb()

    max_rgb = max(star_rgb)

    reduced_rgb = [i/max_rgb for i in star_rgb]

    return reduced_rgb

# #288 [Intermediate] Stars and Stripes and Vertices
# https://www.reddit.com/r/dailyprogrammer/comments/589txl/20161019_challenge_288_intermediate_stars_and/

from PIL import Image, ImageDraw
import numpy as np
from math import floor

center = np.array([100, 100])
radius = 75


def find_vertices(center, radius, n):
    angles = np.array(range(0, n)) * 360 / n + 90
    xs = np.cos(angles * np.pi / 180) * radius + center[0]
    ys = np.sin(angles * np.pi / 180) * radius + center[1]
    return list(zip(list(xs), list(ys)))


def draw_a_star(points, bonus=False):
    new_image = Image.new('RGBA', (200, 200), (255, 255, 255, 0))
    draw = ImageDraw.Draw(new_image)
    for i, point in enumerate(points):
        l = len(points)
        k = floor(l / 2) if not l % 2 == 0 else int(l / 2 - 1)
        pointlist = [points[(i - k) % l], point, points[(i + k) % l]]
        draw.line(pointlist, fill='#ff0000')
    if bonus:
        draw.line(points + [points[0]], fill='#ff0000')
    extra = "+" if bonus else ""
    filename = "star_" + str(l) + extra
    new_image.save(filename, "JPEG")


inputs = [8, 7, 20]
for inp in inputs:
    draw_a_star(find_vertices(center, radius, inp), bonus=True)

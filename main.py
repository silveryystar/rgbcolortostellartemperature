from rgb import reduce_star_rgb
from fit_temp import get_data, get_temp

reduced_rgb = reduce_star_rgb()
r, g, b, x, y, z = get_data(reduced_rgb)
temp1, temp2, temp = get_temp(r, g, b, x, y, z)

print(f"RGB: {reduced_rgb}")
print(f"Estimated R/B Temperature: {temp2} K")
print(f"Estimated G Temperature: {temp1} K")
print(f"Estimated Mean Temperature: {temp} K")

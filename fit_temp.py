import numpy as np
from data import x1, y1, z1, x2, y2, z2


def get_data(reduced_rgb):
    r = reduced_rgb[0]
    g = reduced_rgb[1]
    b = reduced_rgb[2]

    if r == 1:
        x = np.array(x1)
        y = np.array(y1)
        z = np.array(z1)

    elif b == 1:
        x = np.array(x2)
        y = np.array(y2)
        z = np.array(z2)

    else:
        ValueError("Green-dominant; cannot accurately derive temperature.")
        quit()

    return r, g, b, x, y, z


def get_temp(r, g, b, x, y, z):
    i, j, k, l, m, n, o, p, q, s, t = np.polyfit(x, z, 10)
    temp1 = i*g**10 + j*g**9 + k*g**8 + l*g**7 + m*g**6 + n*g**5 + o*g**4 + p*g**3 + q*g**2 + s*g + t

    if r == 1:
        x = b

    else:
        x = r

    i, j, k, l, m, n, o, p, q, s, t = np.polyfit(y, z, 10)
    temp2 = i*x**10 + j*x**9 + k*x**8 + l*x**7 + m*x**6 + n*x**5 + o*x**4 + p*x**3 + q*x**2 + s*x + t

    temp = (temp1+temp2)/2

    return temp1, temp2, temp

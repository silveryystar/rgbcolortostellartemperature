import numpy as np
import matplotlib.pyplot as plt
from data import x1, y1, z1, x2, y2, z2


def plots():
    x = np.array(x1)
    y = np.array(y1)
    z = np.array(z1)

    plt.axhline(1, 0, (6100-2300)/55000, color="r", label="R")
    plt.plot(z, x, color="g", label="G")
    plt.plot(z, y, color="b", label="B")

    x = np.array(x2)
    y = np.array(y2)
    z = np.array(z2)

    plt.axhline(1, (6200-2300)/55000, 1, color="b")
    plt.plot(z, x, color="g")
    plt.plot(z, y, color="r")

    plt.xlim(2300, 55000)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Color (RGB)")
    plt.title("Main Sequence Stellar Color-Temperature Relation")
    plt.legend()
    plt.show()


plots()

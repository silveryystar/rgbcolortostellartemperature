# Stellar Temperature via RGB Color
A tool to estimate stellar temperature through RGB color interpolation of optical-band stellar astrophotography.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter ```pip install pillow```.
5. Enter ```pip install numpy```.
6. Enter ```pip install matplotlib```.
7. Enter ```python main.py```.

# Usage
Run *main.py* via ```python main.py``` in Terminal.
```Image:``` will print.
Enter the image of the star to determine its temperature.

In the background, the program will find the RGB median of the image.
All pixels with RGB values less than or equal to the median compose the background.
The leftover pixels compose the star.
After, background pixels are averaged and subtracted from the star pixels.
The star pixels are then averaged and normalized, producing the average rgb color of the star.
The average RGB color will print as ```RGB: [R, G, B]```.

Using literature color values of solar metallicity model stars (see https://arxiv.org/pdf/2101.06254.pdf, Table 5), temperature is interpolated via two of four ten-polynomial best fits of the color-temperatures (R^2 = 1).
For a red-dominant star (low temperature), regressions between T = 2300 and 6100 K is used for green and blue color-temperature.
For a blue-dominant star (high temperature), regressions between T = 6200 and 55000 K is used for red and green color-temperature.
The program does not support temperature interpolation for green-dominant stars.

After interpolating, the program will print three temperatures.
The first is an estimated temperature based on the red/blue color value, and the second is based on the green color value.
The third temperature is an average between the two temperatures.

In particular, ```Estimated R/B Temperature: x```, ```Estimated G Temperature: y``` and ```Estimated Mean Temperature: (x+y)/2``` will print.
Here, ```x``` and ```y``` are the interpolated temperatures.

This program thrives at determining low stellar temperatures (T < 10000 K), usually correct within ±1000 K.
At higher temperatures, the program struggles to produce accurate results.
This is likely because the red and green color values converge for high-temperature stars, while the blue color value saturates.
This trend is shown in *Figure_0* in the repository. 
Thus, it is recommended to run the program on stars with stellar class no greater than A0V.

# Example
Suppose we want to estimate the temperature of Betelgeuse, a star with a literature temperature of approximately 3600 K (see https://arxiv.org/pdf/2002.10463.pdf).
An image of Betelgeuse (credit: ESO VLT, see https://www.eso.org/public/images/eso2003b/) taken in the visible wavelength of the electromagnetic spectrum is located in the repository as *betelgeuse.png*.

Run *main.py* via ```python main.py``` in Terminal.
When ```Image:``` prints, enter ```betelgeuse.png```.

After a minute, ```RGB: [1.0, 0.49992481700575797, 0.662027121892179]``` will print, indicating that the program has found the average RGB value of the star.
After a few seconds, ```Estimated R/B Temperature: 5027.797278333193 K```, ```Estimated G Temperature: 2288.3719642162323 K```, and ```Estimated Mean Temperature: 3658.084621274713 K``` will print.
These are the solutions to the temperature of Betelgeuse via RGB color interpolation.

# Errors
1. ```Green dominant; cannot accurately derive temperature```.
Solution: Try another star or reduce background oneself; the program cannot interpolate green-dominant stars.
2. ```FileNotFoundError: [Errno 2] No such file or directory```.
Solution: Enter the correct file name, including directory if not located in repository folder.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.

# Cartoon-Image
## Introduction
This program trensforms photos to cartoon like images using the Bilateral Filter which is an  a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It 
replaces the intensity of each pixel with a weighted average of intensity values from 
nearby pixels. This weight can be based on a Gaussian distribution. Crucially, the 
weights depend not only on Euclidean distance of pixels, but also on the radiometric 
differences (e.g., range differences, such as color intensity, depth distance, etc.).

### Definition of the Bilater Filter [1]

$$
h(x) = k^{-1}(x) \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(\xi) c(\xi, x) s(f(\xi), f(x))  d\xi 
$$

**Normalization Term**

$$
k(x) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} c(\xi, x) s(f(\xi), f(x))  d\xi 
$$

#### Where:
- **$h(x)$** is the filtered output signal
- **$f(x)$** is the original input signal
- **$c(\xi, x)$** is the closeness (spatial) kernel measuring geometric distance between $\xi$ and $x$
- **$s(f(\xi), f(x))$** is the similarity (range) kernel measuring photometric similarity
- **$k(x)$** is the normalization factor ensuring filter weights sum to 1

To remove noise, the bilateral filter gives each pixel a new value based on the average of its closest matching neighbors.
In parts of the image that are already smooth and uniform, it simply blurs the area, which has the effect of smoothing out the random noise.


## References
[1] C. Tomasi and R. Manduchi, "Bilateral filtering for gray and color images," Sixth International Conference on Computer Vision (IEEE Cat. No.98CH36271), Bombay, India, 1998, pp. 839-846, doi: 10.1109/ICCV.1998.710815. keywords: {Filtering;Color;Low pass filters;Photometry;Imaging phantoms;Pixel;Shape measurement;Smoothing methods;Computer science;Humans},


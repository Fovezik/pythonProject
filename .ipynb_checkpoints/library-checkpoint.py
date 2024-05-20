import scikit_build_example as clib
import numpy as np
import imageio.v3 as im
import matplotlib.pyplot as plt


# audio = clib.read_audio("test-audio.wav", 5)
# clib.plot_line(audio.time, audio.wave)

# generated_wave = clib.generate_wave('sine', 0.1)
# clib.plot_line(generated_wave.time, generated_wave.wave)

# generated_wave = clib.generate_wave('cosine', 1)
# clib.plot_line(generated_wave.time, generated_wave.wave)

# generated_wave = clib.generate_wave('square', 2)
# clib.plot_line(generated_wave.time, generated_wave.wave)

# generated_wave = clib.generate_wave('sawtooth', 4)
# clib.plot_line(generated_wave.time, generated_wave.wave)

# generated_wave = clib.generate_wave('test', 0.67)
# clib.plot_line(generated_wave.time, generated_wave.wave)

input_image = im.imread("test-image.jpg")

print(input_image.shape)
input_image_plt = plt.imshow(input_image)
plt.show()

kernel = np.random.rand(3, 3, 3, 1).astype(np.float32)
convolved_image = clib.convolve(input_image, kernel)
print(convolved_image.shape)
output_image_plt = plt.imshow(convolved_image)
plt.show()

kernel_size = 5
sigma = 5
gaussian_filtered_image = clib.gaussian_filter(input_image, kernel_size, sigma)
print(gaussian_filtered_image.shape)
gaussian_image_plt = plt.imshow(gaussian_filtered_image)
plt.show()




import scikit_build_example as clib
import imageio.v3 as im
import matplotlib.pyplot as plt


frequency = 1

sinus = clib.generate_wave('sine', frequency)
clib.plot_line(sinus.time, sinus.wave)

cosinus = clib.generate_wave('cosine', frequency)
clib.plot_line(cosinus.time, cosinus.wave)

square = clib.generate_wave('square', frequency)
clib.plot_line(square.time, square.wave)

sawtooth = clib.generate_wave('sawtooth', frequency)
clib.plot_line(sawtooth.time, sawtooth.wave)

audio = clib.read_audio("inputs\\test-audio.wav")
clib.plot_line(audio.time, audio.wave)

filtered_audio = clib.lowpass_filter(audio, 100)
clib.plot_line(filtered_audio.time, filtered_audio.wave)

input_image = im.imread("inputs\\test-image.jpg")
plt.imshow(input_image)
plt.savefig("outputs\\test-image.jpg")
plt.show()

gaussian_filtered_image = clib.gaussian_filter(input_image, 3)
plt.imshow(gaussian_filtered_image)
plt.savefig("outputs\\test-image-gaussian.jpg")
plt.show()

grayscale_image = clib.grayscale(input_image)
plt.imshow(grayscale_image, cmap='gray')
plt.savefig("outputs\\test-image-grayscale.jpg")
plt.show()

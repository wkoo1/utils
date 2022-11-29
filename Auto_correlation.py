import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
plt.rcParams['figure.dpi'] = 150
pic = Image.open('1drawio.png').convert('L')
image = np.asarray(pic)
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
iff = np.fft.ifft2(f)
#AC = np.fft.ifft2(np.abs(f) ** 2 )
#AC = np.fft.ifftshift(AC)
#上面两行与下面两行效果相同。
AC = np.fft.ifft2(np.abs(f) ** 2 )
AC = np.fft.fftshift(AC)

plt.subplot(221)
plt.imshow(image,cmap='gray')
plt.title('Origin Image')
plt.axis('off')
plt.subplot(222)
plt.imshow(abs(AC),cmap='hot')
plt.title('AutoCorrelation')
plt.axis('off')
plt.show()
plt.subplot(223)
plt.imshow(20 * np.log(np.abs(fshift)),cmap='gray')
plt.axis('off')
plt.title('Fourier Transform')
plt.subplot(224)
plt.imshow(np.abs(iff),cmap='gray')
plt.title('ifft2')
plt.axis('off')
plt.show()


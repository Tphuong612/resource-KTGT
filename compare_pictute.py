import cv2
import numpy as np

# Đọc 2 ảnh
img1 = cv2.imread('hoadao.jpg')
img2 = cv2.imread('output.png')

# So sánh từng pixel
equal_pixels = np.all(img1 == img2, axis=2)  # Trả về True tại pixel giống nhau

# Đếm số pixel giống nhau
num_equal = np.sum(equal_pixels)
total_pixels = img1.shape[0] * img1.shape[1]
percentage = (num_equal / total_pixels) * 100

print(f"Số pixel giống nhau: {num_equal}")
print(f"Tỉ lệ phần trăm giống nhau: {percentage:.2f}%")

# Tạo ảnh mask thể hiện vùng giống nhau (trắng) và khác nhau (đen)
mask = (equal_pixels * 255).astype(np.uint8)
cv2.imwrite('similar_mask.png', mask)

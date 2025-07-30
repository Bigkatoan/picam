import cv2
from picamera2 import Picamera2
import time

# 1. Khởi tạo và cấu hình camera
picam2 = Picamera2()
# Cấu hình camera để xem trước, kích thước 640x480
# Định dạng "main" sẽ là luồng chính để lấy khung hình cho OpenCV
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)

# Bắt đầu chạy camera
picam2.start()

# Thêm một chút thời gian chờ để camera ổn định
time.sleep(1)

# 2. Vòng lặp để xử lý video thời gian thực
while True:
    # Lấy khung hình từ camera dưới dạng mảng NumPy (định dạng BGR mặc định của OpenCV)
    frame = picam2.capture_array()

    # --------------------------------------------------
    # --- THÊM MÃ OPENCV CỦA BẠN TẠI ĐÂY ---
    # Ví dụ: chuyển đổi hình ảnh sang ảnh xám
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # --------------------------------------------------

    # Hiển thị khung hình gốc trong một cửa sổ
    cv2.imshow("Camera Goc", frame)
    # Hiển thị khung hình đã xử lý (ảnh xám) trong cửa sổ khác
    cv2.imshow("Anh Xam", gray_frame)


    # Chờ phím 'q' được nhấn để thoát khỏi vòng lặp
    # cv2.waitKey(1) rất quan trọng để cửa sổ imshow có thể cập nhật
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 3. Dọn dẹp tài nguyên
print("Dừng chương trình...")
cv2.destroyAllWindows()
picam2.stop()
import time
from picamera2 import Picamera2

NUM_FRAMES = 500
RESOLUTION = (640, 480)

# --- Khởi tạo camera ---
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": RESOLUTION})
picam2.configure(config)
picam2.start()

# Chờ camera khởi động và ổn định
print("Camera đang khởi động...")
time.sleep(1.0)
print("Bắt đầu kiểm tra FPS...")

frame_count = 0
start_time = time.time()

while frame_count < NUM_FRAMES:
    frame = picam2.capture_array()
    frame_count += 1

# --- Tính toán và hiển thị kết quả ---
end_time = time.time()
elapsed_time = end_time - start_time
fps = frame_count / elapsed_time

print("---------------------------------")
print(f"Đã bắt được: {frame_count} khung hình")
print(f"Thời gian thực thi: {elapsed_time:.2f} giây")
print(f"FPS (không hiển thị): {fps:.2f}")
print("---------------------------------")

# Dừng camera
picam2.stop()
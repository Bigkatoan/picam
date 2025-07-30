# Picam: Tự động cài đặt Môi trường Camera cho Raspberry Pi
Dự án này cung cấp một kịch bản (script) để tự động hóa việc thiết lập một môi trường phát triển hoàn chỉnh cho Camera Module của Raspberry Pi. Script sẽ cài đặt Picamera2, OpenCV, và Jupyter Lab vào bên trong một môi trường ảo Python (venv) riêng biệt.

## ⚙️ Yêu cầu
Phần cứng
Raspberry Pi (Khuyến nghị Model 3, 4, 5 hoặc Zero 2 W)

Raspberry Pi Camera Module đã được kết nối

Phần mềm
Hệ điều hành Raspberry Pi OS (Khuyến nghị bản "Bookworm" hoặc mới hơn)

## 🚀 Hướng dẫn cài đặt
Kịch bản cài đặt sẽ tự động tải về, cấp quyền và chạy để thiết lập toàn bộ môi trường cho bạn.

Mở Terminal trên Raspberry Pi và chạy các lệnh sau:

# Tải về kịch bản cài đặt
```
wget https://raw.githubusercontent.com/Bigkatoan/picam/refs/heads/main/setup.bash
```
# Cấp quyền thực thi cho kịch bản
```
chmod +x setup.bash
```
# Chạy kịch bản
```
./setup.bash
```
# Dọn dẹp file cài đặt sau khi hoàn tất
```
rm setup.bash
```
Kịch bản sẽ thực hiện tất cả các bước cần thiết, bao gồm cài đặt gói hệ thống, tạo môi trường ảo và cài đặt các thư viện Python.

🐍 Cách sử dụng
Sau khi quá trình cài đặt hoàn tất, bạn có thể khởi động Jupyter Lab để bắt đầu lập trình.

Tìm địa chỉ IP của Raspberry Pi
Cách đơn giản nhất là sử dụng lệnh hostname:
```
hostname -I
```
Lệnh này sẽ trả về địa chỉ IP của Pi (ví dụ: 192.168.1.10).

Khởi động Jupyter Lab
Chạy lệnh sau trong Terminal:
```
jupyter-lab --ip <your-pi-ip>
```
Lưu ý: Thay thế <your-pi-ip> bằng địa chỉ IP bạn tìm được ở bước trên.

Truy cập môi trường làm việc
Sau khi chạy, Terminal sẽ hiển thị một đường dẫn URL (có chứa token đăng nhập). Hãy sao chép và dán đường dẫn này vào trình duyệt web trên một máy tính khác trong cùng mạng LAN để bắt đầu sử dụng Jupyter Lab.

import cv2

# Kết nối đến webcam mặc định
cap = cv2.VideoCapture(0)

# Kiểm tra xem camera có mở được không
if not cap.isOpened():
    print("Không thể mở camera!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không thể lấy được khung hình từ camera!")
        break

    # Hiển thị khung hình nhận được từ camera
    cv2.imshow("Camera Feed", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
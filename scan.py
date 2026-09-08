import cv2

# Load QR image
img = cv2.imread("qr_codes/qr_2026-05-09_14-11-00.png")

detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)

if data:
    print("QR Content:", data)
    print("Opening image...")
    image = cv2.imread(data)
    cv2.imshow("Captured Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("QR not detected")



"""import cv2
import base64
import os
import numpy as np

qr_folder = "qr_codes"

detector = cv2.QRCodeDetector()

chunks_dict = {}

# 1️⃣ Scan all QR codes
for file in sorted(os.listdir(qr_folder)):
    if file.endswith(".png"):
        img = cv2.imread(os.path.join(qr_folder, file))
        data, _, _ = detector.detectAndDecode(img)

        if data:
            # Format: part/total|base64data
            part_info, chunk = data.split("|")
            part_no, total = part_info.split("/")

            chunks_dict[int(part_no)] = chunk

# 2️⃣ Combine chunks in correct order
full_base64 = ""
for i in range(1, len(chunks_dict) + 1):
    full_base64 += chunks_dict[i]

# 3️⃣ Decode Base64 to image bytes
img_bytes = base64.b64decode(full_base64)
img_array = np.frombuffer(img_bytes, dtype=np.uint8)

# 4️⃣ Reconstruct image
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# 5️⃣ Show image
if image is not None:
    cv2.imshow("Reconstructed Image from QR Codes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to reconstruct image")
"""

"""import cv2

# CHANGE THIS to the QR you want to scan
qr_image_path = "qr_codes/qr_20260119_194515_2.png"

# Load QR image
img = cv2.imread(qr_image_path)

detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)

if data:
    # Data format: part/total|base64data
    part_info, chunk = data.split("|")
    part_no, total = part_info.split("/")

    print("QR SCANNED SUCCESSFULLY")
    print("----------------------")
    print("Part number :", part_no)
    print("Total parts :", total)
    print("Data chunk  :")
    print(chunk)
else:
    print("QR code not detected")
"""



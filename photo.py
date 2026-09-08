import cv2
import base64
import os
import numpy as np

qr_folder = "qr_codes"
detector = cv2.QRCodeDetector()

chunks = {}
capture_id = None
total_parts = None

for file in sorted(os.listdir(qr_folder)):
    if file.endswith(".png"):
        img = cv2.imread(os.path.join(qr_folder, file))
        data, _, _ = detector.detectAndDecode(img)

        if not data:
            continue

        cap_id, part_info, chunk = data.split("|")
        part_no, total = part_info.split("/")

        if capture_id is None:
            capture_id = cap_id
            total_parts = int(total)

        # Ignore mixed captures
        if cap_id != capture_id:
            continue

        chunks[int(part_no)] = chunk

# Validate
if len(chunks) != total_parts:
    print("ERROR: Missing QR codes")
    print("Expected:", total_parts, "Found:", len(chunks))
    exit()

# Combine Base64 safely
full_base64 = "".join(chunks[i] for i in range(1, total_parts + 1))

# Decode Base64
img_bytes = base64.b64decode(full_base64)
img_array = np.frombuffer(img_bytes, dtype=np.uint8)

# Decode PNG image
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

if image is None:
    print("ERROR: Image reconstruction failed")
else:
    cv2.imshow("Reconstructed Image (FIXED)", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

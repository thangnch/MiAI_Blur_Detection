import cv2

# Duong dan den file anh
image_file= "test01.jpg"
# Dinh nghia blur threshold
blur_threshold=100

# Doc anh tu file
image = cv2.imread(image_file)
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Tinh toan muc do focus cua anh
focus_measure = cv2.Laplacian(gray, cv2.CV_64F).var()

if focus_measure < blur_threshold:
    text = "Blurry pix"
    cv2.putText(image, "{} - FM = {:.2f}".format(text, focus_measure), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

else:
    text = "Fine pix"
    cv2.putText(image, "{} - FM = {:.2f}".format(text, focus_measure), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

# Hien thi anh
cv2.imshow("Image", image)
key = cv2.waitKey(0)
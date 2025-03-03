import cv2
from PIL import Image
from pytesseract import pytesseract
from new import result
camera = cv2.VideoCapture(1)
test=None
while True:
    session, image = camera.read()
    cv2.imshow('Text Detection', image)
    if cv2.waitKey(1000) & 0xFF == ord('s'):
        cv2.imwrite('Text.jpg', image)
        break

camera.release()
cv2.destroyAllWindows()


def tesseract():
    path = r"E:\New folder\tesseract.exe"
    pytesseract.tesseract_cmd = path
    image_path = "Text.jpg"
    test = pytesseract.image_to_string(Image.open(image_path))
    print(test)
    #test = "5-45*2/5-2-3/3*9"
    result(test)
    # print(len(test))


tesseract()

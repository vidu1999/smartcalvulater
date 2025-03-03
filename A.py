import cv2
import pytesseract

# initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # read a frame from the camera
    ret, frame = cap.read()

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply thresholding to the grayscale image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # apply some morphological operations to the thresholded image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)

    # find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # loop over the contours
    for cnt in contours:
        # get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(cnt)

        # draw the bounding box on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # extract the number from the bounding box using pytesseract
        number = pytesseract.image_to_string(gray[y:y + h, x:x + w], config='--psm 10')

        # print the number
        print(number)

    # show the frame
    cv2.imshow('frame', frame)

    # exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

import joblib
import cv2
import pandas as pd


def image_preprocess(im_path):
    im = cv2.imread(im_path)
    blur_img = cv2.GaussianBlur(im, (5, 5), 2)
    gray_img = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, 1, 2)
    areas = []
    for i in range(5):
        try:
            areas.append(str(cv2.contourArea(contours[i])))
        except:
            areas.append("0")
    return areas


def detect(image):
    print(image)
    classifier = joblib.load("rf_malaraia_100_5")
    lst = image_preprocess(image)
    df = pd.DataFrame([lst], columns=["area_0", "area_1", "area_2", "area_3", "area_4"])
    return classifier.predict(df)


# print(detect('static/uploads/malaria-1.png'))

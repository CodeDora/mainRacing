import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui #gerekli kütüphaneleri ekledim

detector = HandDetector(detectionCon=0.5, maxHands=2)
cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 400) # kamera boyutları 

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]  # İlk algılanan eli seçiyoruz
        fingers = detector.fingersUp(hand)  # Parmakların durumunu alıyoruz
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2) # gözüken parmak konum değerlerini düzenliyoruz

        if totalFingers == 5: # avuç açık kapamayı parmak hareketleriyle anlaşılmasını sağlıyoruz
            pyautogui.keyDown("right") 
            pyautogui.keyUp('left')
        if totalFingers == 0:
            pyautogui.keyDown('left')
            pyautogui.keyUp("right")

    cv2.imshow("Kamera", img) # pencereyi ekranda göster
    cv2.waitKey(1)

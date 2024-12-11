import cv2
import mediapipe as mp
import time
import math
import pyttsx3  

engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('volume', 1)  


from questions import questions 

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,1200)

mphands = mp.solutions.hands
hands = mphands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpdraw = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
qno = 0
last_ans = None
wait = True
give = "hello"
skip = ""
answered = False
with open("ans.txt", 'w') as file:
    
    while qno< len(questions):
        
        success, img = cam.read()
        if not success:
            print("Failed to grab frame")
            break
        
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        results = hands.process(imgRGB)
        if not answered:
            engine.say(questions[qno])
            engine.runAndWait()
            answered = True
        if results.multi_hand_landmarks:

                for handlms in results.multi_hand_landmarks:
                    mpdraw.draw_landmarks(img, handlms, mphands.HAND_CONNECTIONS)
                
                    lm4 = handlms.landmark[4] 
                    lm8 = handlms.landmark[8] 
                    lm12 = handlms.landmark[12]
                    lm16 = handlms.landmark[16]
                    lm20 = handlms.landmark[20]
                    lm6 = handlms.landmark[6]
                    lm10 = handlms.landmark[10]
                    lm14 = handlms.landmark[14]
                    lm18 = handlms.landmark[18]
                    lm3 = handlms.landmark[3]
                    lm17 = handlms.landmark[17]
                    
                    c1x = int(lm4.x * img.shape[1])  
                    c1y = int(lm4.y * img.shape[0])  

                    c2x = int(lm8.x * img.shape[1])
                    c2y = int(lm8.y * img.shape[0])  

                    c3x = int(lm12.x * img.shape[1])  
                    c3y = int(lm12.y * img.shape[0])  

                    c4x = int(lm16.x * img.shape[1])  
                    c4y = int(lm16.y * img.shape[0])  

                    c5x = int(lm20.x * img.shape[1])  
                    c5y = int(lm20.y * img.shape[0]) 

                    c6x = int(lm6.x * img.shape[1])  
                    c6y = int(lm6.y * img.shape[0])

                    c7x = int(lm10.x * img.shape[1])  
                    c7y = int(lm10.y * img.shape[0])

                    c8x = int(lm14.x * img.shape[1]) 
                    c8y = int(lm14.y * img.shape[0])

                    c9x = int(lm18.x * img.shape[1])
                    c9y = int(lm18.y * img.shape[0])

                    c10x = int(lm3.x * img.shape[1])  
                    c10y = int(lm3.y * img.shape[0])

                    c17x = int(lm17.x * img.shape[1])  
                    c17y = int(lm17.y * img.shape[0])

                    cv2.circle(img, (c1x, c1y), 15, (255, 0, 255), -1)  
                    cv2.circle(img, (c2x, c2y), 15, (255, 0, 255), -1)  
                    cv2.circle(img, (c3x, c3y), 15, (255, 0, 255), -1) 
                    cv2.circle(img, (c4x, c4y), 15, (255, 0, 255), -1) 
                    cv2.circle(img, (c5x, c5y), 15, (255, 0, 255), -1)
                    


                    cv2.line(img, (c1x, c1y), (c2x, c2y), (255, 0, 0), 1)
                    cv2.line(img, (c1x, c1y), (c3x, c3y), (255, 0, 0), 1)
                    cv2.line(img, (c1x, c1y), (c4x, c4y), (255, 0, 0), 1)
                    cv2.line(img, (c1x, c1y), (c5x, c5y), (255, 0, 0), 1)

                    
                    a = int(math.hypot((c2x - c1x), (c2y - c1y)))
                    b = int(math.hypot((c3x - c1x), (c3y - c1y)))
                    c = int(math.hypot((c4x - c1x), (c4y - c1y)))
                    d = int(math.hypot((c5x - c1x), (c5y - c1y)))
                    

                    if a < 30:
                        ans = "A"
                    elif b < 30:
                        ans = "B"
                    elif c < 30:
                        ans = "C"
                    elif d < 30:
                        ans = "D"
                    
                    else:
                        ans = "not any ans..."
                    
        
                    if c1y<c2y and c1y<c3y and c1y<c4y and c1y<c5y and c2x>c6x and c3x>c7x and c4x> c8x and c5x>c9x:
                        cv2.putText(img, "Thumbs Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                        give = "yes"
                        engine.say("yes you are now ready to answer")
                        engine.runAndWait()
                        time.sleep(3)
                        
                    elif c1y>c2y and c1y>c3y and c1y>c4y and c1y>c5y and c2x>c6x and c3x>c7x and c4x> c8x and c5x>c9x:
                        cv2.putText(img, "Thumbs Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                        give = "no"
                        engine.say("Moving to next question")
                        engine.runAndWait()
                        qno +=1
                        answered= False
                        time.sleep(3)
                        
                    
                    
                    
                    if give=="yes":
                        
                        if ans != "not any ans..." and wait :
                    
                            
                            file.write(f"for question no {qno + 1}\n {questions[qno]}:\n Your answer is {ans};\n\n")
                            last_ans = ans
                            print(f"Answer for Question {qno + 1}: {ans}")
                            engine.say(f"Your answer for this question{qno + 1} is {ans}")
                            engine.runAndWait()
                            
                            qno += 1
                            wait = False
                            answered = False
                            time.sleep(2)
                    if not wait:
                         time.sleep(0)
                         wait = True
                    if not give:
                        give = "hello"
     
        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        
            
engine.say("The exam is over. Hope your exam goes well!!!")
engine.runAndWait()
cam.release()
cv2.destroyAllWindows()

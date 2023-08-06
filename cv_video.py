import cv2
import numpy as np
import datetime


if __name__ == '__main__':
    
    img_count = 0
    cap = cv2.VideoCapture('rtsp://admin:admin123@192.168.123.228:554/cam/realmonitor?channel=2&subtype=0&unicast=true&proto=Onvif')
    w  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float `height`

    s = min(int(w / 8), int(h / 8))
    CROSS_W = s
    CROSS_H = s

    RETICLE_W_SIZE = int(w / 7)
    RETICLE_H_SIZE = int(w / 7)
    DELTA = 40
    SHIFT = 30
    DASH = 100

    while(True):
        ret, frame = cap.read()
        text_color = (255,0,0)
        c1 = int(w/2)
        c2 = int(h/2)

        x1 = int(w/2 - CROSS_W/2)
        y1 = int(h/2)

        x11 = int(w/2 - CROSS_W/2 + DASH/2)
        y11 = int(h/2)

        x2 = int(w/2 + CROSS_W/2)
        y2 = int(h/2)

        x21 = int(w/2 + CROSS_W/2 - DASH/2)
        y21 = int(h/2)

        x3 = int(w/2)
        y3 = int(h/2 - CROSS_H/2)

        x31 = int(w/2)
        y31 = int(h/2 - CROSS_H/2 + DASH/2)

        x4 = int(w/2)
        y4 = int(h/2 + CROSS_H/2)

        x41 = int(w/2)
        y41 = int(h/2 + CROSS_H/2 - DASH/2)

        x5 = int(w/2 - RETICLE_W_SIZE/2 - SHIFT)
        y5 = int(h/2 - RETICLE_H_SIZE/2)

        x51 = int(w/2 - RETICLE_W_SIZE/2 - SHIFT)
        y51 = int(h/2 - RETICLE_H_SIZE/2 +  DELTA)

        x52 = int(w/2 - RETICLE_W_SIZE/2 -SHIFT + DELTA)
        y52 = int(h/2 - RETICLE_H_SIZE/2)


        x6 = int(w/2 + RETICLE_W_SIZE/2 + SHIFT)
        y6 = int(h/2 - RETICLE_H_SIZE/2)

        x61 = int(w/2 + RETICLE_W_SIZE/2 + SHIFT)
        y61 = int(h/2 - RETICLE_H_SIZE/2 +  DELTA)

        x62 = int(w/2 + RETICLE_W_SIZE/2 + SHIFT - DELTA)
        y62 = int(h/2 - RETICLE_H_SIZE/2)

        x7 = int(w/2 - RETICLE_W_SIZE/2 - SHIFT)
        y7 = int(h/2 + RETICLE_H_SIZE/2)

        x71 = int(w/2 - RETICLE_W_SIZE/2 - SHIFT)
        y71 = int(h/2 + RETICLE_H_SIZE/2 -  DELTA)

        x72 = int(w/2 - RETICLE_W_SIZE/2 - SHIFT + DELTA)
        y72 = int(h/2 + RETICLE_H_SIZE/2)

        x8 = int(w/2 + RETICLE_W_SIZE/2 + SHIFT)
        y8 = int(h/2 + RETICLE_H_SIZE/2)

        x81 = int(w/2 + RETICLE_W_SIZE/2 - SHIFT + DELTA)
        y81 = int(h/2 + RETICLE_H_SIZE/2)

        x82 = int(w/2 + RETICLE_W_SIZE/2 + SHIFT)
        y82 = int(h/2 + RETICLE_H_SIZE/2 - DELTA) 

        #cv2.line(frame,(x1,y1),(x2,y2),(255,255,255),1,cv2.LINE_AA)
        #cv2.line(frame,(x3,y3),(x4,y4),(255,255,255),1,cv2.LINE_AA)
        cv2.circle(frame, (c1,c2), radius=0, color=(255, 255, 255), thickness=-1)
        cv2.line(frame,(x1,y1),(x11,y11),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x2,y2),(x21,y21),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x3,y3),(x31,y31),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x4,y4),(x41,y41),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x5,y5),(x51,y51),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x5,y5),(x52,y52),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x6,y6),(x61,y61),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x6,y6),(x62,y62),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x7,y7),(x71,y71),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x7,y7),(x72,y72),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x8,y8),(x81,y81),(255,255,255),1,cv2.LINE_AA)
        cv2.line(frame,(x8,y8),(x82,y82),(255,255,255),1,cv2.LINE_AA)

        cv2.putText(frame,'Thermal IR',(64,64),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        now = datetime.datetime.now()
        cv2.putText(frame,str(now),(w - 380,64),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("frame%d.jpg" % img_count, frame)
            img_count = img_count + 1
            print("save one frame ok!")
            
    

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
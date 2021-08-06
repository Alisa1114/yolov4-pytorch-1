import time
import threading
import cv2
import numpy as np
from PIL import Image

from yolo import YOLO
from tools.alarm import alarm
from tools.save_csv import save_record
from tools.client import client

if __name__ == "__main__":
    """
    這是用來捕捉攝影機畫面並將畫面送進模型預測的程式
    """
    yolo = YOLO()
    cnt_x = 0
    client_cnt = 0
    cap = cv2.VideoCapture(0)
    start = time.time()
    start_client = time.time()
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frame_pil = Image.fromarray(np.uint8(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)))
            frame, count_OX = yolo.detect_image(frame_pil)
            frame = cv2.cvtColor(np.asarray(frame),cv2.COLOR_RGB2BGR)
            cv2.imshow("Camera",frame)
            
            if count_OX[0][1] >= 1:
                cnt_x += 1
            elif count_OX[0][1] == 0:
                cnt_x = 0
            if cnt_x >= 30:
                cnt_x = 0
                t = threading.Thread(target = alarm)
                t.start()
                client_cnt += 1
            if (time.time() - start_client) >= 10.0:
                print(time.time() - start_client)
                if client_cnt >= 1:
                    t = threading.Thread(target = client)
                    t.start()
                    client_cnt = 0
                start_client = time.time()
            
            if (time.time() - start) >= 30.0:
                t = threading.Thread(target = save_record, args = (count_OX,))
                t.start()
                start = time.time()
            
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
import time
import csv
import numpy as np

def save_record(count):
    # count.shape = (1, 2)
    # 裡面個別紀錄有穿和沒穿的數量
    # count[0][0]為有穿的數量，count[0][1]為沒穿的數量
    date_record = str(time.strftime("%Y-%m-%d", time.localtime()))
    time_record = str(time.strftime("%H:%M:%S", time.localtime()))
    total_num = count.sum()
    
    with open('tools/record.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date_record, time_record, total_num, count[0][0], count[0][1]])
        
if __name__ == '__main__':
    save_record(np.array([[1, 5]]))
    time.sleep(10)
    save_record(np.array([[7,16]]))
    time.sleep(10)
    save_record(np.array([[2,12]]))
    time.sleep(10)
    save_record(np.array([[8,36]]))
    time.sleep(10)
    save_record(np.array([[51, 3]]))
    time.sleep(10)
    save_record(np.array([[0,0]]))
    time.sleep(10)
    save_record(np.array([[8,8]]))
    time.sleep(10)
    save_record(np.array([[9,14]]))
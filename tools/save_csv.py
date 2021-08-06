import time
import csv

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
    
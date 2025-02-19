# เวลาใช้งานวาง payload ไว้ใน obj แล้วรัน python3 deseri.py
import pickle5 as pickle

desir_me = b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00\x8c\x13serialize me please\x94.'
res = pickle.loads(desir_me)
print(res)

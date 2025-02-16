# เวลาใช้งานวาง payload ไว้ใน obj แล้วรัน python3 seri.py
import pickle5 as pickle

obj = "serialize me please"
results = pickle.dumps(obj)
print(results)

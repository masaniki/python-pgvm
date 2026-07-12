#Pythonの挙動を確認するようのmain file。
import json

str01={"appple":1, "banana":2, "orange":3}
with open("sample.txt",mode="w",encoding="utf-8") as f:
  print(type(f))
  jsonStr01=json.dump(str01,f,indent="abc")
print(type(jsonStr01))

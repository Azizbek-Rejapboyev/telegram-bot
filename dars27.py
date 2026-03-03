import json

with open('hozir.json', 'r', encoding="UTF-8") as file:
    fanlar = json.load(file)
while True:
    print(f"[{fanlar['test_nomi']}]")
    for fan in fanlar['fanlar']:
        for i in range(1, 6):
            
        print(i, fan['fan_nomi'])
    break
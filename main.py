import time

print("Запуск Python-парсера внутри Docker...", flush=True)

counter = 1
while True:
	print(f"[{counter}] Работаю... Собираю данные с сайта...", flush=True)
	time.sleep(3)
	counter +=1

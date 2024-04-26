import queue
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()

# Функція генерації заявки
def  generate_request():
     request_id = random.randint(1, 500)  # Генеруємо унікальний ідентифікатор заявки
     request_queue.put(request_id) # Додаємо заявку до черги
     print(f"Заявка {request_id} додана до черги.")
     
# Функція обробки заявки
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()  # Видаляємо заявку з черги
        print(f"Заявка {request_id} оброблена.")
    else:
        print("Черга порожня.")
    
    
    
# Головний цикл програми
while True:
    generate_request()  # Генеруємо нові заявки
    time.sleep(random.uniform(0.5, 2))  # Затримка для симуляції часу між заявками
    process_request()  # Обробляємо заявки
    time.sleep(random.uniform(0.5, 2))  # Затримка для симуляції часу обробки заявки




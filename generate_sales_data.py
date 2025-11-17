import random
from datetime import datetime, timedelta
import pandas as pd
import string
import os

categories = {
    'Детские товары': ['Машинка', 'Кукла', 'Книга', 'Пазлы'],
    'Бытовая химия': ['Стиральный порошок', 'Мыло', 'Пятновыводитель', 'Отбеливатель'],
    'Текстиль': ['Подушка', 'Одеяло', 'Полотенце', 'Комплект белья'],
    'Напитки': ['Вода', 'Сок', 'Морс', 'Холодный чай'],
    'Бакалея': ['Макароны', 'Крупы', 'Масло', 'Соус']
}

shop_number = [11, 21, 38]

cash_number = [1, 2]

amount_item = [1, 2, 3, 4, 5]
amount_item_probability = [0.5, 0.25, 0.15, 0.05, 0.05]

discount_item = [0, 5, 10]
discount_item_probability = [0.5, 0.3, 0.2]

today = datetime.today()
export_date = (today - timedelta(days=1)).date()

c = 25

if not os.path.exists('data'):
    os.makedirs('data')

for val in shop_number:
  for cash in cash_number:
    file_name = f'{val}_{cash}.csv'
    d = {
      'dt': [export_date.strftime("%d-%m-%Y")] * c,
      'shop_num': [val] * c,
      'cash_num': [cash] * c,
      'doc_id': [],
      'item': [],
      'category': [],
      'amount': [random.choices(amount_item, amount_item_probability, k=1)[0] for _ in range(c)],
      'price': [random.randint(0, 500) for _ in range(c)],
      'discount': [random.choices(discount_item, discount_item_probability, k=1)[0] for _ in range(c)]
    }
    
    unique_doc_ids = [''.join(random.choices(string.digits, k=1)) + random.choice(string.ascii_uppercase) for _ in range(c // 2)]
    d['doc_id'] = [random.choice(unique_doc_ids) if random.random() < 0.8 else ''.join(random.choices(string.digits, k=1)) + random.choice(string.ascii_uppercase) for _ in range(c)]
    for _ in range(c):
      category = random.choice(list(categories.keys()))
      item = random.choice(categories[category])
      d['category'].append(category)
      d['item'].append(item)
    df = pd.DataFrame(d)
    df.to_csv(f'data/{file_name}', index=False)
  

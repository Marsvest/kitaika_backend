# Kitaika website bd + fastapi backend
## Methods
### GetCategories (GET)
```
https://kitaika39.ru/api/getcategories/
```
Получает категории для наполнения меню
```
Возвращает:
name: название категории
image_path: ссылка на картинку
```
### GetProducts (GET)
```
https://kitaika39.ru/api/getproducts/{category_id}
```
Получает товары в выбранной категории
```
Возвращает:
label: название товара
price: цена товара
about: описание товара
image_path: ссылка на картинку
calories: калории в товаре
```
### GetOrders (GET)
```
https://kitaika39.ru/api/getorders/
```
Получает все заказы
```
Возвращает:
ordered_time: время оформление заказа
last_time: время, на которое сделан заказ
phone_number: номер телефона
name: имя
info: дополнительная информация к заказу
address: адрес доставки
take_type: тип выдачи (delivery/pickup) (доставка/самовывоз)
payment_type: тип оплаты (cash/card/online) (наличка/карта/онлайн)
status: статус заказа (in queue/cooking/done/taked) (в очереди/готовится/готов к выдаче/забрали)
items: массив, содержащий поля метода GetItems()
```
### GetItems (GET)
```
https://kitaika39.ru/api/getitems/{order_id}
```
Получает товары в выбранном заказе
```
Возвращает:
product_id: айди продукта 
count: количество продуктов данного типа в заказе
price: суммарная цена продуктов данного типа
product: массив, содержащий поля метода GetProducts()
```
### UpdateOrder (PUT)
```
https://kitaika39.ru/api/updateorder/{order_id}
```
Подтверждает заказ и возвращает его айди
```
Необходимые параметры:
last_time: время, на которое сделан заказ
phone_number: номер телефона
name: имя
info: дополнительная информация к заказу
address: адрес доставки
take_type: тип выдачи (delivery/pickup) (доставка/самовывоз)
payment_type: тип оплаты (cash/card/online) (наличка/карта/онлайн)
```
```
Возвращает:
order_id: айди заказа
```
### OrderInit (POST)
```
https://kitaika39.ru/api/orderinit
```
Инициализирует новый заказ (чтобы потом добавлять товары) и возвращает его айди
```
Возвращает:
order_id: айди заказа
```

### AddToCart (POST)
```
https://kitaika39.ru/api/addtocart
```
Добавляет товары к корзине
```
Необходимые параметры:
order_id: айди заказа
product_id: айди продукта
count: количество продуктов данного типа
```
```
Возвращает:
item_id: айди нового предмета
```
### CreateProduct (POST)
```
https://kitaika39.ru/api/createproduct
```
Создает новый товар
```
Необходимые параметры:
label: название
price: цена за единицу товара
category_id: айти категории
about: описании
image_path: полный путь к картинке
calories: калории
```
```
Возвращает:
item_id: айди товара
```

## Passwords
### mail.ru
kitaika39@mail.ru

UYoATun9b3x}
### reg.ru
kitaika39@mail.ru

3!gCOD2i

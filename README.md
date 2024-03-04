# Kitaika website bd + fastapi backend
## Methods
### GetCategories (GET)
```
http://kitaika39.ru:8000/api/getcategories/
```
Получает категории для наполнения меню
```
name: название категории
image_path: ссылка на картинку
```
### GetProducts (GET)
```
http://kitaika39.ru:8000/api/getproducts/{category_id}
```
Получает товары в выбранной категории
```
label: название товара
price: цена товара
about: описание товара
image_path: ссылка на картинку
calories: калории в товаре
```
### GetOrders (GET)
```
http://kitaika39.ru:8000/api/getorders/
```
Получает все заказы
```
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
http://kitaika39.ru:8000/api/getitems/{order_id}
```
Получает товары в выбранном заказе
```
product_id: айди продукта 
count: количество продуктов данного типа в заказе
price: суммарная цена продуктов данного типа
product: массив, содержащий поля метода GetProducts()
```
### CreateOrder (POST)
```
http://kitaika39.ru:8000/api/createorder/
```
Создает заказ и возвращает его айди
```
Необходимые параметры:
last_time: время, на которое сделан заказ
phone_number: номер телефона
name: имя
info: дополнительная информация к заказу
address: адрес доставки
take_type: тип выдачи (delivery/pickup) (доставка/самовывоз)
payment_type: тип оплаты (cash/card/online) (наличка/карта/онлайн)
Возвращает:
order_id: айди заказа
```

## Passwords
### mail.ru
kitaika39@mail.ru

UYoATun9b3x}
### reg.ru
kitaika39@mail.ru

3!gCOD2i

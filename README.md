# Kitaika website bd + fastapi backend
## Methods
### GetCategories
```
http://kitaika39.ru:8000/api/getcategories
```
Получает категории для наполнения меню
```
name: название категории
image_path: ссылка на картинку
```
### GetProducts
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
### GetOrders (not working)
```
http://kitaika39.ru:8000/api/getorders
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
```

## Passwords
### mail.ru
kitaika39@mail.ru

UYoATun9b3x}
### reg.ru
kitaika39@mail.ru

3!gCOD2i

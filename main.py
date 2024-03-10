from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from datetime import datetime
from starlette.responses import JSONResponse

app = FastAPI()
engine = create_engine(
    'sqlite:///kitaika.db')
Session = sessionmaker(bind=engine)

origins = [
    "http://kitaika39.ru",
    "https://kitaika39.ru",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def parse_time(timestamp):
    return datetime.fromtimestamp(timestamp / 1000)


@app.get("/api")
async def root():
    return {
        "api_documentation": "https://github.com/Marsvest/kitaika_backend/blob/master/README.md"
    }


def get_categories_all(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories


@app.get("/api/getcategories")
async def get_categories_route(categories: list = Depends(get_categories_all)):
    return {
        "categories": [
            {
                "category_id": category.id,
                "name": category.category,
                "image_path": category.image_path
            }
            for category in categories]
    }


def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.category_id == category_id).all()
    return products


@app.get("/api/getproducts/{category_id}")
async def get_products_route(category_id: int, products: list = Depends(get_products_by_category)):
    return {
        "category_id": category_id,
        "products": [
            {
                "product_id": product.id,
                "label": product.label,
                "price": product.price,
                "about": product.about,
                "image_path": product.image_path,
                "calories": product.calories
            }
            for product in products]
    }


def get_orders_all(db: Session = Depends(get_db)):
    orders = db.query(models.Orders).all()
    return orders


def get_items_by_order(order_id: int, db: Session = Depends(get_db)):
    items = db.query(models.OrderItems).filter(models.OrderItems.order_id == order_id).all()
    return items


def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.id == product_id).all()
    return products[0]


@app.get("/api/getorders/")
async def get_orders_route(orders: list = Depends(get_orders_all), db: Session = Depends(get_db)):
    return {
        "orders_count": len(orders),
        "orders": [
            {
                "order_id": order.id,
                "ordered_time": parse_time(order.ordered_time),
                "last_time": parse_time(order.last_time),
                "phone_number": order.phone_number,
                "name": order.name,
                "info": order.info,
                "address": order.address,
                "take_type": order.take_type,
                "payment_type": order.payment_type,
                "status": order.status,
                "confirmend": order.confirmed,
                "total_price": order.total_price,
                "items": [
                    {
                        "id": item.id,
                        "product_id": item.product_id,
                        "count": item.count,
                        "price": item.price,
                        "product": get_product_by_id(item.product_id, db)
                    }
                    for item in get_items_by_order(order.id, db)]
            }
            for order in orders]
    }


@app.get("/api/getitems/{order_id}")
def get_items_route(order_id: int, items: list = Depends(get_items_by_order), db: Session = Depends(get_db)):
    return {
        "order_id": order_id,
        "items": [
            {
                "id": item.id,
                "product_id": item.product_id,
                "count": item.count,
                "price": item.price,
                "product": get_product_by_id(item.product_id, db)
            }
            for item in items]
    }


@app.put("/api/updateorder/{order_id}")
async def update_order_route(order_id: int, updated_order: models.OrderUpdate,
                             items: list = Depends(get_items_by_order)):
    ordered_time = str(int(datetime.now().timestamp() * 1000))

    with Session() as session:
        db_order = session.query(models.Orders).filter(models.Orders.id == order_id).first()

        if db_order is None:
            raise HTTPException(status_code=404, detail="Order not found")

        for field, value in updated_order.model_dump().items():
            setattr(db_order, field, value)

        setattr(db_order, "total_price", sum(i.price for i in items))
        setattr(db_order, "confirmed", 1)
        setattr(db_order, "ordered_time", ordered_time)

        session.commit()
        session.refresh(db_order)

    return {
        "message": "Order updated successfully",
        "order_id": db_order.id
    }


@app.post("/api/orderinit")
async def order_init_route(order: models.OrderInit):
    db_order = models.Orders(**order.model_dump(), ordered_time="0", last_time="0", status="in queue",
                             phone_number="0", name="0", address="0", take_type="delivery", payment_type="cash",
                             total_price=0, info="0", confirmed=False)

    with Session() as session:
        session.add(db_order)
        session.commit()
        session.refresh(db_order)

    response = JSONResponse({
        "message": "Order created successfully",
        "order_id": db_order.id
    })

    response.set_cookie("order_id", str(db_order.id))
    return response


@app.post("/api/addtocart")
async def add_to_cart_route(order: models.OrderItemsUpdate, db: Session = Depends(get_db)):
    single_price = get_product_by_id(order.product_id, db).price
    price = single_price * order.count
    db_orderitems = models.OrderItems(**order.model_dump(), price=price, single_price=single_price)

    with Session() as session:
        session.add(db_orderitems)
        session.commit()
        session.refresh(db_orderitems)

    return {
        "message": "Item added successfully",
        "item_id": db_orderitems.id
    }


@app.post("/api/createproduct")
async def add_product_route(product: models.ProductCreate):
    db_product = models.Product(**product.model_dump())

    with Session() as session:
        session.add(db_product)
        session.commit()
        session.refresh(db_product)

    return {
        "message": "Product created successfully",
        "item_id": db_product.id
    }

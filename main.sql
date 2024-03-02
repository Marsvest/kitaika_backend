Create Table Categories
(
    id         integer primary key autoincrement,
    category   text unique not null,
    image_path text unique not null
);

Create Table Products
(
    id          integer primary key autoincrement,
    label       text unique not null,
    price       integer     not null,
    category_id integer     not null,
    about       text        not null,
    image_path  text unique not null,
    calories    integer,
    foreign key (category_id) references Categories (id)
);

Create Table OrderItems
(
    id         integer primary key autoincrement,
    order_id   integer not null,
    product_id integer not null,
    count      integer not null,
    price      integer not null,
    foreign key (order_id) references Orders (id),
    foreign key (product_id) references Products (id)
);

Create Table Orders
(
    id           integer primary key autoincrement,
    ordered_time datetime not null,
    last_time    datetime not null,
    phone_number text     not null,
    name         text     not null,
    info         text     not null,
    address      text     not null,
    take_type    text check ( take_type in ('delivery', 'pickup') ),
    payment_type text check ( payment_type in ('cash', 'card', 'online') ),
    status       text check ( status in ('in queue', 'cooking', 'done') )
);

-- Create Table Promo
-- (
--     id         integer primary key autoincrement,
--     image_path text unique not null,
--     product_id integer     not null,
--     foreign key (product_id) references Products (id)
-- );

Select
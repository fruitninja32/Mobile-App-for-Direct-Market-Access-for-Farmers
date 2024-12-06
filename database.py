from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://root:bth63051zF4pptj6ytBjVofIewGkupaZ@dpg-csseg29u0jms73ea4kf0-a.oregon-postgres.render.com/dma_app?sslmode=require"
)


def remove_Product(pid):
    with engine.connect() as conn:
        result = conn.execute(text("DELETE FROM products WHERE pid = :pid"),
                              {"pid": pid})
        conn.commit()
def remove_orders(pid):
    with engine.connect() as conn:
        result = conn.execute(text("DELETE FROM products WHERE pid = :pid"),
                              {"pid": pid})
        conn.commit()


def accept_order(oid):
    with engine.connect() as conn:
        conn.execute(
            text(
                "UPDATE orders SET status = 'Accepted', updates = 'Accepted' WHERE oid = :oid"
            ), {"oid": oid})
        conn.commit()


def update(oid, update_order):
    with engine.connect() as conn:
        conn.execute(
            text("UPDATE orders SET updates=:update_order WHERE oid=:oid"), {
                "oid": oid,
                "update_order": update_order
            })
        conn.commit()


def cancel_order(oid):
    with engine.connect() as conn:
        conn.execute(text("UPDATE orders SET status='Cancel' WHERE oid=:oid"),
                     {"oid": oid})
        conn.commit()


def delivered_order(oid, rating):
    with engine.connect() as conn:
        conn.execute(
            text(
                "UPDATE orders SET status='Delivered', updates='Delivered', rating=:rating WHERE oid=:oid"
            ), {
                "oid": oid,
                "rating": rating
            })
        conn.commit()


def add_user_to_db(data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO products(fname, fid, pname, quantity, price, dt,url) "
            "VALUES(:fname, :fid, :pname, :quantity, :price, :dt,:url)")
        conn.execute(
            query,
            {
                "fname": username,
                "fid": uid,
                "pname": data["pname"],
                "quantity": data["quantity"],
                "price": data["price"],
                "dt": data["date"],
                "url": data['url']
            },
        )
        conn.commit()


def add_product_to_db(data, username, uid):

    with engine.connect() as conn:
        query = text(
            "INSERT INTO products(fname, fid, pname, quantity, price, dt,url) "
            "VALUES(:fname, :fid, :pname, :quantity, :price, :dt,:url)")
        conn.execute(
            query,
            {
                "fname": username,
                "fid": uid,
                "pname": data["pname"],
                "quantity": data["quantity"],
                "price": data["price"],
                "dt": data["date"],
                "url": data['url']
            },
        )
        conn.commit()


def add_orders_to_db(fid, pid, bid, quantity, total_price):
    with engine.begin() as conn:  # Transactional connection
        query = text(
            "INSERT INTO Orders(fid, pid, bid, quantity, price, status) "
            "VALUES(:fid, :pid, :bid, :quantity, :price, 'Ordered')")
        conn.execute(
            query, {
                "fid": fid,
                "pid": pid,
                "bid": bid,
                "quantity": quantity,
                "price": total_price,
            })

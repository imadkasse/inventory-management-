from database.models import Product 
from sqlalchemy import select
from database.connection import session



def add_product(name, price , quantity , category_id):
    try:
        new_product = Product(name=name, price=price , quantity=quantity ,category_id=category_id)
        session.add(new_product)
        session.commit()
        return 'product Added Successfully'
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'
    

def update_product(id,new_name=None , new_price=None , new_quantity=None):
    try:
        stmt =select(Product).where(Product.id ==id)
        
        product = session.scalars(stmt).one()
        if not product:
            return 'product not found'
        if new_name and new_price and new_quantity:
            product.name = new_name
            product.price = new_price
        elif new_name :
            product.name = new_name
        elif new_price:
            product.price=new_price
        else:
            product.quantity=new_quantity
        session.commit()    
        return f'product With Id:{id} Updated Successfully'
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'
    

def delete_product(id):
    try:
        product = session.get(Product,id)

        session.delete(product)
        session.commit()
        return 'product Deleted Successfully'
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'

def find_one_product(id):
    try:
        product = session.get(Product , id)
        return product
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'  


def find_many_product():
    try:
        stmt = select(Product)
        products = session.scalars(stmt).all()
        return products
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'    


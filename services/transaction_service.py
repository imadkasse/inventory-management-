from database.models import Transaction  , Product
from sqlalchemy import select
from database.connection import session
from .product_service import update_product , find_one_product
# - type: String (Not Null) - Type of movement (e.g., "IN" or "OUT")
def add_transaction(product_id, type , quantity ,notes ):
    try:
        new_transaction = Transaction(product_id=product_id, type=type , quantity=quantity ,notes=notes)
        # change the product quantity after do an transactio 
        # get the Product info 
        product = find_one_product(product_id)
        if type == 'IN' :
            new_quantity= quantity+ product.quantity
            update_product(id=product_id , new_quantity=new_quantity)
        else:
            # check if the transaction quantity less or equal than product quantity
            if product.quantity >= quantity:
                new_quantity= product.quantity - quantity
                update_product(id=product_id , new_quantity=new_quantity)
            else:
                raise ValueError('The quantity should be equal or less than product quantity')   
                
        session.add(new_transaction)
        session.commit()
        return 'transaction Added Successfully'
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'
    
def find_one_transaction(id):
    try:
        transaction = session.get(Transaction , id)
        return transaction
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'  


def find_many_transaction():
    try:
        stmt = select(Transaction)
        transactions = session.scalars(stmt).all()
        return transactions
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'    


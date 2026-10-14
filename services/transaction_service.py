from database.models import Transaction 
from sqlalchemy import select
from database.connection import session
# - type: String (Not Null) - Type of movement (e.g., "IN" or "OUT")
def add_transaction(product_id, type , quantity ,notes ):
    try:
        new_transaction = Transaction(product_id=product_id, type=type , quantity=quantity ,notes=notes)
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
        print('from func transaction : ', transactions)
        return transactions
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'    


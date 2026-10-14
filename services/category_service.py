"""
this file contains all proccess with table `categories`
"""

from database.models import Category 
from sqlalchemy import select
from database.connection import session


def add_category(name, description):
    try:
        new_category = Category(name=name, description=description)
        session.add(new_category)
        session.commit()
        return 'Category Added Successfully'
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'
    

def update_category(id,new_name=None , new_description=None):
    try:
        stmt =select(Category).where(Category.id ==id)
        
        category = session.scalars(stmt).one()
        if not category:
            return 'Category not found'
        if new_name and new_description:
            category.name = new_name
            category.description = new_description
        elif new_name :
            category.name = new_name
        # elif new_description
        else:
            category.description=new_description
        session.commit()    
        return f'Category With Id:{id} Updated Successfully'
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'
    

def delete_category(id):
    try:
        category = session.get(Category,id)

        session.delete(category)
        session.commit()
        return 'Category Deleted Successfully'
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'

def find_one_category(id):
    try:
        category = session.get(Category , id)
        return category
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'  


def find_many_category():
    try:
        stmt = select(Category)
        categories = session.scalars(stmt).all()
        return categories
    except Exception as e:
        session.rollback() 
        return f'Oops an error: {e}'    


from sqlalchemy import create_engine  ,select
from sqlalchemy.orm import Session
from models import Base , Category


engine = create_engine(r"sqlite:///D:\project\inventory_app\db.db", echo=True )

Base.metadata.create_all(engine)

session = Session(engine)


# with session:

#      newCategory = Category(name = 'Macbook air 3' , description='this pc is very powerfull' )
     

#      session.add_all([newCategory])

#      session.commit()

# stmt = select(Category)

# for category in session.scalars(stmt):
#     print(f'category {category}')
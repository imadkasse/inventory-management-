"""
that file for define the schema of this app 
the models : 
--- 1. Category Model ---



--- 2. Product Model ---



--- 3. Transaction Model ---


"""
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase ,Mapped , mapped_column , relationship 
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Category(Base):
    """
    Table name: "categories"
    Required Columns:
    - id: Integer (Primary Key, Index)
    - name: String (Unique, Not Null) - Category name
    - description: String (Nullable) - Optional description of the category
    Relationship:
    - products: Linked to the Product model using relationship() with back_populates="category"
    """
    __tablename__ = "categories"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(unique=True)
    description:Mapped[str] = mapped_column(nullable=True)
    products: Mapped[list["Product"]] = relationship(back_populates="category")
    
    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name='{self.name}' , description='{self.description}')>"


class Product(Base):
    """
    Table name: "products"
    Required Columns:
    - id: Integer (Primary Key, Index)
    - name: String (Not Null) - Product name
    - price: Float (Not Null) - Unit price
    - quantity: Integer (Default = 0) - Current stock quantity
    - reorder_level: Integer (Default = 5) - Threshold for low stock warning
    - category_id: Integer (Foreign Key referencing "categories.id")
    Relationships:
    - category: Linked to the Category model (back_populates="products")
    - transactions: Linked to the Transaction model (back_populates="product")
    """
    
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True , autoincrement=True)
    name:Mapped[str] = mapped_column(nullable=False)
    price:Mapped[float] = mapped_column(nullable=False)
    quantity:Mapped[int]= mapped_column(default=0)
    category_id:Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category:Mapped["Category"] = relationship(back_populates='products')
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="product", cascade="all, delete-orphan")
    def __repr__(self) -> str:
        return f"<Product(id={self.id}, name='{self.name}' , price='{self.price} , quantity={self.quantity} ')>"
    
class Transaction(Base):
    """
    Table name: "transactions"
    Required Columns:
    - id: Integer (Primary Key, Index)
    - product_id: Integer (Foreign Key referencing "products.id")
    - type: String (Not Null) - Type of movement (e.g., "IN" or "OUT")
    - quantity: Integer (Not Null) - Quantity added or removed
    - timestamp: DateTime (Default = datetime.utcnow) - Time of the transaction
    - notes: String (Nullable) - Additional notes or reason
    Relationship:
    - product: Linked to the Product model (back_populates="transactions")
    """
    __tablename__ = "Transactions"
    id:Mapped[int]= mapped_column(primary_key=True)
    product_id:Mapped[int] = mapped_column(ForeignKey("products.id"))
    type:Mapped[str] = mapped_column(nullable=False)
    quantity:Mapped[int] = mapped_column(nullable=False)
    notes:Mapped[str] = mapped_column(nullable=True)
    timestamp:Mapped[datetime] = mapped_column(default=datetime.now())
    product: Mapped["Product"] = relationship(back_populates="transactions")
    
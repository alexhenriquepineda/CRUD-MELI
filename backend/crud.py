from sqlalchemy.orm import Session
from models import ProductModel
from schema import ProductCreate, ProductUpdate

def get_products(db: Session):
    """
    Retrieve all products from the database.
    Args:
        db (Session): The database session used to query the products.
    Returns:
        List[ProductModel]: A list of all products in the database.
    """
    return db.query(ProductModel).all()


def get_product(db: Session, product_id: int):
    """
    Retrieve a product from the database by its ID.
    Args:
        db (Session): The database session to use for the query.
        product_id (int): The ID of the product to retrieve.
    Returns:
        ProductModel: The product with the specified ID, or None if no such product exists.
    """

    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def create_product(db: Session, product: ProductCreate):
    """
    Create a new product in the database.
    Args:
        db (Session): The database session used to add the product.
        product (ProductCreate): The product data to be added to the database.
    Returns:
        ProductModel: The product that was added to the database.
    """
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    """
    Delete a product from the database.
    Args:
        db (Session): The database session used to delete the product.
        product_id (int): The ID of the product to be deleted.
    Returns:
        ProductModel: The product that was deleted from the database.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Update an existing product in the database.
    Args:
        db (Session): The database session to use for the update.
        product_id (int): The ID of the product to update.
        product (ProductUpdate): An object containing the updated product information.
    Returns:
        ProductModel: The updated product object if the product was found and updated, 
                      None if the product with the given ID does not exist.
    """


    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description
    
    if product.price is not None:
        db_product.price = product.price

    if product.category is not None:
        db_product.category = product.category

    if product.email_supplier is not None:
        db_product.email_supplier = product.email_supplier

    db.commit()
    db.refresh(db_product)

    return db_product


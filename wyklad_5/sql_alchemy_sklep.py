from sqlalchemy import (
    Table,
    Column,
    Integer,
    Numeric,
    String,
    DateTime,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import (
    relationship,
)

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import as_declarative, declarative_base

# set echo to False
engine = create_engine('sqlite:///sql_alchemy_sklep.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# to będzie nasza baza - po niej będziemy dziedziczyć
#http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/api.html#sqlalchemy.ext.declarative.as_declarative
@as_declarative()
class Base():
    pass
    
#Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    surname = Column(String(), nullable=False)
    msisdn = Column(String(), nullable=True)
    email = Column(String(), nullable=False)
    
    # password = Column(Integer(), ForeignKey('simple_passwords.password_id'))


class Adress(Base):
    __tablename__ = 'adresses'
    
    id = Column(Integer(), primary_key=True)
    country = Column(String(), nullable=False)
    city = Column(String(), nullable=False)
    street = Column(String(), nullable=False)
    house_number = Column(Integer(), nullable=False)
    flat_number = Column(Integer(), nullable=True)
    # TODO: to później dodać
    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
        index=True,
    )
    # TODO: to później dodać
    user = relationship(
        'User',
        #foreign_keys=user_id,
        backref='adresses',
    )
    
    
order_item_association_table = Table(
    'order_item_association',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('item_id', Integer, ForeignKey('items.id'))
)
    
    
class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer(), primary_key=True)
    adress_id = Column(
        Integer,
        ForeignKey('adresses.id'),
        nullable=False,
        index=True,
    )
    adress = relationship(
        'Adress',
        #foreign_keys=user_id,
        backref='orders',
    )
    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False,
        index=True,
    )
    user = relationship(
        'User',
        #foreign_keys=user_id,
        backref='orders',
    )
    # TODO: dodać relację z przedmiotami many-to-many
    items = relationship(
        "Item",
        secondary=order_item_association_table
    )    
    
    
class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    price = Column(Integer(), nullable=False)


# TODO: to nie działa, przy restarcie aplikacji baza dodaje się na nowo
# trzeba to sfixować w pracy domowej
DB_CREATED = False
def create_db():
    if not DB_CREATED:
        Base.metadata.create_all(engine)
        global DB_CREATED
        DB_CREATED = True




########################dodawanie wpisów do bazy################################
#session.add(proste_haslo)
#session.commit()




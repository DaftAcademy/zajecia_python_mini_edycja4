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

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import as_declarative, declarative_base

engine = create_engine('sqlite:///sql_alchemy_second_db.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# to będzie nasza baza - po niej będziemy dziedziczyć
#http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/api.html#sqlalchemy.ext.declarative.as_declarative
@as_declarative()
class Base():
    pass
    
#Base = declarative_base()
class User(Base):
    __tablename__ = 'simple_users'
    
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)
    password = Column(Integer(), ForeignKey('simple_passwords.password_id'))

    
class Password(Base):
    __tablename__ = 'simple_passwords'
    
    password_id = Column(Integer(), primary_key=True)
    # tu będziemy trzymać "hasła" w czystym tekście - nie róbcie tak, to złe
    swordfish = Column(String, nullable=False)
    
    
    
Base.metadata.create_all(engine)

proste_haslo = Password(swordfish='dupa1234')
session.add(proste_haslo)
session.commit()
zenek = User(username='Zenek', password=proste_haslo.password_id)
session.add(zenek)
session.commit()


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

engine = create_engine('sqlite:///sql_alchemy_first_db.db')
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
    
    username = Column(String(), primary_key=True)
    
    
Base.metadata.create_all(engine)


zenek = User(username='Zenek')
muniek = User(username='Zygmunt')
hermenegilda = User(username='Hera')
session.add(zenek)
session.commit()
session.add(hermenegilda)
session.add(muniek)
session.commit()



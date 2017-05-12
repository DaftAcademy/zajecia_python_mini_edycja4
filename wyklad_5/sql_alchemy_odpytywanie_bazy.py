from sqlalchemy import or_
from sql_alchemy_sklep import (
    User,
    Adress,
    Order,
    Item,
    session,
    
)

# filtrowanie
# Having?
# sortowanie
# and, or
# 
# joinowanie



def query_db():
    print('{:*^80}'.format('simple_query'))
    simple_query()
    
    print('{:*^80}'.format('query_all'))
    query_all()
    
    print('{:*^80}'.format('query_for'))
    query_for()
    
    print('{:*^80}'.format('query_for_users'))
    query_for_users()
    
    print('{:*^80}'.format('query_for_order'))
    query_for_order()
    
    print('{:*^80}'.format('query_for_filter'))
    query_for_filter()
    
    print('{:*^80}'.format('query_for_filter_or'))
    query_for_filter_or()
    

def simple_query():
    # http://docs.sqlalchemy.org/en/latest/orm/query.html#query-api
    items = session.query(Item)
    print('type(items) = {}'.format(type(items)))
    print('items = {}'.format(items))
    
def query_all():
    items = session.query(Item).all()
    print('type(items) = {}'.format(type(items)))
    print('items = {}'.format(items))
    
    
def query_for():
    items = session.query(Item)
    for item in items:
        print('{:-^80}'.format('new_item'))
        print('type(item) = {}'.format(type(item)))
        print('item = {}'.format(item))
        print('item.id = {}'.format(item.id))
        print('item.name = {}'.format(item.name))
        print('item.description = {}'.format(item.description))
        print('item.price = {}'.format(item.price))
        
        
def query_for_users():
    users = session.query(User)
    for user in users:
        print('{:-^80}'.format('next user'))
        print('type(user) = {}'.format(type(user)))
        print('user = {}'.format(user))
        print('user.id = {}'.format(user.id))
        print('user.name = {}'.format(user.name))
        print('user.surname = {}'.format(user.surname))
        # To nam dokłada kloejne query - ma to wady i zalety
        print('user.orders = {}'.format(user.orders))   
        

def query_for_order():
    # może być też desc
    items = session.query(Item).order_by(Item.name.asc())
    for item in items:
        print('{:-^80}'.format('new_item'))
        print('type(item) = {}'.format(type(item)))
        print('item = {}'.format(item))
        print('item.id = {}'.format(item.id))
        print('item.name = {}'.format(item.name))
        print('item.description = {}'.format(item.description))
        print('item.price = {}'.format(item.price))
        
        
def query_for_filter():
    items = session.query(Item).filter(Item.name == 'wilk')
    for item in items:
        print('{:-^80}'.format('new_item'))
        print('type(item) = {}'.format(type(item)))
        print('item = {}'.format(item))
        print('item.id = {}'.format(item.id))
        print('item.name = {}'.format(item.name))
        print('item.description = {}'.format(item.description))
        print('item.price = {}'.format(item.price))
        
        
def query_for_filter_or():
    print('dupa')
    #items = session.query(Item).filter(or_(Item.name == 'wilk', Item.name == 'lampart'))
    items = session.query(Item).filter(or_(Item.name == 'lampart', Item.name == 'wilk'))
    for item in items:
        print('{:-^80}'.format('new_item'))
        print('type(item) = {}'.format(type(item)))
        print('item = {}'.format(item))
        print('item.id = {}'.format(item.id))
        print('item.name = {}'.format(item.name))
        print('item.description = {}'.format(item.description))
        print('item.price = {}'.format(item.price))


if __name__ == '__main__':
    query_db()

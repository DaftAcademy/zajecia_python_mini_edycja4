from sql_alchemy_sklep import (
    User,
    Adress,
    Order,
    Item,
    session,
    create_db,
)


def add_data_to_db():
    create_db()
    
    # bieda transakcja
    try:
        # przedmioty
        bear = Item(
            name = 'niedźwiedź',
            description = 'Choćby niedźwiedź... to dostoję!',
            price = 100,
        )
        # http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#adding-new-or-existing-items
        session.add(bear)
        
        wolf = Item(
            name = 'wilk',
            description = 'Wilki?... Ja ich całą zgraję\nPozabijam i pokraję!',
            price = 200,
        )
        session.add(wolf)
        
        lampart = Item(
            name = 'lampart',
            description = 'Te hieny, te lamparty\nTo są dla mnie czyste żarty!',
            price = 500,
        )    
        session.add(lampart)
        
        # klienci
        stefek = User(
            name = 'Stefan',
            surname = 'Burczymucha',
            msisdn = '123456789',
            email = 'stefek.burczumucha@maria.konopnicka.com',
        )
        session.add(stefek)
        
        bambo = User(
            name = 'Murzynek',
            surname = 'Bambo',
            msisdn = '741852963',
            email = 'murzynek.bambo@julian.tuwim.com',
        )
        session.add(bambo)
        
        # adresy
        adres_ptasia = Adress(
            country = 'Polska',
            city = 'Warszawa',
            street = 'Ptasia',
            house_number = 2,
            flat_number = 222,
            user = stefek,
        )
        session.add(adres_ptasia)
        
        adres_kacza = Adress(
            country = 'Polska',
            city = 'Warszawa',
            street = 'Kacza',
            house_number = 5,
            flat_number = 555,
            user = stefek,
        )
        session.add(adres_kacza)
        
        adres_bambo = Adress(
            country = 'polska',
            city = 'Warszawa',
            street = 'Esperanto',
            house_number = 5,
            flat_number = None,
            user = bambo,
        )
        session.add(adres_bambo)
        session.commit()
        
    except:
        # w razie jakiegokolwiek problemu robimy rollback.
        # nic z transakcji nie trafi do bazy
        session.rollback()
        raise
    
    # znów bieda transakcja
    try:
        # dodanie zamówień
        zamówiene_na_wilka = Order(
            adress = adres_ptasia,
            user = adres_ptasia.user,
            items = [wolf],
        )
        session.add(zamówiene_na_wilka)
        
        zamówiene_na_wilka_i_lamparta = Order(
            adress = adres_kacza,
            user = adres_kacza.user,
            items = [wolf, lampart]
        )
        session.add(zamówiene_na_wilka_i_lamparta)
        
        zamówiene_na_dwa_misie = Order(
            adress = adres_bambo,
            user = adres_bambo.user,
            # to jest bardzo słabe przy dużych zamówieniach, mamy źle
            # zaprojektowaną bazę danych !!!
            # TODO: rozwiązać problem, praca domowa
            items = [bear, bear]
        )
        session.add(zamówiene_na_dwa_misie)
         
        session.commit()
    except:
        session.rollback()
        raise


if __name__ == '__main__':
    add_data_to_db()

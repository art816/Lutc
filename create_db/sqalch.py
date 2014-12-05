__author__ = 'art'


# import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

def using():




    engine = create_engine('sqlite:///test1.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()

    user_tables = Table('users', metadata, Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String),
        Column('password', String)
    )
    metadata.create_all(engine)
    mapper(User, user_tables)
    # print(mapper(User, user_tables))  # и отобразить. Передает класс User и нашу таблицу
    # user = User("Вася", "Василий", "qweasdzxc")
    for user in session.query(User):
        print(user)  #Напечатает <User('Вася', 'Василий', 'qweasdzxc'>
    # print(user.id)
    # session.add(user)
    # session.commit()
    # session.close()


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

if __name__ == '__main__':
    using()
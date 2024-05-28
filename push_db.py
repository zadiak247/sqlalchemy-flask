# Импорт необходимых модулей и функций для работы БД
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Настройка базы данных
engine = create_engine('sqlite:///blob.db')
Base = declarative_base()

class Post(Base):
  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  content = Column(Text)

# Создание базы данных и таблиц
Base.metadata.create_all(engine)

# Сессия базы данных
Session = sessionmaker(bind=engine)
session = Session()


for i in range(1, 6):
    my_first_post = Post(title = f'Привет Мир {i}!', content = 'Содержимое записи привет мир!')
    session.add(my_first_post)
    session.commit()
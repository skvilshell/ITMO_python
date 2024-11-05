import pandas as pd

from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
 
# Получение данных для подключения к базе
db_user = input("Введите имя пользователя базы данных: ")
db_host = input("Введите адрес хоста базы данных: ")
db_password = input("Введите пароль для подключения к базе данных: ")
db_name = input("Введите имя базы данных: ")
 
# Формирование строки подключения к PostgreSQL
connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
 
try:
    # Получение и загрузка файла
    file_path = input("Введите имя CSV файла: ")
    table_name = file_path.split('.')[0]  # Имя таблицы по названию файла
 
    # Загрузка данных из CSV в DataFrame
    df = pd.read_csv(file_path, dtype=str)  # Указываем, что все типы данных строковые
 
    # Создание таблицы с нужными столбцами
    columns = [Column(col_name, String) for col_name in df.columns]
    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)
 
    # Загрузка данных из CSV в таблицу кусками
    chunksize = 1000000 # Размер куска
    for chunk in pd.read_csv(file_path, chunksize=chunksize, dtype=str, iterator=True):
        chunk.to_sql(table_name, engine, index=False, if_exists='append')
    print(f"Таблица '{table_name}' успешно создана и данные загружены.")
 
    # Функции работы с таблицей
    def show_columns():
        """Выводит заголовки всех столбцов таблицы."""
        print(f"Столбцы таблицы '{table_name}':")
        print(", ".join(df.columns))
 
    def add_row():
        """Добавляет новую строку в таблицу. Пользователь вводит данные через пробел."""
        row_data = input("Введите значения для новой строки через пробел: ")
        row_values = row_data.split(" ")
        if len(row_values) != len(df.columns):
            print("Ошибка: количество значений не совпадает с количеством столбцов.")
            return
        new_row = {col: val for col, val in zip(df.columns, row_values)}
        session.execute(table.insert().values(new_row))
        session.commit()
        print("Строка успешно добавлена.")
 
    def show_rows():
#        """Выводит строки с указанной по указанную."""
        start = int(input("Введите номер начальной строки: "))
        end = int(input("Введите номер конечной строки: "))
        result = session.query(table).slice(start - 1, end).all()
        for row in result:
            print(row)
 
    def show_rows_in_column():
#        """Выводит строки указанного столбца с указанной по указанную."""
        column_name = input("Введите имя столбца: ")
        if column_name not in df.columns:
            print(f"Ошибка: столбец '{column_name}' не существует.")
            return
        start = int(input("Введите номер начальной строки: "))
        end = int(input("Введите номер конечной строки: "))
        result = session.query(getattr(table.c, column_name)).slice(start - 1, end).all()
        for row in result:
            print(row)
 
    def show_column():
#        """Выводит весь столбец по имени."""
        column_name = input("Введите имя столбца: ")
        if column_name not in df.columns:
            print(f"Ошибка: столбец '{column_name}' не существует.")
            return
        result = session.query(getattr(table.c, column_name)).all()
        for row in result:
            print(row)
 
    def user_interface():
#        """Основной интерфейс для пользователя."""
        print("\nВыберите команду для выполнения:")
        print("1. Вывести заголовки всех столбцов таблицы")
        print("2. Добавить строку в таблицу")
        print("3. Вывести строки с указанной по указанную")
        print("4. Вывести строки с указанной по указанную в указанном столбце")
        print("5. Вывести весь столбец по имени")
        print("6. Завершить работу")
 
        while True:
            command = input("\nВведите номер команды: ")
            if command == '1':
                show_columns()
            elif command == '2':
                add_row()
            elif command == '3':
                show_rows()
            elif command == '4':
                show_rows_in_column()
            elif command == '5':
                show_column()
            elif command == '6':
                print("Выход из программы.")
                break
            else:
                print("Неверная команда. Попробуйте снова.")
 
    # Запуск интерфейса
    user_interface()
 
except SQLAlchemyError as e:
    print(f"Ошибка при работе с базой данных: {e}")
finally:
    session.close()
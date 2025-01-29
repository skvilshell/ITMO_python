import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import inspect
import os

# Функции для работы с таблицей
def show_columns(table):
    """Выводит заголовки всех столбцов таблицы."""
    print(f"Столбцы таблицы '{table.name}':")
    print(", ".join([col.name for col in table.columns]))

def add_row(table, session):
    """Добавляет новую строку в таблицу. Пользователь вводит данные через пробел."""
    row_data = input("Введите значения для новой строки через пробел: ")
    row_values = row_data.split(" ")
    if len(row_values) != len(table.columns) - 1:  # Учитываем id
        print("Ошибка: количество значений не совпадает с количеством столбцов.")
        return
    new_row = {col.name: val for col, val in zip(table.columns[1:], row_values)}
    session.execute(table.insert().values(new_row))
    session.commit()
    print("Строка успешно добавлена.")

def show_rows(table, session):
    """Выводит строки таблицы по значениям id."""
    if 'id' not in table.c:
        print("Ошибка: Столбец 'id' не найден в таблице.")
        return

    start_id = int(input("Введите начальный id строки: "))
    end_id = int(input("Введите конечный id строки: "))
    result = session.execute(table.select().where(table.c.id.between(start_id, end_id))).fetchall()
    for row in result:
        print(row)

def show_rows_in_column(table, session):
    """Выводит строки в указанном столбце, используя диапазон значений id."""
    column_name = input("Введите имя столбца: ")
    if column_name not in [col.name for col in table.columns]:
        print(f"Ошибка: столбец '{column_name}' не существует.")
        return
    if 'id' not in table.c:
        print("Ошибка: Столбец 'id' не найден в таблице.")
        return

    start_id = int(input("Введите начальный id строки: "))
    end_id = int(input("Введите конечный id строки: "))
    result = session.execute(
        table.select().with_only_columns(getattr(table.c, column_name)).where(table.c.id.between(start_id, end_id))
    ).fetchall()
    for row in result:
        print(row)

def show_column(table, session):
    """Выводит все значения указанного столбца."""
    column_name = input("Введите имя столбца: ")
    if column_name not in [col.name for col in table.columns]:
        print(f"Ошибка: столбец '{column_name}' не существует.")
        return
    result = session.execute(table.select().with_only_columns(getattr(table.c, column_name))).fetchall()
    for row in result:
        print(row)

def delete_rows(table, session):
    """Удаляет строки в таблице от указанной до указанной по уникальному id."""
    if 'id' not in table.c:
        print("Ошибка: Столбец 'id' не найден в таблице.")
        return

    start_id = int(input("Введите начальный id строки для удаления: "))
    end_id = int(input("Введите конечный id строки для удаления: "))
    try:
        stmt = table.delete().where(table.c.id.between(start_id, end_id))
        session.execute(stmt)
        session.commit()
        print(f"Строки с id от {start_id} до {end_id} успешно удалены.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Ошибка при удалении строк: {e}")

def delete_table(engine, metadata):
    """Удаляет таблицу по имени, введенному пользователем."""
    table_to_delete = input("Введите имя таблицы для удаления: ")
    try:
        if inspect(engine).has_table(table_to_delete):
            table_obj = Table(table_to_delete, metadata, autoload_with=engine)
            table_obj.drop(engine)
            print(f"Таблица '{table_to_delete}' успешно удалена.")
        else:
            print(f"Таблица '{table_to_delete}' не существует.")
    except SQLAlchemyError as e:
        print(f"Ошибка при удалении таблицы: {e}")

def select_operation(session, table, engine, metadata):
    while True:
        print("""
        Выберите операцию:
        1. Показать заголовки всех столбцов таблицы
        2. Добавить строку в таблицу
        3. Показать строки с указанной по указанную по id
        4. Показать строки с указанной по указанную в указанном столбце
        5. Показать все значения указанного столбца
        6. Удалить строки с указанной по указанную по id
        7. Удалить таблицу по имени
        8. Выйти
        """)
        operation = input("Введите номер операции: ")
        if operation == "1":
            show_columns(table)
        elif operation == "2":
            add_row(table, session)
        elif operation == "3":
            show_rows(table, session)
        elif operation == "4":
            show_rows_in_column(table, session)
        elif operation == "5":
            show_column(table, session)
        elif operation == "6":
            delete_rows(table, session)
        elif operation == "7":
            delete_table(engine, metadata)
        elif operation == "8":
            break
        else:
            print("Неизвестная команда. Пожалуйста, попробуйте еще раз.")

def main():
    db_user = "user"
    db_host = "localhost"
    db_password = "password"
    db_name = "itmo_data"

    connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}"
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()

    try:
        print("""
        Выберите действие:
        1. Создать таблицу из CSV файла
        2. Подключиться к существующей таблице
        """)
        choice = input("Введите номер действия: ")

        if choice == "1":
            file_path = input("Введите имя CSV файла: ")
            if not os.path.isfile(file_path):
                print("Файл не найден. Проверьте правильность имени и путь к файлу.")
                return

            table_name = os.path.splitext(os.path.basename(file_path))[0]
            df = pd.read_csv(file_path, nrows=0)

            if inspect(engine).has_table(table_name):
                print(f"Таблица с именем '{table_name}' уже существует.")
                overwrite_choice = input("Вы хотите перезаписать существующую таблицу? (да/нет): ")
                if overwrite_choice.lower() == 'да':
                    Table(table_name, metadata, autoload_with=engine).drop(engine)
                    print(f"Таблица '{table_name}' была удалена.")
                else:
                    print("Процесс создания новой таблицы отменён.")
                    return

            columns = [Column('id', Integer, primary_key=True, autoincrement=True)]
            columns += [Column(col_name, String) for col_name in df.columns]

            table = Table(table_name, metadata, *columns, extend_existing=True)
            metadata.create_all(engine)

            chunksize = 1000000
            for chunk in pd.read_csv(file_path, chunksize=chunksize, dtype=str):
                chunk.to_sql(table_name, engine, index=False, if_exists='append')
            print(f"Таблица '{table_name}' успешно создана и данные загружены.")

        elif choice == "2":
            table_name = input("Введите имя существующей таблицы: ")
            if not inspect(engine).has_table(table_name):
                print(f"Таблица с именем '{table_name}' не найдена.")
                return

            table = Table(table_name, metadata, autoload_with=engine)
            print(f"Подключено к таблице '{table_name}'.")

        else:
            print("Неверный выбор. Завершение работы программы.")
            return

        select_operation(session, table, engine, metadata)

    except SQLAlchemyError as e:
        print(f"Ошибка при работе с базой данных: {e}")
    except Exception as ex:
        print(f"Возникла ошибка: {ex}")
    finally:
        session.close()

if __name__ == "__main__":
    main()

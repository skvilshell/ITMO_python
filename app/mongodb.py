import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import pandas as pd

CHUNK_SIZE = 1000000  # Размер части

async def get_user_input(prompt):
    return input(prompt)

async def connect_to_database():
    user = "admin"
    host = "localhost"
    password = "my_password"
    db_name = await get_user_input("Введите имя базы данных: ")
    uri = f"mongodb://{user}:{password}@{host}:27017"

    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    return db

async def load_csv_in_chunks(collection, file_path):
    """
    Загружает CSV-файл частями в MongoDB.
    """
    for chunk in pd.read_csv(file_path, chunksize=CHUNK_SIZE):
        # Преобразование DataFrame в список словарей для вставки
        records = chunk.to_dict('records')

        # Асинхронная вставка данных в коллекцию
        if records:
            await collection.insert_many(records)
        print(f"Загружена часть из {len(records)} строк.")

async def show_columns(collection):
    sample_document = await collection.find_one()
    if sample_document:
        print("Заголовки столбцов:", list(sample_document.keys()))
    else:
        print("Таблица пуста.")

async def main():
    db = await connect_to_database()

    choice = await get_user_input("Введите 1 для работы с существующей таблицей, 2 для загрузки из CSV: ")

    if choice == '1':
        table_name = await get_user_input("Введите имя таблицы: ")
        collection = db[table_name]
    elif choice == '2':
        file_path = await get_user_input("Введите путь к файлу CSV: ")
        table_name = file_path.split('/')[-1].split('.')[0]
        collection = db[table_name]

        # Загрузка CSV в MongoDB частями
        await load_csv_in_chunks(collection, file_path)

    # Теперь взаимодействуем с таблицей
    while True:
        action = await get_user_input(
            "\nВыберите действие:\n"
            "1: Вывести заголовки столбцов\n"
            "2: Добавить строки\n"
            "3: Вывести строки с/по номеру\n"
            "4: Вывести строки с/по номеру в столбце\n"
            "5: Вывести столбец по имени\n"
            "6: Удалить таблицу\n"
            "7: Удалить строки с/по номеру\n"
            "8: Выйти\n"
        )

        if action == '1':
            await show_columns(collection)

        elif action == '2':
            row_input = await get_user_input("Введите строку для добавления (значения через пробел): ")
            values = row_input.split()
            doc = {str(i): val for i, val in enumerate(values)}
            await collection.insert_one(doc)

        elif action == '3':
            start = int(await get_user_input("Введите начальный номер строки: "))
            end = int(await get_user_input("Введите конечный номер строки: "))
            cursor = collection.find().skip(start-1).limit(end-start+1)
            async for document in cursor:
                print(document)

        elif action == '4':
            start = int(await get_user_input("Введите начальный номер строки: "))
            end = int(await get_user_input("Введите конечный номер строки: "))
            column = await get_user_input("Введите имя столбца для вывода: ")
            cursor = collection.find().skip(start-1).limit(end-start+1)
            async for document in cursor:
                print(document.get(column, "Не найдено"))

        elif action == '5':
            column = await get_user_input("Введите имя столбца: ")
            cursor = collection.find({}, {column: 1})
            async for document in cursor:
                print(document.get(column, "Не найдено"))

        elif action == '6':
            await db.drop_collection(table_name)
            print(f"Таблица '{table_name}' была удалена.")
            break

        elif action == '7':
            start = int(await get_user_input("Введите начальный номер строки для удаления: "))
            end = int(await get_user_input("Введите конечный номер строки для удаления: "))
            cursor = collection.find().skip(start-1).limit(end-start+1)
            delete_ids = [document['_id'] for document in await cursor.to_list(length=end-start+1)]
            await collection.delete_many({'_id': {'$in': delete_ids}})
            print(f"Строки с {start} по {end} были удалены.")

        elif action == '8':
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == '__main__':
    asyncio.run(main())

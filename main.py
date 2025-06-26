from infrastructure.db.postgres import PostgresDB
from core.settings import settings
from core.model import Category, Locations, Object


def initialize_database():
    # Инициализация подключения к БД
    db = PostgresDB(database_url=settings.DATABASE_URL)

    # Проверка подключения
    if not db.check_connection():
        print("❌ Не удалось подключиться к базе данных")
        return False

    # Пересоздание таблиц (для разработки)
    db.drop_tables()
    db.init_db()

    # Создание тестовых данных
    try:
        session = db.get_session()

        # Создаем категории
        electronics = Category(name="Электроника")
        furniture = Category(name="Мебель")
        session.add(electronics)
        session.add(furniture)
        session.commit()

        # Создаем локации
        office = Locations(name_2022="Главный офис")
        warehouse = Locations(name_2022="Склад №1")
        session.add(office)
        session.add(warehouse)
        session.commit()

        # Создаем объекты
        laptop = Object(
            name="Ноутбук Dell",
            inventory_number="INV-001",
            quantity=5,
            comments="Новые ноутбуки для отдела разработки",
            category_id=electronics.id,
            location_id=office.id
        )

        chair = Object(
            name="Офисное кресло",
            inventory_number="FURN-001",
            quantity=10,
            comments="Эргономичные кресла",
            category_id=furniture.id,
            location_id=office.id
        )

        session.add(laptop)
        session.add(chair)
        session.commit()

        print("✅ Тестовые данные успешно созданы")
        return True

    except Exception as e:
        print(f"❌ Ошибка при создании тестовых данных: {e}")
        session.rollback()
        return False
    finally:
        session.close()


if __name__ == "__main__":
    print("\n=== Инициализация базы данных ===")

    if initialize_database():
        print("\n✅ База данных успешно инициализирована")
    else:
        print("\n❌ Произошли ошибки при инициализации базы данных")
# main.py
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from ui.logic.main_window import MainWindow
from infrastructure.db.postgres import PostgresDB
from core.settings import settings


def main():
    app = QApplication(sys.argv)

    # Инициализация БД
    db = PostgresDB(settings.DATABASE_URL)
    db.init_db()

    # Проверка подключения
    if not db.check_connection():
        QMessageBox.critical(
            None, "Ошибка",
            "Не удалось подключиться к базе данных. Проверьте настройки подключения."
        )
        sys.exit(1)

    # Создание главного окна
    window = MainWindow()
    window.setWindowTitle("Инвентаризация оборудования")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
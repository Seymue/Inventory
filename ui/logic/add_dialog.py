# ui/logic/add_dialog.py
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_addForm import Ui_Dialog
from core.model import Object, Category, Locations
from infrastructure.db.repositories import CategoryRepository, LocationsRepository, ObjectRepository


class AddDialog(QDialog, Ui_Dialog):
    def __init__(self, session, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.session = session

        # Подключение сигналов
        self.acceptButton.clicked.connect(self.save_object)
        self.cancelButton.clicked.connect(self.reject)

    def save_object(self):
        try:
            # Получение данных из формы
            name = self.nameText.text().strip()
            inventory_number = self.number_inventory_Text.text().strip()
            quantity = int(self.quantityText.text())
            category_name = self.typeText.text().strip()
            location_name = self.departament_number_Text.text().strip()
            comments = self.commentText.text().strip()

            # Поиск или создание категории
            category_repo = CategoryRepository(self.session)
            category = category_repo.get_by_name(category_name)
            if not category:
                category = Category(name=category_name)
                category_repo.add(category)

            # Поиск или создание локации
            locations_repo = LocationsRepository(self.session)
            location = locations_repo.get_by_name(location_name)
            if not location:
                location = Locations(name_2022=location_name)
                locations_repo.add(location)

            # Создание объекта
            obj = Object(
                name=name,
                inventory_number=inventory_number,
                quantity=quantity,
                comments=comments,
                category=category,
                location=location
            )

            object_repo = ObjectRepository(self.session)
            object_repo.add(obj)

            self.accept()

        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Некорректное значение количества")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить объект: {str(e)}")
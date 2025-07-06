# ui/logic/edit_dialog.py
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_editForm import Ui_Dialog
from core.model import Object, Category, Locations
from infrastructure.db.repositories import CategoryRepository, LocationsRepository, ObjectRepository


class EditDialog(QDialog, Ui_Dialog):
    def __init__(self, session, obj, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.session = session
        self.obj = obj

        # Заполнение формы данными
        self.nameText.setText(obj.name)
        self.number_inventory_Text.setText(obj.inventory_number)
        self.quantityText.setText(str(obj.quantity))
        self.typeText.setText(obj.category.name)
        self.departament_number_Text.setText(obj.location.name_2022)
        self.commentText.setText(obj.comments or "")

        # Подключение сигналов
        self.acceptButton.clicked.connect(self.update_object)
        self.cancelButton.clicked.connect(self.reject)

    def update_object(self):
        try:
            # Обновление данных объекта
            self.obj.name = self.nameText.text().strip()
            self.obj.inventory_number = self.number_inventory_Text.text().strip()
            self.obj.quantity = int(self.quantityText.text())
            self.obj.comments = self.commentText.text().strip()

            # Обновление категории
            category_repo = CategoryRepository(self.session)
            category_name = self.typeText.text().strip()
            if category_name != self.obj.category.name:
                category = category_repo.get_by_name(category_name)
                if not category:
                    category = Category(name=category_name)
                    category_repo.add(category)
                self.obj.category = category

            # Обновление локации
            locations_repo = LocationsRepository(self.session)
            location_name = self.departament_number_Text.text().strip()
            if location_name != self.obj.location.name_2022:
                location = locations_repo.get_by_name(location_name)
                if not location:
                    location = Locations(name_2022=location_name)
                    locations_repo.add(location)
                self.obj.location = location

            # Сохранение изменений


            self.accept()

        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Некорректное значение количества")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось обновить объект: {str(e)}")
# ui/logic/main_window.py
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableView, QDialog
from ui.ui_mainwindow import Ui_MainWindow
from .models import ObjectTableModel
from .add_dialog import AddDialog
from .edit_dialog import EditDialog
from infrastructure.db.postgres import PostgresDB
from core.settings import settings




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Инициализация БД
        self.db = PostgresDB(settings.DATABASE_URL)
        self.session = self.db.get_session()

        # Настройка модели данных
        self.model = ObjectTableModel(self.session)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QTableView.SelectRows)

        # Подключение сигналов
        self.addButton.clicked.connect(self.add_object)
        self.editButton.clicked.connect(self.edit_object)
        self.deleteButton.clicked.connect(self.delete_object)
        self.findButton.clicked.connect(self.find_objects)

    def add_object(self):
        dialog = AddDialog(self.session, self)
        dialog.setWindowTitle("Добавление")
        if dialog.exec() == QDialog.Accepted:
            self.model.refresh()

    def edit_object(self):
        index = self.tableView.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Ошибка", "Выберите объект для редактирования")
            return

        obj = self.model.get_object(index)
        dialog = EditDialog(self.session, obj, self)
        dialog.setWindowTitle("Изменение")
        if dialog.exec() == QDialog.Accepted:
            self.model.refresh()

    def delete_object(self):
        index = self.tableView.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Ошибка", "Выберите объект для удаления")
            return

        obj = self.model.get_object(index)
        reply = QMessageBox.question(
            self, "Подтверждение",
            f"Удалить объект '{obj.name}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                self.model.repository.delete(obj)
                self.model.refresh()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось удалить объект: {str(e)}")

    def find_objects(self):
        filter_text = self.findText.text()
        self.model.refresh(filter_text)

    def closeEvent(self, event):
        self.session.close()
        super().closeEvent(event)
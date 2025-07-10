# ui/logic/main_window.py
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableView, QDialog, QApplication, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
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
        self.findButton.clicked.connect(self.find_objects)

        # Настройка контекстного меню для таблицы
        self.setup_table_context_menu()

    def add_object(self):
        dialog = AddDialog(self.session, self)
        dialog.setWindowTitle("Добавление")
        if dialog.exec() == QDialog.Accepted:
            self.model.refresh()
            self.tableView.viewport().update()

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



    def setup_table_context_menu(self):
        """Настройка контекстного меню для таблицы"""
        # Разрешаем контекстное меню
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        """Показ контекстного меню в позиции курсора"""
        # Создаем меню
        menu = QMenu(self)

        # Добавляем действия
        add_action = QAction("Добавить", self)
        add_action.triggered.connect(self.add_object)
        menu.addAction(add_action)

        # Проверяем, есть ли выделенная строка
        selected = self.tableView.selectionModel().selectedRows(0)
        if selected:
            edit_action = QAction("Изменить", self)
            edit_action.triggered.connect(self.edit_object)
            menu.addAction(edit_action)

            delete_action = QAction("Удалить", self)
            delete_action.triggered.connect(self.delete_object)
            menu.addAction(delete_action)

            copy_action = QAction("Копировать", self)
            copy_action.triggered.connect(self.copy_selected)
            menu.addAction(copy_action)

        # Добавляем разделитель
        menu.addSeparator()

        # Добавляем действие обновления
        refresh_action = QAction("Обновить", self)
        refresh_action.triggered.connect(self.refresh_table)
        menu.addAction(refresh_action)

        # Показываем меню в позиции курсора
        menu.exec_(self.tableView.viewport().mapToGlobal(pos))

    def copy_selected(self):
        """Копирование выделенных данных в буфер обмена"""
        selected = self.tableView.selectionModel().selectedRows()
        if not selected:
            return

        # Получаем данные выделенных строк
        clipboard_text = ""
        for row_index in sorted(set(index.row() for index in selected)):
            row_data = []
            for col in range(self.model.columnCount()):
                item = self.model.item(row_index, col)
                row_data.append(item.text() if item else "")
            clipboard_text += "\t".join(row_data) + "\n"

        # Копируем в буфер обмена
        QApplication.clipboard().setText(clipboard_text.strip())

    def refresh_table(self):
        """Обновление таблицы"""
        # Здесь можно добавить логику перезагрузки данных
        # Например: self.load_data_from_database()
        QMessageBox.information(self, "Обновление", "Таблица обновлена")
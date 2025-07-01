import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableView, QMessageBox, QPushButton
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QFile
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_addForm import Ui_Dialog  # Импорт интерфейса формы добавления

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_table()
        self.ui.addButton.clicked.connect(self.open_add_form)
        #self.ui.editButton.clicked.connect(self.edit_item)
        self.ui.deleteButton.clicked.connect(self.delete_item)
    def init_table(self):
            """Инициализация таблицы с данными"""
            # Создаем модель данных
            self.model = QStandardItemModel()

            # Устанавливаем заголовки столбцов
            self.model.setHorizontalHeaderLabels([
                "ID",
                "Название",
                "Номер инвентаризации",
                "Тип",
                "Количество",
                "Номер кабинета",
                "Номер отдела",
                "Комментарий"
            ])


            # Привязываем модель к таблице
            self.ui.tableView.setModel(self.model)

            # Настройка внешнего вида таблицы
            self.ui.tableView.setSelectionBehavior(QTableView.SelectRows)  # Выделение строк
            self.ui.tableView.setEditTriggers(QTableView.NoEditTriggers)  # Запрет редактирования

            # Загружаем тестовые данные
            self.load_sample_data()

    def open_add_form(self):
        """Открывает диалоговое окно добавления"""
        dialog = QDialog(self)  # Создаем диалог
        add_form = Ui_Dialog()  # Создаем UI формы
        add_form.setupUi(dialog)  # Инициализируем UI в диалоге

        # Показываем диалог как модальное окно
        dialog.exec()

    def delete_item(self):

        selected = self.ui.tableView.selectionModel().selectedRows(0)
        if not selected:

            msg_box, buttons = self.create_custom_message_box(
                "Ошибка",
                "Выберите объект для удаления",
                ["ОК"]
            )
            msg_box.exec()
            return

        row_index = selected[0].row()
        item_id = self.model.item(row_index, 0).text()


        msg_box, buttons = self.create_custom_message_box(
            "Подтверждение удаления",
            f"Вы уверены, что хотите удалить объект с ID {item_id}?",
            ["Да", "Нет"]
        )

        # Показываем сообщение и ждем ответа
        msg_box.exec()

        if msg_box.clickedButton() == buttons[0]:  # Кнопка "Да"
            self.model.removeRow(row_index)

            success_box, _ = self.create_custom_message_box(
                "Успех",
                f"Объект с ID {item_id} удален",
                ["ОК"]
            )
            success_box.exec()

    def create_custom_message_box(self, title, text, button_texts):

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)

        msg_box.setStyleSheet("""
            QMessageBox {

            }
            QLabel {
                color: #E0E0E0;
                font-family: 'Segoe UI';
                font-size: 10pt;
            }
            QPushButton {
                background-color: #007ACC;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 4px;
                font-family: 'Segoe UI';
                font-size: 8pt;
            }
            QPushButton:hover {
                background-color: #0099FF;
            }
            QPushButton:pressed {
                background-color: #005A9E;
                padding-top: 9px;
                padding-bottom: 7px;
            }
        """)

        # Создаем кастомные кнопки
        buttons = []
        for text in button_texts:
            button = QPushButton(text)
            buttons.append(button)
            msg_box.addButton(button, QMessageBox.ActionRole)

        msg_box.setIcon(QMessageBox.Information)

        return msg_box, buttons

    def load_sample_data(self):
        """Загрузка тестовых данных в таблицу"""
        sample_data = [
            ["1","Компьютер", "INV-001", "Техника", "1", "101", "IT", "Новый"],
            ["2","Монитор", "INV-002", "Техника", "2", "102", "Бухгалтерия", "Исправен"],
            ["3","Принтер", "INV-003", "Техника", "1", "103", "Отдел кадров", "Требуется ТО"],
            ["4","Стол", "INV-004", "Мебель", "5", "201", "Общий", ""],
            ["5","Кресло", "INV-005", "Мебель", "10", "202", "Общий", "Кожаное"],
        ]

        for row_data in sample_data:
            row = []
            for item in row_data:
                cell = QStandardItem(item)
                row.append(cell)
            self.model.appendRow(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QFile
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_addForm import Ui_Dialog  # Импорт интерфейса формы добавления

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.open_add_form)

    def open_add_form(self):
        """Открывает диалоговое окно добавления"""
        dialog = QDialog(self)  # Создаем диалог
        add_form = Ui_Dialog()  # Создаем UI формы
        add_form.setupUi(dialog)  # Инициализируем UI в диалоге

        # Показываем диалог как модальное окно
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

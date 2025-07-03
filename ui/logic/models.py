from sqlalchemy.orm import Session
from infrastructure.db.repositories import ObjectRepository
from PySide6.QtCore import QAbstractTableModel, Qt


class ObjectTableModel(QAbstractTableModel):
    def __init__(self, session: Session, parent=None):
        super().__init__(parent)
        self.session = session
        self.repository = ObjectRepository(session)
        self.objects = []
        self.headers = [
            "ID", "Название", "Инвентарный номер",
            "Количество", "Категория", "Локация", "Комментарий"
        ]
        self.refresh()

    def refresh(self, filter_text=None):
        self.beginResetModel()
        if filter_text:
            self.objects = self.repository.search_by_name(filter_text)
        else:
            self.objects = self.repository.get_all()
        self.endResetModel()

    def rowCount(self, parent=None):
        return len(self.objects)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            obj = self.objects[index.row()]
            col = index.column()
            if col == 0:
                return obj.id
            elif col == 1:
                return obj.name
            elif col == 2:
                return obj.inventory_number
            elif col == 3:
                return obj.quantity
            elif col == 4:
                return obj.category.name
            elif col == 5:
                return obj.location.name_2022
            elif col == 6:
                return obj.comments
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return None

    def get_object(self, index):
        if index.isValid():
            return self.objects[index.row()]
        return None
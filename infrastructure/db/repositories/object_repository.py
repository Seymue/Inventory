from sqlalchemy.orm import Session
from core.model.object import Object
from infrastructure.db.repositories.base_repository import BaseRepository


class ObjectRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Object)

    def get_by_inventory_number(self, inventory_number: str):
        """Получить объект по инвентарному номеру"""
        return self.session.query(Object).filter_by(inventory_number=inventory_number).first()

    def get_by_category_id(self, category_id: int):
        """Получить все объекты с заданной категорией"""
        return self.session.query(Object).filter_by(category_id=category_id).all()

    def get_by_location_id(self, location_id: int):
        """Получить все объекты в заданной локации"""
        return self.session.query(Object).filter_by(location_id=location_id).all()

    def search_by_name(self, keyword: str):
        """Поиск по части имени"""
        return self.session.query(Object).filter(Object.name.ilike(f"%{keyword}%")).all()

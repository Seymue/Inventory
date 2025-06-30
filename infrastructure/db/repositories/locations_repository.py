from sqlalchemy.orm import Session
from core.model.locations import Locations
from infrastructure.db.repositories.base_repository import BaseRepository


class LocationsRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Locations)

    def get_by_name(self, name: str):
        """Получить локацию по точному имени (name_2022)"""
        return self.session.query(Locations).filter_by(name_2022=name).first()

    def search_by_partial_name(self, keyword: str):
        """Поиск локации по части имени (name_2022)"""
        return self.session.query(Locations).filter(Locations.name_2022.ilike(f"%{keyword}%")).all()

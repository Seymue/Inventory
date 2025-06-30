from sqlalchemy.orm import Session
from core.model.category import Category
from infrastructure.db.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Category)

    def get_by_name(self, name: str):
        """Получить категорию по имени"""
        return self.session.query(Category).filter_by(name=name).first()

    def search_by_partial_name(self, keyword: str):
        """Поиск категории по части имени"""
        return self.session.query(Category).filter(Category.name.ilike(f"%{keyword}%")).all()

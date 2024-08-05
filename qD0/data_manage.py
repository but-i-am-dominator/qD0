from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for declarative class definitions.
Base = declarative_base()

class project_table(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    create_date = Column(Integer, nullable=False)

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.engine = create_engine(f'sqlite:///{self.db_name}')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def add_project(self, name, age):
        new_project = project_table(name=name, age=age)
        self.session.add(new_project)
        self.session.commit()

    def get_projects(self):
        return self.session.query(project_table).all()
from sqlalchemy import Column, String, Float, Boolean, ARRAY, JSON, Integer
from db.database import Base

class Country(Base):
    __tablename__ = "countries"

    code = Column(String(length=2), primary_key=True, index=True)
    name = Column(String, index=True)
    official_name = Column(String)
    flag = Column(String)
    native_names = Column(JSON)
    coat_of_arms = Column(String)
    
    capital = Column(ARRAY(String))
    region = Column(String, index=True)
    subregion = Column(String, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    borders = Column(ARRAY(String))
    area = Column(Float, index=True)
    population = Column(Integer, index=True)
    
    independent = Column(Boolean, index=True)
    
    def __repr__(self):
        return f"<Country(code='{self.code}', name='{self.name}')>"
    

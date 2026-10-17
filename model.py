from datetime import datetime
from sqlalchemy import Column, Integer, Text, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


engine = create_engine("sqlite:///Text_Analyzer.db")

class Analysis(Base):
    __tablename__ = "analysis"
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable = False)
    date_entered = Column(DateTime, nullable = False, default = datetime.now)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)



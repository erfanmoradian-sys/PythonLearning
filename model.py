from datetime import datetime
from sqlalchemy import Column, Integer, Text, DateTime, Float, JSON, create_engine
from sqlalchemy.orm import declarative_base,Mapped, mapped_column, sessionmaker

Base = declarative_base()


engine = create_engine("sqlite:///Text_Analyzer.db")

class Analysis(Base):
    __tablename__ = "analysis"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable = False)
    date_entered: Mapped[datetime] = mapped_column(DateTime, nullable = False, default = datetime.now)
    words: Mapped[int] = mapped_column(Integer, nullable=False )
    num_of_char: Mapped[int] = mapped_column(Integer, nullable=False)
    num_of_char_and_space: Mapped[int] = mapped_column(Integer, nullable=False)
    num_of_lines: Mapped[int] = mapped_column(Integer, nullable=False)
    num_of_sentence: Mapped[int] = mapped_column(Integer, nullable=False)
    five_common_words: Mapped[list] = mapped_column(JSON)
    average_length: Mapped[Float] = mapped_column(Float)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine, expire_on_commit=False)



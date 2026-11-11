from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, JSON, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base,Mapped, mapped_column, sessionmaker
from flask_login import UserMixin

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
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable = True)

class User(Base, UserMixin):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable = False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable = False )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable = False)
    password: Mapped[str] = mapped_column(String(255), nullable = False)
    

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine, expire_on_commit=False)



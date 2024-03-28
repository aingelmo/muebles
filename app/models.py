from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    materials = relationship("Material", back_populates="article")
    finishings = relationship("Finishing", back_populates="article")
    dimensions = relationship("Dimension", back_populates="article")


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    article_id = Column(Integer, ForeignKey("articles.id"))
    article = relationship("Article", back_populates="materials")


class Finishing(Base):
    __tablename__ = "finishings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    article_id = Column(Integer, ForeignKey("articles.id"))
    article = relationship("Article", back_populates="finishings")


class Dimension(Base):
    __tablename__ = "dimensions"

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    width = Column(Integer)
    thickness = Column(Integer)

    name = Column(String, index=True)
    price = Column(Integer)
    article_id = Column(Integer, ForeignKey("articles.id"))
    article = relationship("Article", back_populates="dimensions")

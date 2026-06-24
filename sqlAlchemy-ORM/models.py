from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

    posts = relationship(
        "Post",
        back_populates="user"
    )


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.user_id")
    )

    user = relationship(
        "User",
        back_populates="posts"
    )
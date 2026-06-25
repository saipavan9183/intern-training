from database import SessionLocal
from crud import (
    create_user,
    get_users,
    create_post,
    update_user,
    delete_post
)
from models import User

db = SessionLocal()

# CREATE USER
user = create_user(
    db,
    "Sai Pavan",
    "pavan_new@gmail.com"
)

# CREATE POSTS
create_post(
    db,
    "Learning SQLAlchemy",
    "ORM Basics",
    user.user_id
)

create_post(
    db,
    "PostgreSQL Practice",
    "Relationships",
    user.user_id
)

# READ
users = get_users(db)

for u in users:
    print(u.name)

# UPDATE
update_user(
    db,
    user.user_id,
    "Sai"
)

# RELATIONSHIP QUERY
user = (
    db.query(User)
    .filter(User.name == "Sai")
    .first()
)

print(f"\nUser: {user.name}")

for post in user.posts:
    print(post.title)

# DELETE
delete_post(
    db,
    2
)
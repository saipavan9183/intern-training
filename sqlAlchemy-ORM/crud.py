from models import User, Post


def create_user(db, name, email):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db):
    return db.query(User).all()


def get_user_by_name(db, name):
    return db.query(User).filter(User.name == name).first()


def update_user(db, user_id, new_name):
    user = db.query(User).filter(User.user_id == user_id).first()

    if user:
        user.name = new_name
        db.commit()
        db.refresh(user)

    return user


def delete_post(db, post_id):
    post = db.query(Post).filter(Post.post_id == post_id).first()

    if post:
        db.delete(post)
        db.commit()


def create_post(db, title, content, user_id):
    post = Post(
        title=title,
        content=content,
        user_id=user_id
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post
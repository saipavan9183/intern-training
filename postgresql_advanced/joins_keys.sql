create table users (user_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,name VARCHAR(100) NOT NULL , email VARCHAR(100) UNIQUE);

INSERT INTO users(name, email)
VALUES
    ('sai pavan', 'pavan123@gmail.com'),
    ('surendra', 'surendra234@gmail.com'),
    ('bhargav', 'bhargav23@gmail.com'),
    ('kiran', 'kiran43@gmail.com'),
    ('manoj', 'manoj159@gmail.com');

select*from users;

CREATE TABLE posts (
    post_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO posts (title, content, user_id)
VALUES
('First Post', 'Learning PostgreSQL', 1),
('Second Post', 'Working with joins', 1),
('FastAPI Basics', 'Creating APIs', 2),
('Python Tips', 'Useful Python tricks', 3);

select*from posts;

UPDATE posts
SET title = 'Advanced PostgreSQL'
WHERE post_id = 1;

DELETE FROM posts 
WHERE post_id = 4;

SELECT
    u.name,
    p.title
FROM posts p
INNER JOIN users u
ON p.user_id = u.user_id;

SELECT
    u.user_id,
    u.name,
    p.title
FROM users u
LEFT JOIN posts p
ON u.user_id = p.user_id;

SELECT
    u.name,
    COUNT(p.post_id) AS post_count
FROM users u
LEFT JOIN posts p
ON u.user_id = p.user_id
GROUP BY u.user_id, u.name;


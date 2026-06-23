create table users (user_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,name VARCHAR(100) NOT NULL , email VARCHAR(100) UNIQUE);
-- insert into users ( name , email)
-- values ('sai pavan','pavan123@gmail.com'),
--        ('surendra','surendra234@gmail.com'),
-- 	   ('bhargav' , 'bhargav23@gmail.com'),
-- 	   ('kiran' , 'kiran43@gmail.com'),
-- 	   ('manoj' , 'manoj159@gmail.com');

INSERT INTO users(name, email)
VALUES
    ('sai pavan', 'pavan123@gmail.com'),
    ('surendra', 'surendra234@gmail.com'),
    ('bhargav', 'bhargav23@gmail.com'),
    ('kiran', 'kiran43@gmail.com'),
    ('manoj', 'manoj159@gmail.com');

select*from users;

select * from users 
where name='kiran';

select * from users 
order by user_id desc;

select * from users 
order by email;

select name,user_id from users
order by email;




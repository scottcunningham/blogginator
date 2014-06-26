drop table if exists posts;
create table posts (
    post_id integer primary key autoincrement,
    date integer not null,
    title text not null,
    content text not null
);
drop table if exists users;
create table users (
    user_id integer primary key autoincrement,
    username text not null,
    real_name text,
    password_hash text not null
);

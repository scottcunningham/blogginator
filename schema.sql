drop table if exists posts;
create table posts (
  post_id integer primary key autoincrement,
  date integer not null,
  title text not null,
  content text not null
);

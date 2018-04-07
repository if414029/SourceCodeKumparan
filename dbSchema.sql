-- database for news, news_topic, and topic
-- news consists of id_news, title, content, image, and status
-- news_topic consist of id_newstopic, id_news, and id_topic
-- topic consist of id_topic and topic


drop table if exists news;
create table news (
  id_news integer primary key autoincrement,
  title text not null,
  content text not null,
  image text,
  status text
);

drop table if exists topic;
create table topic (
    id_topic integer primary key autoincrement,
    topic text not null
);


drop table if exists news_topic;
create table news_topic (
  id_newstopic integer primary key autoincrement,
  id_news integer,
  id_topic integer,
  foreign key (id_news) references news(id_news),
  foreign key (id_topic) references  topic(id_topic)
);

INSERT INTO news (id_news, title, content, image, status) VALUES (1, 'First Title', 'First Content.', '', 'publish');
INSERT INTO topic (id_topic, topic) VALUES (1, 'Politik');
INSERT INTO news_topic (id_news, id_topic) VALUES (1, 1);

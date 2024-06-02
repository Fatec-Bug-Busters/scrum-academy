-- run with `sudo mysql -u root -p < scripts.sql

create database scrumacademy;
use scrumacademy;

create table users (
    `id` int auto_increment primary key,
    `name` varchar(255) null,
    `email` varchar(320) not null,
    `created_at` datetime not null
);

create table iterations (
    `id` int auto_increment primary key,
    `is_finished` boolean not null default false,
    `total_score` int null,
    `review_score` int null,
    `review_comment` varchar(255) null,
    `created_at` datetime not null,
    `finished_at` datetime null
);

create table quizzes (
    `id` int auto_increment primary key,
    `iteration_id` int not null,
    `index` int not null,
    `score` int not null,
    `users_answer` varchar(127) not null,
    `created_at` datetime not null,

    foreign key (iteration_id) references iterations(id)
);

create table exams (
    `id` int auto_increment primary key,
    `score` int not null,
    `users_answer` varchar(255) not null,
    `created_at` datetime not null
);
CREATE VIEW minha_view2 AS
SELECT t1.id, t1.name, t2.score, t3.review_comment, t3.review_score
FROM users t1, exams t2, iterations t3;

CREATE VIEW minha_view2 AS
SELECT t1.id, t1.name, t2.score, t3.review_comment, t3.review_score
FROM users t1, exams t2, iterations t3;

-- create user
CREATE USER 'scrum'@'localhost' IDENTIFIED WITH caching_sha2_password BY '123456';
GRANT ALL PRIVILEGES ON scrumacademy.* TO 'scrum'@'localhost' WITH GRANT OPTION;

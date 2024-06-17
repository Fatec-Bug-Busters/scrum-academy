-- run with `sudo mysql -u root -p < scripts.sql

create database if not exists scrumacademy;
use scrumacademy;

create table users (
    `id` int auto_increment primary key,
    `name` varchar(255) null,
    `email` varchar(320) not null,
    `created_at` datetime not null
);

create table exams (
    `id` int auto_increment primary key,
    `user_id` int not null,
    `score` int not null,
    `review_score` int null,
    `review_comment` varchar(255) null,
    `created_at` datetime not null,
    foreign key (user_id) references users(id)
);

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
    `users_id` int not null,
    `total_score` int null,
    `review_score` int null,
    `review_comment` varchar(255) null,
    `created_at` datetime not null,
    foreign key (users_id) references users(id)
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


INSERT into users (id, name, email, created_at) VALUES
('5', 'Guilhermo Lasso', 'guilaso@bol.com', "2024-06-02 18:01:09" ),
('6', 'Leopoldina Maria Francista', 'mafra@gmail.com', "2024-06-02 18:01:09"),
('7', 'Simón Bolivar', 'revolucion@onionproyect.com', "2024-06-02 18:01:09"),
('8', 'Dilma Rousseff', 'presidenta@pt.org.br', "2024-06-02 18:01:09"),
('9', 'João Emanuel Carneiro', 'producao@globo.com', "2024-06-02 18:01:09"),
('10', 'Georfe Boole', 'boleano@official.uk', "2024-06-02 18:01:09"),
('11', 'Leon Trotsky', 'frida@onionproyect.com', "2024-06-02 18:01:09"),
('12', 'Frida Kahlo', 'leonmiamor@onioproyect.com', "2024-06-02 18:01:09");

INSERT into iterations (users_id, total_score, review_score, review_comment, created_at) VALUES
('5', '10', '5', 'El mejor sitio para agregar conocimientos en Scrum', "2024-06-02 18:01:09" ),
('6', '9', '5', 'Aonde é que eu assino para pegar o certificado?' , "2024-06-02 18:01:09"),
('7', '10', '4','Não sei como fui aprovado, foi um processo muito intenso e imersivo', "2024-06-02 18:01:09" ),
('8', '8', '5', "Eu sabia que detrás de um cachorro, que estava escondido atrás da figura de um menino, havia hight tec tec", "2024-06-02 18:01:09"),
('9', '8', '5', 'Trama típica de uma das minhas novelas!', "2024-06-02 18:01:09"),
('10', '10', '3', 'Vocês usaram bem a matemática que eu inventei, rapazes!', "2024-06-02 18:01:09"),
('11', '5', '2', 'Só fiz porque minha mulher mandou', "2024-06-02 18:01:09"),
('12', '10', '4', 'O de cima é meu pau-mandado', "2024-06-02 18:01:09");

-- create user
CREATE USER 'scrum'@'localhost' IDENTIFIED WITH caching_sha2_password BY '123456';
GRANT ALL PRIVILEGES ON scrumacademy.* TO 'scrum'@'localhost' WITH GRANT OPTION;

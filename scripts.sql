-- run with `sudo mysql -u root -p < scripts.sql

create database if not exists scrumacademy;
use scrumacademy;

create table users (
    `id` int auto_increment primary key,
    `name` varchar(255) null,
    `email` varchar(320) not null,
    `created_at` datetime not null
);

create table quizzes (
    `id` int auto_increment primary key,
    `user_id` int not null,
    `index` int not null,
    `score` int not null,
    `users_answer` varchar(127) not null,
    foreign key (user_id) references users(id)
);

create table exams (
    `id` int auto_increment primary key,
    `user_id` int not null,
    `score` int not null,
    `users_answer` varchar(255) not null,
    `review_score` int null,
    `review_comment` varchar(255) null,
    `created_at` datetime not null,
    foreign key (user_id) references users(id)
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

INSERT INTO exams (user_id, score, users_answer, review_score, review_comment, created_at) VALUES 
('5', '10', '{"q1": "b", "q2": "b", "q3": "b", "q4": "b", "q5": "b", "q6": "b", "q7": "b", "q8": "b", "q9": "b", "q10": "b"}', '5', 'El mejor sitio para agregar conocimientos en Scrum', "2024-06-02 18:01:09"), 
('6', '9', '{"q1": "a", "q2": "b", "q3": "b", "q4": "b", "q5": "b", "q6": "b", "q7": "b", "q8": "b", "q9": "b", "q10": "b"}', '4', 'Aonde é que eu assino para pegar o certificado?', "2024-06-02 18:01:09"), 
('7', '8', '{"q1": "a", "q2": "a", "q3": "b", "q4": "b", "q5": "b", "q6": "b", "q7": "b", "q8": "b", "q9": "b", "q10": "b"}', '5', 'Não sei como fui aprovado, foi um processo muito intenso e imersivo', "2024-06-02 18:01:09"), 
('8', '8', '{"q1": "a", "q2": "a", "q3": "b", "q4": "b", "q5": "b", "q6": "b", "q7": "b", "q8": "b", "q9": "b", "q10": "b"}', '4', 'Eu sabia que detrás de um cachorro, que estava escondido atrás da figura de um menino, havia hight tec tec', "2024-06-02 18:01:09"),  
('9', '8', '{"q1": "a", "q2": "a", "q3": "b", "q4": "b", "q5": "b", "q6": "b", "q7": "b", "q8": "b", "q9": "b", "q10": "b"}', '4', 'Trama típica de uma das minhas novelas!', "2024-06-02 18:01:09"), 
('10', '9', '{"q1": "b", "q2": "a", "q3": "b", "q4": "b", "q5": "b", "q6": "b", "q7": "b", "q8": "b", "q9": "b", "q10": "b"}', '5', 'Vocês usaram bem a matemática que eu inventei, rapazes!', "2024-06-02 18:01:09"), 
('11', '5', '{"q1": "b", "q2": "a", "q3": "a", "q4": "a", "q5": "a", "q6": "a", "q7": "b", "q8": "b", "q9": "b", "q10": "b"}', '3', 'Só fiz porque minha mulher mandou', "2024-06-02 18:01:09"), 
('12', '10', '{"q1": "a", "q2": "a", "q3": "b", "q4": "b", "q5": "b", "q6": "b", "q7": "b", "q8": "b", "q9": "b", "q10": "b"}', '5', 'O de cima é meu pau-mandado', "2024-06-02 18:01:09");


-- create user
CREATE USER 'scrum'@'localhost' IDENTIFIED WITH caching_sha2_password BY '123456';
GRANT ALL PRIVILEGES ON scrumacademy.* TO 'scrum'@'localhost' WITH GRANT OPTION;

-- запросы для выдачи данных из БД

-- создание таблиц компаний

create table vacancies (id serial PRIMARY KEY,
                           description text,
                           employer varchar(50),
                           experience varchar(30),
                           salary int,
                           url varchar(100));


-- создание таблиц вакансий

create table employers(id serial PRIMARY KEY,
                        company_name varchar(200));
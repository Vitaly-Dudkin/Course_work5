-- запросы для выдачи данных из БД

-- создание таблиц компаний

create table if not exists placeholder (id serial PRIMARY KEY,
                           description text,
                           employer varchar(50),
                           experience varchar(30),
                           salary int,
                           url varchar(100));


-- создание таблиц вакансий

create table if not exists employers(company_name varchar(200) PRIMARY KEY)
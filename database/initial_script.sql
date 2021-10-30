-- create table titles
create table titles
(
    id serial primary key,
    title_name varchar(255) unique,
    basic_salary int,
    group_id int
);

-- create table employees
create table employees
(
    id serial primary key,
    first_name varchar(30),
    last_name varchar(30),
    title_id int references titles (id),
    mail varchar(255),
    phone int,
    login varchar(255),
    password varchar(255)
);

-- create table worktime
create table worktime
(
    employee_id int,
    start_time timestamp,
    end_time timestamp
);

select * from titles;
select * from employees;
select * from worktime;

select * from job_service.worktime;


-- create table worktime
create table job_service.worktime
(
    employee_id int,
    start_time timestamp,
    end_time timestamp
);

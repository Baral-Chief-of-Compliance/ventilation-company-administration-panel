show databases;
create database ventilation_supply_сontrol;
use ventilation_supply_сontrol;
show tables;


create table operator(
	id int primary key unique auto_increment not null,
    surname varchar(20) not null,
    name varchar(20) not null,
    patronymic varchar(20) null,
    login varchar(20) not null unique,
    password_hash varchar(128) not null,
    phone varchar(12) not null unique
);


create table address(
	id int primary key unique auto_increment not null,
    street varchar(64) not null,
    house int not null,
    frame int null,
    longitude varchar(20) not null,
    latitude varchar(20) not null
);


create table brigade(
	id int primary key unique auto_increment not null,
    name varchar(20) not null
);


create table employee(
	id int primary key unique auto_increment not null,
	surname varchar(20) not null,
    name varchar(20) not null,
    patronymic varchar(20) null,
    position varchar(25) not null,
	phone varchar(12) not null unique,
    br_id int not null unique,
    foreign key (br_id) references brigade(id) on delete cascade on update cascade
);


create table client(
	id int primary key unique auto_increment not null,
	surname varchar(20) not null,
    name varchar(20) not null,
    patronymic varchar(20) null,
    phone varchar(12) not null unique
);


create table phys(
	cl_id int not null unique,
    adr_id int not null,
    primary key(cl_id),
    foreign key (cl_id) references client(id) on delete cascade on update cascade,
    foreign key (adr_id) references address(id) on delete cascade on update cascade
);


create table entity(
	cl_id int not null unique,
    name_of_company varchar(64) not null unique,
    inn varchar(10) not null unique,
    foreign key (cl_id) references client(id) on delete cascade on update cascade
);


create table stack(
	id int primary key unique auto_increment not null,
    adr_id int not null, 
	foreign key (adr_id) references address(id) on delete cascade on update cascade
);


create table materials(
	id int primary key unique auto_increment not null,
    stack_id int not null,
    name varchar(64) not null,
    quantity int null,
    foreign key (stack_id) references stack(id) on delete cascade on update cascade
);


drop table application;
create table application(
	id int primary key unique auto_increment not null,
    cl_id int not null,
    op_id int not null,
    br_id int not null,
    date_create DATE not null,
    date_start_work DATE not null,
    date_end_work DATE not null,
    date_close DATE null,
    days_of_delay int null,
	adr_id int not null, 
    foreign key (cl_id) references client(id) on delete cascade on update cascade,
	foreign key (op_id) references operator(id) on delete cascade on update cascade,
    foreign key (br_id) references brigade(id) on delete cascade on update cascade,
	foreign key (adr_id) references address(id) on delete cascade on update cascade
);


create table materials_in_order(
	m_id int not null,
    app_id int not null,
    quantity int not null,
    primary key (m_id, app_id),
    foreign key (m_id) references materials(id) on delete cascade on update cascade,
    foreign key (app_id) references application(id) on delete cascade on update cascade
);
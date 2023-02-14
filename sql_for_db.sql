show databases;
create database ventilation_supply_сontrol;
use ventilation_supply_сontrol;
show tables;

select * from operator;
create table operator(
	id int primary key unique auto_increment not null,
    surname varchar(20) not null,
    name varchar(20) not null,
    patronymic varchar(20) null,
    login varchar(20) not null unique,
    password_hash varchar(128) not null,
    phone varchar(12) not null unique
);

select * from address;
create table address(
	id int primary key unique auto_increment not null,
    street varchar(64) not null,
    house int not null,
    frame int null,
    longitude varchar(20) not null,
    latitude varchar(20) not null
);

alter table address
add apartment int null;

alter table address
add town varchar(24) not null;

select * from brigade;
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


select * from client;
create table client(
	id int primary key unique auto_increment not null,
	surname varchar(20) not null,
    name varchar(20) not null,
    patronymic varchar(20) null,
    phone varchar(12) not null unique
);


select * from phys;
create table phys(
	cl_id int not null unique,
    adr_id int not null,
    primary key(cl_id),
    foreign key (cl_id) references client(id) on delete cascade on update cascade,
    foreign key (adr_id) references address(id) on delete cascade on update cascade
);



select * from entity;
create table entity(
	cl_id int not null unique,
    name_of_company varchar(64) not null unique,
    inn varchar(20) not null unique,
    foreign key (cl_id) references client(id) on delete cascade on update cascade
);


select * from stack;
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


DELIMITER //
drop procedure all_brigades;
create procedure add_brigade(
		name varchar(20)
)
begin
	insert into brigade(brigade.name) values (name);
end//


create procedure all_brigades()
begin
	select * from brigade;
end//


create procedure inf_about_brigade(
									id int
)
begin
	select brigade.name from brigade where brigade.id = id;
end//


create procedure delete_brigade(
									id int
)
begin
	delete from brigade where brigade.id = id;
end//

create procedure all_employess()
begin
	select * from employee;
end//

drop procedure add_employee;
create procedure add_employee(
								surname varchar(20),
								name varchar(20),
								patronymic varchar(20),
								position varchar(25),
								phone varchar(12),
								br_id int
)
begin
	insert into employee(employee.surname, employee.name, employee.patronymic, employee.position, employee.phone , employee.br_id) values (surname, name, patronymic, position, phone, br_id);
end//


create procedure inf_about_employee(
										id int
)
begin
	select employee.surname, employee.name, employee.patronymic, employee.position, employee.phone , employee.br_id from employee where employee.id = id;
end//


create procedure delete_employee(
									id int
)
begin
	delete from employee where employee.id = id;
end//


create procedure all_operators()
begin
	select * from operator;
end//


create procedure add_operator(
								surname varchar(20),
								name varchar(20),
								patronymic varchar(20),
								login varchar(20),
								password_hash varchar(128),
								phone varchar(12)
)
begin
	insert into operator(operator.surname, operator.name, operator.patronymic, operator.login, operator.password_hash, operator.phone) 
    values(surname, name, patronymic, login, password_hash, phone);
end//


create procedure inf_about_operator(
										id int
)
begin
	select operator.surname, operator.name, operator.patronymic, operator.login, operator.password_hash , operator.phone from operator where operator.id = id;
end//



create procedure delete_operator(
										id int
)
begin
	delete from operator where operator.id = id;
end//



create procedure create_phys_client(
										surname varchar(20),
                                        name varchar(20),
                                        patronymic varchar(20),
                                        phone varchar(12),
                                        town varchar(24),
                                        street varchar(64),
                                        house int,
                                        frame int,
                                        apartment int,
                                        longitude varchar(20),
                                        latitude varchar(20)
)
begin
	insert into client(client.surname, client.name, client.patronymic, client.phone) values (surname, name, patronymic, phone);
    insert into address(address.street, address.house, address.frame, address.apartment, address.longitude, address.latitude, address.town) values (street, house, frame, apartment, longitude, latitude, town);
    select @cl_id := max(id) from client;
    select @adr_id := max(id) from address;
    insert into phys(phys.cl_id, phys.adr_id) values(@cl_id, @adr_id);
end//

drop procedure inf_about_phys_client;
create procedure inf_about_phys_client(
										id int
)
begin
		select client.surname, client.name, client.patronymic, client.phone, address.town, address.street, address.house, address.frame, address.apartment, address.longitude, address.latitude 
        from client
        inner join phys
        on client.id = phys.cl_id
        inner join address
        on phys.adr_id = address.id
        where client.id = id;
end//


create procedure all_phys_clients()
begin
		select client.id, client.surname, client.name, client.patronymic, client.phone, address.town, address.street, address.house, address.frame, address.apartment, address.longitude, address.latitude 
        from client
        inner join phys
        on client.id = phys.cl_id
        inner join address
        on phys.adr_id = address.id;
end//


create procedure delete_phys_clients(
										id int
)
begin
		delete client, address, phys
        from client
        inner join phys
        on client.id = phys.cl_id
        inner join address
        on phys.adr_id = address.id
        where client.id = id;
end//



create procedure add_entity_client(
										surname varchar(20),
                                        name varchar(20),
                                        patronymic varchar(20),
                                        phone varchar(12),
                                        name_of_company varchar(64),
                                        inn varchar(20)
)
begin
	insert into client(client.surname, client.name, client.patronymic, client.phone) values (surname, name, patronymic, phone);
    select @cl_id := max(id) from client;
    insert into entity(entity.cl_id, entity.name_of_company, entity.inn) values(@cl_id, name_of_company, inn);
end//



create procedure all_entity_clients()
begin
		select client.id, client.surname, client.name, client.patronymic, client.phone, entity.name_of_company, entity.inn 
        from client
        inner join entity
        on client.id = entity.cl_id;
end//


create procedure inf_about_entity_client(
										id int
)
begin
		select client.surname, client.name, client.patronymic, client.phone, entity.name_of_company, entity.inn  
        from client
        inner join entity
        on client.id = entity.cl_id
        where client.id = id;
end//


create procedure delete_entity_clients(
										id int
)
begin
		delete client, entity
        from client
        inner join entity
        on client.id = entity.cl_id
        where client.id = id;
end//


create procedure add_stock(
                                        town varchar(24),
                                        street varchar(64),
                                        house int,
                                        frame int,
                                        apartment int,
                                        longitude varchar(20),
                                        latitude varchar(20)
)
begin
    insert into address(address.street, address.house, address.frame, address.apartment, address.longitude, address.latitude, address.town) values (street, house, frame, apartment, longitude, latitude, town);
    select @adr_id := max(id) from address;
    insert into stack(stack.adr_id) values(@adr_id);
end//


create procedure all_stocks()
begin
		select stack.id, address.town, address.street, address.house, address.frame, address.apartment, address.longitude, address.latitude 
        from stack
        inner join address
        on stack.adr_id = address.id;
end//



create procedure inf_about_stock(
										id int
)
begin
		select address.town, address.street, address.house, address.frame, address.apartment, address.longitude, address.latitude
        from stack
        inner join address
        on stack.adr_id = address.id
        where stack.id = id;
end//


create procedure delete_stock(
										id int
)
begin
		delete stack, address
        from stack
        inner join address
        on stack.adr_id = address.id
        where stack.id = id;
end//


create procedure add_material(
								stock_id int,
                                name_of_material varchar(64),
                                quantity int
)
begin
	insert into materials(materials.stack_id, materials.name, materials.quantity)
    values (stock_id, name_of_material, quantity);
end//



create procedure all_materials()
begin
		select materials.id, materials.name, materials.quantity, materials.stack_id, address.town, address.street, address.house, address.frame, address.apartment, address.longitude, address.latitude 
        from materials
        inner join stack
        on materials.stack_id = stack.id
        inner join address
        on stack.adr_id = address.id;
end//




create procedure add_application(

                                        town varchar(24),
                                        street varchar(64),
                                        house int,
                                        frame int,
                                        apartment int,
                                        longitude varchar(20),
                                        latitude varchar(20)
)
begin
	insert into client(client.surname, client.name, client.patronymic, client.phone) values (surname, name, patronymic, phone);
    insert into address(address.street, address.house, address.frame, address.apartment, address.longitude, address.latitude, address.town) values (street, house, frame, apartment, longitude, latitude, town);
    select @cl_id := max(id) from client;
    select @adr_id := max(id) from address;
    insert into phys(phys.cl_id, phys.adr_id) values(@cl_id, @adr_id);
end//


create procedure show_all_employess_in_brigade(
												br_id int
)
begin
	select * from employee where employee.br_id = br_id;
end//
DELIMITER ;



call inf_about_phys_client(1);
call inf_about_operator(1);
call all_phys_clients();
call all_materials();


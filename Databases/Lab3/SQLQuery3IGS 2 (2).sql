use VideoGamesShops
go

-- 1.a)Add a new column named Rating to the table Games
create procedure do_proc_0
as
begin
	alter table Games
	add Rating int
	print 'The procedure do_proc_0 was executed!'
end
go

exec do_proc_0
go

select * from Games
go

-- 1.b)Remove the column Rating from the table Games
create procedure undo_proc_0
as
begin
	alter table Games
	drop column Rating
	print 'The procedure undo_proc_0 was executed!'
end
go

exec undo_proc_0
go

-- 2.a)Add a default constraint to the column Rating in the table Games
create procedure do_proc_1
as
begin
	alter table Games
	add constraint df_Rating default 80 for Rating
	print 'The procedure do_proc_1 was executed!'
end
go

exec do_proc_1
go


-- 2.b)Remove the default constraint from the column Rating in the table Games
create procedure undo_proc_1
as
begin
	alter table Games
	drop constraint df_Rating
	print 'The procedure undo_proc_1 was executed!'
end
go

exec undo_proc_1
go


-- 3.a)Create a new table named Employees
create procedure do_proc_2
as
begin
	create table Employees
	(Eid INT PRIMARY KEY IDENTITY NOT NULL, 
	Name varchar(50) NOT NULL,
	Specialization varchar(50) NOT NULL,
	Vid int)
	print 'The procedure do_proc_2 was executed!'
end
go


exec do_proc_2
go


--3.b)Drom the table named Employees 
create procedure undo_proc_2
as
begin
	drop table Employees
	print'The procedure undo_proc_2 was executed!'
end
go

exec undo_proc_2
go

--4.a)Add a foreign key constraint to the table Employees
create procedure do_proc_3
as
begin
    alter table Employees
    add constraint fk_Employees foreign key (Vid) references VideoGamesCompany(Vid);
    
    print 'The procedure do_proc_3 was executed!';
end
go

exec do_proc_3
go


--4.b)Remove the foreign key constraint of the table Employees
create procedure undo_proc_3
as
begin
	alter table Employees
	drop constraint fk_Employees
	print'The procedure undo_proc_3 was executed!'
end
go

exec undo_proc_3
go

--Creates a table that holds the current version of the database
create table Version(version int)
go

create or alter procedure main
@n int
as
  begin
		declare @v int=(select top 1 version from Version)
		declare @proc varchar(50)
		while @v<@n
		begin
			set @proc=concat('do_proc_',@v)
			print @proc
			set @v =@v+1
			exec @proc
			update Version set version=@v
		end
		while @v>@n
		begin
			set @v =@v-1
			set @proc=concat('undo_proc_',@v)
			print @proc
			exec @proc
			update Version set version=@v
		end
	end
go

exec main 0
exec main 1
exec main 2
exec main 3
exec main 4

select * from Version

insert into Version values(0)
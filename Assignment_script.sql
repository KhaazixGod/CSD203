use Assgmnt
create table Students(
id int primary key,
first_name Nvarchar(50),
last_name Nvarchar(50),
sex varchar,
address Nvarchar(50),
birth Date,
check (sex = 'F'or sex = 'M')
);

create table Courses(
id int primary key,
name Nvarchar(50));

create table Marks(
student_id int,
course_id int,
mark float,
Exam_date Date,
time time,
foreign key (student_id) references Students(id),
foreign key (course_id) references Courses(id)
);

create table Professors(
id int primary key,
first_name Nvarchar(50),
last_name Nvarchar(50),
sex varchar,
address Nvarchar(50),
birth Date,
course_id int,
check (sex = 'F'or sex = 'M'),
foreign key (course_id) references Courses(id));

-- In điểm toàn bộ điểm của sinh viên
select s.id,s.last_name+' '+s.first_name as Fullname,c.name as Course ,m.mark,p.last_name+' '+p.first_name as Professor_name from Marks m join Students s 
on m.student_id = s.id 
join Courses c
on m.course_id = c.id
left join Professors p 
on m.course_id = p.course_id;

-- Tính điểm trung bình của toàn bộ sinh viên
select m.student_id as Student_id,s.last_name+' '+s.first_name as Fullname,sum(m.mark)/4 from 
Students s join Marks m
on s.id = m.student_id
group by m.student_id,s.id,s.last_name,s.first_name;

-- Đếm số lượng sinh viên mỗi môn học
select c.name as Course_name, COUNT(m.student_id) Number_Of_Students from Courses c join Marks m on c.id = m.course_id
group by c.name;

-- In ra sinh viên có điểm cao nhất của từng môn học
select m.course_id as Course_id,max(m.mark) as Highest_mark from Marks m inner join Students s on m.student_id = s.id group by m.course_id;

-- Xoá sinh viên có ID 1 đã ra trường
delete from Students where id = 1;
delete from Marks where student_id = 1;

-- Xoá giáo viên có ID 1 đã rời trường
delete from Professors where id = 1;

-- Sửa điểm của sinh viên theo ID và mã môn
update Marks 
set mark = 8
where student_id = 1 and course_id = 1;



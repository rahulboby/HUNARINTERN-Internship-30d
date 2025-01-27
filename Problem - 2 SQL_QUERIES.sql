create database HunarIntern; /*Creating new database*/
use hunarintern; /*Using this data base for tables*/

/* --- Creating Student Table --- */
create table student (
	RollNo int primary key,
    Student_name varchar(25),
    Marks float(6,2),
    Aadhar char(12) unique,
    Address varchar(150)
);

/* --- Creating course Table --- */
create table course (
	RollNo int,
    Course varchar(20),
    course_duration varchar(10),
    foreign key (rollno) references student(rollno)
);

/* --- Some queries --- */
Select avg(marks) as average_marks from student; /*To Extract average marks*/
Select Student_name from student order by Student_name; /*To display names in ascending order*/
Select Rollno from student where marks<30; /*Get roll numbers of students scoring below 30*/
Select Rollno from student where student_name like "r%"; /*Rollno of Names starting with R*/
Select student.Rollno from student left join course on student.rollno = course.rollno where course = "BCA";

/* --- Teesting with SAMPLE DATA --- */

insert into student (rollno, student_name, marks, aadhar) values 
	(7, "Rakesh", 47, "098765432109"),
	(1, "Rahul", 83, "123456789012"),
    (2, "Rishi", 94, "567890123456"),
    (3, "Amika", 92, "432109876543"),
    (4, "Rohit", 56, "456723109876"),
    (5, "Lary", 29, "887766554410"),
    (6, "Brad", "12", "120934875609");
    
insert into course values
	(1, "B.Tech", "4 Years"),
    (2, "BBA", "3 Years"),
    (3, "BSc", "3 Years"),
    (4, "BE", "4 Years");
    (5, "B.Tech", "4 Years"),
    (6, "B.Tech", "4 Years"),
    (7, "BCA", "3 Years");
    
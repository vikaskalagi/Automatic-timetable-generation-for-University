<?php
session_start();
#$connect_str = "dbname='timetable' user='postgres' host='localhost' password='vskalagi'";
#$my=new PDO("pgsql:host=localhost;dbname=timetable","postgres","vskalagi");
$connect_str =pg_connect( "dbname='timetable' user='postgres' host='localhost' password='vskalagi'");
#$sql="SELECT schedule FROM teacher where id=1";
# $result=pg_query($connect_str,$sql);
  #echo "no".pg_num_rows($result);
# while ($row=pg_fetch_row($result)) {var_dump($row);}
if(isset($_POST['submit2']))
  {//echo "jj";
#echo isset($_POST['submit2']);
  $p=$_SESSION['id'];
   $sql="SELECT * FROM takes where instructor_id='$p'";
 $result=pg_query($connect_str,$sql);
$ex=1;
  while ($row=pg_fetch_row($result)) {
    #$ex=json_encode(array($row[0],$row[1],$row[3]));
    $sub=$_POST[$ex];
    $query="update takes set instructor_id='$sub' where year='$row[0]' and section='$row[1]' and course_id='$row[3]'; ";
    #+echo $q;
    $ex++;
    $rw=pg_query($query);

  }
$query="delete from teacher where id=$p";
    #+echo $q;
    $rw=pg_query($query);
 #  $t=$_POST['a'];
#echo "$t";
$sql="SELECT id,hours FROM course ";
 $result=pg_query($connect_str,$sql);
 while ($row=pg_fetch_row($result)) {
$query="UPDATE takes set hour='$row[1]' where  course_id='$row[0]'; ";
  $rw=pg_query($query);
 }
$arr=['empty','empty','empty','empty','empty','empty'];
$w=json_encode([$arr,$arr,$arr,$arr,$arr]);
$query="UPDATE teacher set schedule='$w'; ";
$rw=pg_query($query);
$query="UPDATE section set schedule='$w'; ";
$rw=pg_query($query);

#echo "<script>alert('please run code to get timetable updated'); window.location.replace('delete.php');</script>";
}
?>

<!DOCTYPE html>
<html>
<head>
<style>
  .button{
    border-radius: 10px;
  background-color: orange;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;

}
body {
  background-image:linear-gradient(rgba(0,0,0,0.1),rgba(0,0,0,0.1)),url("core_multimedia_package1.jpeg") ;
  background-size: 100%;
}
input[type=text],[type = date],[type = number],[type = email]{
    width: 350px;
    padding: 15px;
    margin: 5px 0 22px 0;
    display: inline-block;
    border: none;
    background: #f1f1f1;
}
select{
    width: 300px;
    padding: 15px;
    margin: 5px 0 22px 0;
    display: inline-block;
    border: none;
    background: #f1f1f1;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}
tr:hover {background-color: #f5f5f5;}

body{
  font-family: BOOK ANTIQUA;
}
li {
  float: left;
}
table {
  width: 80%;
}

th {
  height: 50px;
}
tr:nth-child(even) {background-color: #f2f2f2;}
th, td {
  padding: 15px;
  text-align: left;
  vertical-align: top;
}
th {
  background-color: #4CAF50;
  color: white;
}
a{
  font-size: 20px;
  color: black
}

li a {

  font-size: 18px;
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  transition-duration: 0.4s;
}

/* Change the link color to #111 (black) on hover */
li a:hover {

  background-color: #111;
}

</style>
</head>
<body>
  <header><p align="center" style="font-size: 40PX">PES UNIVERSITY </p>
</header>
<section>
  <nav>
  <ul>
<li id=1><a href="insert.php">INSERT TEACHER</a></li><br>
<li id=2><a href="year_choice.php">ALLOCATE TEACHER TO SECTION</a></li><br>
<li id=6><a href="year_choice.php">BLOCK PERIODS</a></li><br>

  <li id=3><a href="delete.php">REMOVE TEACHER</a></li><br>
  <li id=4><a href="final_rama.php">TIMETABLE</a></li><br>
  <li id=5><a href="teacher_kri.php">TEACHER SCHEDULE</a></li><br>
    <li id=6><a href="two_hour.php">BLOCK HOURS</a></li><br>

</ul>
</nav>
</section>
<article>
<?php
#$connect_str = "dbname='timetable' user='postgres' host='localhost' password='vskalagi'";
#$my=new PDO("pgsql:host=localhost;dbname=timetable","postgres","vskalagi");
#$connect_str =pg_connect( "dbname='timetable' user='postgres' host='localhost' password='vskalagi'");
#$sql="SELECT schedule FROM teacher where id=1";
#	$result=pg_query($connect_str,$sql);
	#echo "no".pg_num_rows($result);
#	while ($row=pg_fetch_row($result)) {var_dump($row);}
if(isset($_POST['submit1']))
  {//echo "jj";
	$p=$_POST["id"];
  $_SESSION['id']=$p;
    $sql="SELECT * FROM takes where instructor_id=$p";
    echo "<p>enter the substitute teacher for these section and course</p>";
  $result=pg_query($connect_str,$sql);
    #echo "no".pg_num_rows($result);
  echo "<form action='' method='post'>" ;
   $num=1;
   while ($row=pg_fetch_row($result)) {
    echo "year=$row[0] section=$row[1] course_id=$row[3] ";
    #$ex=json_encode(array($row[0],$row[1],$row[3]));
    #echo $ex;

    echo "instuctor_id:<label><td><input type='number'  name=$num value='' required></td></label>";
    $num++;
    echo "<br>";
echo "<br>";

   }
   echo "<br><center><button type='submit' value='submit2' name='submit2' class='button' >SUBMIT</button></center>";
   echo"<form>";
}
?>

</article>
<script type="text/javascript">
  
    var d = document.querySelectorAll('li');
        d[1].addEventListener("click",fu,false);
d[2].addEventListener("click",fu,false);

/*    
    for(var i = 0, len = d.length; i < len;i+=1){
    d[i].addEventListener("click",fu,false);

    //divE1[i].id=divE1[i].text;
    //divE1[i+1].id=i;
    //divE1[i+2].id=i;
    
    //divE1[1].addEventListener("click",func,false);
  }*/
  function fu(e)
  {//alert(e.currentTarget.id);
    //alert(e.currentTarget.id);
    document.cookie="select="+e.currentTarget.id;


    }

</script>
</body>
</html>
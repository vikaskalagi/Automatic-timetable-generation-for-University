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
   $sql="SELECT * FROM takes where instructor_id=$p";
 $result=pg_query($connect_str,$sql);
$eq=$_POST['["1","a","1"]'];
echo $eq;
  while ($row=pg_fetch_row($result)) {
    $ex=json_encode(array($row[0],$row[1],$row[3]));
    $sub=$_POST[$ex];
    $query="update takes set instuctor_id=$sub where year=$row[0] and section=$row[1] and course_id=$row[3]; ";
    #+echo $q;
    $rw=pg_query($query);

  }
$query="delete from teacher where id=$p";
    #+echo $q;
    $rw=pg_query($query);
 #  $t=$_POST['a'];
#echo "$t";
}
?>
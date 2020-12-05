<?php
 session_start();
#$connect_str = "dbname='timetable' user='postgres' host='localhost' password='vskalagi'";
#$my=new PDO("pgsql:host=localhost;dbname=timetable","postgres","vskalagi");
$connect_str =pg_connect( "dbname='timetable' user='postgres' host='localhost' password='vskalagi'");
#$sql="SELECT schedule FROM teacher where id=1";
# $result=pg_query($connect_str,$sql);
  #echo "no".pg_num_rows($result);
# while ($row=pg_fetch_row($result)) {var_dump($row);}
#print_r( "isset($_POST['submit_all'])");
if(isset($_POST['submit_all']))
  {#echo "jj";
    $year=$_COOKIE['year'];
  $section=$_COOKIE['section'];
      $sql="SELECT * FROM course where year=$year ORDER BY id ASC";
  $result=pg_query($connect_str,$sql);
    $cou=0;
        while($row=pg_fetch_row($result))
        {
          $value=$_POST["$cou"];
          $cou++;
          if($value){
            #echo "sdf";
          $just="SELECT * FROM takes where year='$year' and section='$section' and  course_id='$row[0]'";
          $r=pg_query($connect_str,$just);
            if($ro=pg_fetch_row($r))
          {
            #var_dump($ro);
            #echo "dskd<br>$ro[2]";
            $inter="UPDATE takes SET instructor_id='$value' where year='$year' and section='$section' and course_id=$row[0] ;";  
          }
          else{
            #echo "dskd";
            
          $inter="insert into takes values ('$year','$section','$value','$row[0]','$row[2]'); ";
          }
            $re=pg_query($inter);
}
#echo "string";
    }

    
}
?>
</html>
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
   # session_start();
   /* $aid=$_SESSION['username'];
    include('init.php');
    if (!$conn) 
      die("Connection failed: " . mysqli_connect_error());
    
    $findid = "SELECT * FROM Warden WHERE Email = '$aid'";
    $findidres = mysqli_query($conn,$findid);

    if(mysqli_num_rows($findidres) == 1)
    {
      $rows = mysqli_fetch_assoc($findidres);
    } */
?>    
  <!--<h3 style="font-size: 30px;font-family: garamond;color: grey;padding-left: 300px">Complaints to <?php echo $rows['Wname'];?></h3>-->

  <div style="padding-left: 20px">

  <center><table border="" cellpadding="2" cellspacing="0">
<thead>

</thead>
<tbody>

   <form action="" method="post">
  <?php
  $connect_str =pg_connect( "dbname='timetable' user='postgres' host='localhost' password='vskalagi'");
  $year=$_COOKIE['year'];
  $section=$_COOKIE['section'];
  #echo "$section";
  ECHO "<h1>ENTER THE TEACHER ID FOR YEAR: $year SECTION: $section </h1>";
   $sql="SELECT * FROM course where year=$year ORDER BY id ASC";
  $result=pg_query($connect_str,$sql);
    $cou=0;
        while($row=pg_fetch_row($result))
        {
          ?>

         <tr>
        <td> 
          courese_id:<?php echo  $row[0]; ?> &nbsp; &nbsp;
          course_name:<?php echo  $row[1]; ?> &nbsp; &nbsp;
          teacher id:
          <label><input type='text'  name='<?php echo $cou;?>' value='' ></td></label> 

         </tr>
          

          <?php 
          $cou++;
        }
     ?>

</tbody>

</table>
 <br><center><button type="submit" value="submit_all" name="submit_all" class="button" >SUBMIT</button></center>
</form>
</center>
</div>
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

<?php
    $com=escapeshellcmd('python F:\__pycache__\xampp\htdocs\timetable\delet.py');
    $out=shell_exec($com);
    echo $out;
   # echo "asd";

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
<CENTER><h1>REPLACE  TEACHER</h1></CENTER>
<form action="edit_update.php" method="post">
<CENTER>id:<label><td><input type='number'  name='id' value='' ></td></label></CENTER>	
<br><center><button type="submit" value="submit1" name="submit1" class="button" >SUBMIT</button></center>
</form>
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
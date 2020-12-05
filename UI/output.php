<!DOCTYPE html>
<html>
<head>
	<title>timetable</title>
</head>
<body>

<?php
#$connect_str = "dbname='timetable' user='postgres' host='localhost' password='vskalagi'";
#$my=new PDO("pgsql:host=localhost;dbname=timetable","postgres","vskalagi");
$connect_str =pg_connect( "dbname='timetable' user='postgres' host='localhost' password='vskalagi'");

#$s=pg_connect("dbname=timetable");

$sql="SELECT * FROM teacher"; 
#$results=mysqli_query($connect_str,$sql);
#$q="select * from section";
$result=pg_query($connect_str,$sql);
echo "no".pg_num_rows($result);
while ($row=pg_fetch_row($result)) {
	# code...
	echo $row[1];
	$myu=json_decode($row[2]);
	echo($myu[0][0]=='empty');
	if($myu[0][0]!='empty')
	{
		$r=json_decode($myu[0][0]);
		echo $r[0];
		echo $myu[0][0];
	}
	echo($myu[0][0]);
	#var_dump($myu[0][0]);
	echo "<br>\n";
}
echo $result;
#pg_free_result($result);
#pg_close($s);
?>


</body>
</html>

<?php
	//$dbhost = "localhost";
	//$dbuser = "root";
	//$dbpass = "MrMeet";
	//$dbname = "MrMeet";

  $dbhost = "db4free.net";
	$dbuser = "mrmeet";
	$dbpass = "ccleonliew";
	$dbname = "mrmeet";


	if(!$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname)) 
	{
		die("failed to connect!");
	}

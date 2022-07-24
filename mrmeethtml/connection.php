<?php
	//$dbhost = "localhost";
	//$dbuser = "root";
	//$dbpass = "MrMeet";
	//$dbname = "MrMeet";

	//$dbhost = "remotemysql.com";
	//$dbuser = "g4gIqpoa8A";
	//$dbpass = "V2sTQ01WsK";
	//$dbname = "g4gIqpoa8A";

  $dbhost = "db4free.net";
	$dbuser = "mrmeet";
	$dbpass = "ccleonliew";
	$dbname = "mrmeet";
  

	if(!$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname)) 
	{
		die("failed to connect!");
	}

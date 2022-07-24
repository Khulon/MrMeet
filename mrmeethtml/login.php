<?php
session_start();

	include("connection.php");
	include("function.php");

	$_SESSION['ErrorMsg'] = 0;

	if($_SERVER['REQUEST_METHOD'] == "POST")
	{
		$user_name = $_POST['myusername'];
		$password = $_POST['mypassword'];

		//read from database
		if(!empty($user_name) && !empty($password))
		{

			$query = "select * from chat where chat_id = '$user_name' limit 1";
			$result = mysqli_query($con, $query);

			if ($result)
			{
				if($result && mysqli_num_rows($result) > 0)
				{
					$user_data = mysqli_fetch_assoc($result);

					if($user_data['pass'] === $password)
					{
						$_SESSION['user_id'] = $user_data['chat_id'];
						header("Location: index.php");
						die;
					}else
					{
						$_SESSION['ErrorMsg'] = 1;
					}
				}else
				{
					$_SESSION['ErrorMsg'] = 2;
				}
			}

		}else
		{
			$_SESSION['ErrorMsg'] = 2;
		}
	}


?>

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8" />
	<meta http-equiv="X-UA-Compatble" content="IE=edge,chrome=1">
	<meta name="robots" content="index,follow">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    

	<title>MrMeet!</title>

	<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400&display=swap" rel="stylesheet">
	<link href="StylesLogin.css" rel="stylesheet" type="text/css">


</head>
<body style="background-color: #FAFAF4; margin: 0;">
 


	<header>

		<div style="display: flex; justify-content: center; align-items: center;">

			<a href= "http://t.me/MrMeetBot"><img src="images/logo.png" width="200" height="270"></a>

		</div>

	</header>




	<div style="display: flex; justify-content: center; align-items: center;">

		<h1 id="home">Hurry up and log in lah!</h1>

	</div>




	<form action="login.php" method="POST">


		<p style="color:  grey" id="ChatID"><font size="4">Chat ID:</font></p>

		<input type="text" class="large-fld" name="myusername" value="" placeholder="123456789">





			
		<p style="color:  grey;" id="Password"><font size="4">Password:</font></p>

		<input type="password" class="large-fld" name="mypassword" value="" placeholder="Password">


		<p> 
		<div style="color:  #DE5F4C;" class="ErrorMsg"><font size="3">

			<?php 
			if (($_SESSION['ErrorMsg']) == 1){ ?>
					<b>Wrong Password</b>
			<?php } 
			if (($_SESSION['ErrorMsg']) == 2){ ?>
					<b>Invalid Chat ID</b>
			<?php } ?>

		</div>
		</p>


		<input type="submit" class="login-btn" style="color: white;" name="login" value="Login">




		<p style="color: black;" id="HomeInfo">Click on <span><b>/Webapp</b></span> in telegram to get your <span><b>Chat ID</b></span> and <span><b>Password!</b></span></p>

	</form>



	

</body>
</html>
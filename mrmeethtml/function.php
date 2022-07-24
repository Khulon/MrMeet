<?php

function check_login($con)
{
	if(isset($_SESSION['user_id']))
	{
		$id = $_SESSION['user_id'];
		$query = "select * from chat where chat_id = '$id' limit 1";

		$result = mysqli_query($con, $query);
		if($result && mysqli_num_rows($result) > 0)
		{
			$user_data = mysqli_fetch_assoc($result);
			return $user_data;
		}
	}

	//redirect to login
	header("location:login.php");
	die;

}

function update($name, $id, $con, $type) 
{
  if(isset($_POST[$name]))
  {
    if ($type == 'date') {
      $recieve = substr($_POST[$name], -7, -5);
      $recieve .= substr($_POST[$name], -10, -8);
      $recieve .= substr($_POST[$name], -2);
    }
    else 
    {
      $recieve = $_POST[$name];
    }
    
    if($recieve != ($user_data[$name]))
    {
      $query = "UPDATE chat SET $name = '$recieve' WHERE chat_id = $id";
      mysqli_query($con, $query);
    }
  }
}


function dateget($date)
{
  $day = substr($date, -6, -4);
  $month = substr($date, -4, -2);
  $year = substr($date, -2);
  return $month.'/'.$day.'/20'.$year;
}


function AddMilestone($name, $date, $con, $id, $user_data, $ObjectiveNo)
{
  if(isset($_POST[$name]) && isset($_POST[$date]))
  {
    $MilestoneNo = 1;
    $DataName = 'MyObjective'.$ObjectiveNo.'Milestones'.$MilestoneNo;
    while ((isset($user_data[$DataName])) && $MilestoneNo <=4)
    {
      $MilestoneNo += 1;
      $DataName = 'MyObjective'.$ObjectiveNo.'Milestones'.$MilestoneNo;
    }

    $query = "UPDATE chat SET $DataName = '$_POST[$name]' WHERE chat_id = $id";
    mysqli_query($con, $query);

    $DataDate = 'MyObjective'.$ObjectiveNo.'MilestoneDates'.$MilestoneNo;
    $recieve = substr($_POST[$date], -7, -5);
    $recieve .= substr($_POST[$date], -10, -8);
    $recieve .= substr($_POST[$date], -2);
    $query = "UPDATE chat SET $DataDate = '$recieve' WHERE chat_id = $id";
    mysqli_query($con, $query);

    $DataStatus = 'MyObjective'.$ObjectiveNo.'MilestoneStatus'.$MilestoneNo;
    $query = "UPDATE chat SET $DataStatus = 'Pending' WHERE chat_id = $id";
    mysqli_query($con, $query);

    $name = 'NewObjectives'.$ObjectiveNo.'MilestoneNo';
    $query = "UPDATE chat SET $name = $name + 1 WHERE chat_id = $id";
    mysqli_query($con, $query);
  }
}

function AddObjective($con, $id, $user_data)
{
  if(isset($_POST['NewObjectiveName']) && isset($_POST['NewObjectiveDate']))
  {
    $ObjectiveNo = 1;
    $DataName = 'MyObjectives'.$ObjectiveNo;
    while ((isset($user_data[$DataName])) && $ObjectiveNo <=2)
    {
      $ObjectiveNo += 1;
      $DataName = 'MyObjectives'.$ObjectiveNo;
    }

    $name = $_POST['NewObjectiveName'];
    $query = "UPDATE chat SET $DataName = '$name' WHERE chat_id = $id";
    mysqli_query($con, $query);

    $DataDate = 'MyObjectivesDate'.$ObjectiveNo;
    $recieve = substr($_POST['NewObjectiveDate'], -7, -5);
    $recieve .= substr($_POST['NewObjectiveDate'], -10, -8);
    $recieve .= substr($_POST['NewObjectiveDate'], -2);
    $query = "UPDATE chat SET $DataDate = '$recieve' WHERE chat_id = $id";
    mysqli_query($con, $query);

    $name = 'NewObjectivesNo';
    $query = "UPDATE chat SET $name = $name + 1 WHERE chat_id = $id";
    mysqli_query($con, $query);
  }
}
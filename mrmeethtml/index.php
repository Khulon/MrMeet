<?php
session_start();

include("connection.php");
include("function.php");

$user_data = check_login($con);


if($_SERVER['REQUEST_METHOD'] == "POST")
	{
    $id = $_SESSION['user_id'];
    for ($ObjectiveNo = 0; $ObjectiveNo <= 3; $ObjectiveNo += 1)
    {
      if ($ObjectiveNo == 0)
      {
        AddObjective($con, $id, $user_data);
        
      } else {
        $date = 'NewObjective'.$ObjectiveNo.'MilestoneDate';
        $name = 'NewObjective'.$ObjectiveNo.'MilestoneName';
        AddMilestone($name, $date, $con, $id, $user_data, $ObjectiveNo);
      }
    }


    for ($ObjectiveNo = 1; $ObjectiveNo <= 3; $ObjectiveNo += 1) 
    {
      $name = 'MyObjectives';
      $name .= (string)$ObjectiveNo;
      update($name, $id, $con, 'other');

      $name = 'MyObjectivesDate';
      $name .= (string)$ObjectiveNo;
      update($name, $id, $con, 'date');
      
      for ($MilestoneNo = 1; $MilestoneNo <= 5; $MilestoneNo+=1) 
      {
        $name = 'MyObjective';
        $name .= (string)$ObjectiveNo;
        $name .= 'Milestones';
        $name .= (string)$MilestoneNo;
        update($name, $id, $con, 'other');

        $name = 'MyObjective';
        $name .= (string)$ObjectiveNo;
        $name .= 'MilestoneDates';
        $name .= (string)$MilestoneNo;
        update($name, $id, $con, 'date');

        $name = 'MyObjective';
        $name .= (string)$ObjectiveNo;
        $name .= 'MilestoneStatus';
        $name .= (string)$MilestoneNo;
        update($name, $id, $con, 'other');
      }
    }
    header("Location: index.php?status=1");
  }

?> 

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
	<meta http-equiv="X-UA-Compatble" content="IE=edge,chrome=1">
	<meta name="robots" content="index,follow">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>




<link rel="stylesheet" href="//code.jquery.com/ui/1.13.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
  <script src="https://code.jquery.com/ui/1.13.1/jquery-ui.js"></script>
  <script>
  $( function() {

    $( "#NewObjectiveDate" ).datepicker();
    $( "#NewObjective1MilestoneDate" ).datepicker();
    $( "#NewObjective2MilestoneDate" ).datepicker();
    $( "#NewObjective3MilestoneDate" ).datepicker();
    $( "#MyObjectivesDate1" ).datepicker();
    $( "#MyObjectivesDate2" ).datepicker();
    $( "#MyObjectivesDate3" ).datepicker();
    $( "#MyObjective1MilestoneDates1" ).datepicker();
    $( "#MyObjective1MilestoneDates2" ).datepicker();
    $( "#MyObjective1MilestoneDates3" ).datepicker();
    $( "#MyObjective1MilestoneDates4" ).datepicker();
    $( "#MyObjective1MilestoneDates5" ).datepicker();
    $( "#MyObjective2MilestoneDates1" ).datepicker();
    $( "#MyObjective2MilestoneDates2" ).datepicker();
    $( "#MyObjective2MilestoneDates3" ).datepicker();
    $( "#MyObjective2MilestoneDates4" ).datepicker();
    $( "#MyObjective2MilestoneDates5" ).datepicker();
    $( "#MyObjective3MilestoneDates1" ).datepicker();
    $( "#MyObjective3MilestoneDates2" ).datepicker();
    $( "#MyObjective3MilestoneDates3" ).datepicker();
    $( "#MyObjective3MilestoneDates4" ).datepicker();
    $( "#MyObjective3MilestoneDates5" ).datepicker();

    
  } );
  </script>
  
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400&display=swap" rel="stylesheet">
  <link href="StylesIndex.css" rel="stylesheet" type="text/css">
  <script src="index.js"></script>
  


  <title>
    hello, <?php echo $user_data['chat_id']; ?>
  </title>
  
</head>

<body style="background-color: #FAFAF4; margin: 0; ">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <div class="topnav">
    <a class="active" href="#home">Dashboard</a>
    <a href="./src/meetings.php"> Meetings</a>
    <a href="logout.php"> Logout</a>
    <a href="javascript:void(0);" class="icon" onclick="myFunction()">
      <i class="fa fa-bars"></i>
    </a>
  </div>

  <br>
  <header style="display: flex; justify-content: center; align-items: center;">
    <p><font size="5">
      <a href= "http://t.me/MrMeetBot"><img src="images/logo.png" width="200" height="240" ></a>
    </div>
    <br>
  </p>
</header>

<br>




<br>


<div style="display: flex; justify-content: center; align-items: center;">
  <div class="box" style="border-radius: 50px; background: beige;"><div class="in-box">
    <div style="display: flex; justify-content: center; align-items: center;">
      <h2>My Objectives</h2>
      
    </div>

    <div class="container">
      
      <?php 
      $variable = 0;
      if ($user_data['MyObjectives1'] != '') {
        echo '<div class="obj">';
        echo '<button style="color: white;" class="objective-btn" onclick="toggleObjective(1)">';  
        echo $user_data['MyObjectives1']; 
        echo '</button></div>';
      }

      if ($user_data['MyObjectives2'] != '') {
        echo '<div class="obj">';
        echo '<button style="color: white;" class="objective-btn" onclick="toggleObjective(2)">'; 
        echo $user_data['MyObjectives2'];
        echo '</button></div>';
      }

      if ($user_data['MyObjectives3'] != '') {
        echo '<div class="obj">';
        echo '<button style="color: white;" class="objective-btn" onclick="toggleObjective(3)">'; 
        echo $user_data['MyObjectives3'];
        echo '</button></div>';
        $variable = 1;
      } 

      if ($variable == 0) {
        echo '<div class="obj">';
        echo '<button style="color: white;" class="add-btn" onclick="toggleAddObjectives()">+</button>';
        echo '</div>';
      }
      
      
      ?>

    </div>
    
    <br>
    
  </div></div></div>

  <div class="popup" id="popup-AddObjectives">
    <div class="overlay"></div>
    <div class = "content">
      <div class="close-btn" onclick="toggleAddObjectives()">&times;</div>
      
      <form action="index.php" method="POST" class="form">
          <div class="MilestoneBox">
            <div style="display: flex; justify-content: center; align-items: center;">
              <label>Add Objective</label>
            </div>
            <br>
            <div style="display: inline-flex; float: right;">
              <label>Name:</label>
              <input type="text" id="NewObjectiveName" class="MilestoneInput" name="NewObjectiveName" value="" placeholder="MyObjective">
            </div>
            <br>
            <div style="display: inline-flex; float: right;">
              <label>Due: </label>
             <input type="text" id="NewObjectiveDate" class="MilestoneInput" name="NewObjectiveDate" value="" placeholder="06/30/23">
            </div>
            <br><br>
            <div style="display: inline-flex; justify-content: center; align-items: center;">
              <button id="SaveNewObjective" style="color:white; background-color: #C95746;" class="add-btn">Save</button>
            </div>
          </div>
      </form>
      
    </div>
  </div>

      

  <br><br>








      
  

  <div id="popup-Objective1" style="display: none">
    <div style="display: flex; justify-content: center; align-items: center;">
  <div class="box" style="border-radius: 50px; background: beige;"><div class="in-box">
    <div style="display: flex; justify-content: center; align-items:">
      <h2>My Milestones for</h2>
    </div>

    <form action="index.php" method="POST" class="form">
      <div style="display: flex; justify-content: center; align-items: center;">
        <input type="text" id="MyObjectives1" class="MilestoneInput" name="MyObjectives1" disabled value=" <?php echo $user_data['MyObjectives1']; ?> ">
      </div>
      <div style="display: flex; justify-content: center; align-items: center;">
        <input type="text" id="MyObjectivesDate1" class="MilestoneInput" name="MyObjectivesDate1" disabled value=" <?php echo dateget($user_data['MyObjectivesDate1']); ?> ">
      </div>
      <br>
      
      <div class="container" style="grid-gap: 20px 130px;">
    
      
      <?php 
      $Objective1variable = 0;
      if ($user_data['MyObjective1Milestones1'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 1</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective1MilestoneDates1" class="MilestoneInput" name="MyObjective1MilestoneDates1" disabled value="';
        echo dateget($user_data['MyObjective1MilestoneDates1']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective1Milestones1" class="MilestoneInput" name="MyObjective1Milestones1" disabled value="';
        echo $user_data['MyObjective1Milestones1']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective1MilestoneStatus1" class="MilestoneInput" name="MyObjective1MilestoneStatus1">';
        if (($user_data['MyObjective1MilestoneStatus1']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
        $Objective1variable = 1;
      }

      if ($user_data['MyObjective1Milestones2'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 2</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective1MilestoneDates2" class="MilestoneInput" name="MyObjective1MilestoneDates2" disabled value="';
        echo dateget($user_data['MyObjective1MilestoneDates2']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective1Milestones2" class="MilestoneInput" name="MyObjective1Milestones2" disabled value="';
        echo $user_data['MyObjective1Milestones2']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective1MilestoneStatus2" class="MilestoneInput" name="MyObjective1MilestoneStatus2">';
        if (($user_data['MyObjective1MilestoneStatus2']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective1Milestones3'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 3</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective1MilestoneDates3" class="MilestoneInput" name="MyObjective1MilestoneDates3" disabled value="';
        echo dateget($user_data['MyObjective1MilestoneDates3']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective1Milestones3" class="MilestoneInput" name="MyObjective1Milestones3" disabled value="';
        echo $user_data['MyObjective1Milestones3']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective1MilestoneStatus3" class="MilestoneInput" name="MyObjective1MilestoneStatus3">';
        if (($user_data['MyObjective1MilestoneStatus3']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective1Milestones4'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 4</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective1MilestoneDates4" class="MilestoneInput" name="MyObjective1MilestoneDates4" disabled value="';
        echo dateget($user_data['MyObjective1MilestoneDates4']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective1Milestones4" class="MilestoneInput" name="MyObjective1Milestones4" disabled value="';
        echo $user_data['MyObjective1Milestones4']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective1MilestoneStatus4" class="MilestoneInput" name="MyObjective1MilestoneStatus4">';
        if (($user_data['MyObjective1MilestoneStatus4']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective1Milestones5'] != '') {
        $Objective1variable = 2;
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 5</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective1MilestoneDates5" class="MilestoneInput" name="MyObjective1MilestoneDates5" disabled value="';
        echo dateget($user_data['MyObjective1MilestoneDates5']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective1Milestones5" class="MilestoneInput" name="MyObjective1Milestones5" disabled value="';
        echo $user_data['MyObjective1Milestones5']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective1MilestoneStatus5" class="MilestoneInput" name="MyObjective1MilestoneStatus5">';
        if (($user_data['MyObjective1MilestoneStatus5']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }
      ?>
      </div>
      <br>
      <div style="display: flex; justify-content: center; align-items: center;">
        <button id="save1" disabled style="color:white; background-color: #C95746;" class="add-btn">Save</button>
      </div>
    
      </form>
      <br>

      <div class="container" style="grid-gap: 20px 20px;">
    
      <?php
      if ($Objective1variable != 2) {
        echo '<div class="add">';
        echo '<button style="color: white;" class="add-btn" onclick="toggleAddMilestonesObjective1()">+</button>';
        echo '</div>';
      }
      ?>

      <?php

        echo '<div id="edit1">';
        echo '<button id="edit1" style="color:white; background-color: #DE5F4C;" class="add-btn" onclick="toggleEditMilestonesObjective1()">Edit</button>';
        echo '</div>';
        echo '<div id="cancel1" style="display: none;">';
        echo '<button id=cancel1 style="color:white; background-color: #DE5F4C;" class="add-btn" onclick="toggleCancelMilestonesObjective1()">Cancel</button>';
        echo '</div>';
      
      ?>
      </div></div></div></div></div>




        
      <div class="popup" id="popup-AddMilestonesObjective1">
        <div class="overlay"></div>
          <div class = "content">
          <div class="close-btn" onclick="toggleAddMilestonesObjective1()">&times;</div>

          <form action="index.php" method="POST" class="form">
          <div class="MilestoneBox">
            <div style="display: flex; justify-content: center; align-items: center;">
              <label>Add Milestone</label>
            </div>
            <div style="display: inline-flex; float: right;">
              <label>Name:</label>
              <input type="text" id="NewObjective1MilestoneName" class="MilestoneInput" name="NewObjective1MilestoneName" value="" placeholder="MyMilestone">
            </div>
            <br>
            <div style="display: inline-flex; float: right;">
              <label>Due: </label>
             <input type="text" id="NewObjective1MilestoneDate" class="MilestoneInput" name="NewObjective1MilestoneDate" value="" placeholder="06/30/23">
            </div>
            <br>
            <div style="display: inline-flex; float: right;">
              <label>Status: </label>
             <input type="text" id="NewObjective1MilestoneStatus" class="MilestoneInput" name="NewObjective1MilestoneStatus" disabled value="Pending">
            </div>
            <br><br>
            <div style="display: inline-flex; justify-content: center; align-items: center;">
              <button id="SaveNewMilestone" style="color:white; background-color: #C95746;" class="add-btn">Save</button>
            </div>
            

          </div>
          </form>
            <br>
        </div>
      </div>

      



















<div id="popup-Objective2" style="display: none">
    <div style="display: flex; justify-content: center; align-items: center;">
  <div class="box" style="border-radius: 50px; background: beige;"><div class="in-box">
    <div style="display: flex; justify-content: center; align-items:">
      <h2>My Milestones for</h2>
    </div>

    <form action="index.php" method="POST" class="form">
      <div style="display: flex; justify-content: center; align-items: center;">
        <input type="text" id="MyObjectives2" class="MilestoneInput" name="MyObjectives2" disabled value=" <?php echo $user_data['MyObjectives2']; ?> ">
      </div>
      <div style="display: flex; justify-content: center; align-items: center;">
        <input type="text" id="MyObjectivesDate2" class="MilestoneInput" name="MyObjectivesDate2" disabled value=" <?php echo dateget($user_data['MyObjectivesDate2']); ?> ">
      </div>
      <br>
      
      <div class="container" style="grid-gap: 20px 130px;">
    
      
      <?php 
      $Objective2variable = 0;
      if ($user_data['MyObjective2Milestones1'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 1</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective2MilestoneDates1" class="MilestoneInput" name="MyObjective2MilestoneDates1" disabled value="';
        echo dateget($user_data['MyObjective2MilestoneDates1']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective2Milestones1" class="MilestoneInput" name="MyObjective2Milestones1" disabled value="';
        echo $user_data['MyObjective2Milestones1']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective2MilestoneStatus1" class="MilestoneInput" name="MyObjective2MilestoneStatus1">';
        if (($user_data['MyObjective2MilestoneStatus1']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
        $Objective2variable = 1;
      }

      if ($user_data['MyObjective2Milestones2'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 2</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective2MilestoneDates2" class="MilestoneInput" name="MyObjective2MilestoneDates2" disabled value="';
        echo dateget($user_data['MyObjective2MilestoneDates2']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective2Milestones2" class="MilestoneInput" name="MyObjective2Milestones2" disabled value="';
        echo $user_data['MyObjective2Milestones2']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective2MilestoneStatus2" class="MilestoneInput" name="MyObjective2MilestoneStatus2">';
        if (($user_data['MyObjective2MilestoneStatus2']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective2Milestones3'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 3</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective2MilestoneDates3" class="MilestoneInput" name="MyObjective2MilestoneDates3" disabled value="';
        echo dateget($user_data['MyObjective2MilestoneDates3']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective2Milestones3" class="MilestoneInput" name="MyObjective2Milestones3" disabled value="';
        echo $user_data['MyObjective2Milestones3']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective2MilestoneStatus3" class="MilestoneInput" name="MyObjective2MilestoneStatus3">';
        if (($user_data['MyObjective2MilestoneStatus3']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective2Milestones4'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 4</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective2MilestoneDates4" class="MilestoneInput" name="MyObjective2MilestoneDates4" disabled value="';
        echo dateget($user_data['MyObjective2MilestoneDates4']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective2Milestones4" class="MilestoneInput" name="MyObjective2Milestones4" disabled value="';
        echo $user_data['MyObjective2Milestones4']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective2MilestoneStatus4" class="MilestoneInput" name="MyObjective2MilestoneStatus4">';
        if (($user_data['MyObjective2MilestoneStatus4']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective2Milestones5'] != '') {
        $Objective1variable = 2;
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 5</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective2MilestoneDates5" class="MilestoneInput" name="MyObjective2MilestoneDates5" disabled value="';
        echo dateget($user_data['MyObjective2MilestoneDates5']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective2Milestones5" class="MilestoneInput" name="MyObjective2Milestones5" disabled value="';
        echo $user_data['MyObjective2Milestones5']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective2MilestoneStatus5" class="MilestoneInput" name="MyObjective2MilestoneStatus5">';
        if (($user_data['MyObjective2MilestoneStatus5']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }
      ?>
      </div>
      <br>
      <div style="display: flex; justify-content: center; align-items: center;">
        <button id="save2" disabled style="color:white; background-color: #C95746;" class="add-btn">Save</button>
      </div>
    
      </form>
      <br>

      <div class="container" style="grid-gap: 20px 20px;">
    
      <?php
      if ($Objective2variable != 2) {
        echo '<div class="add">';
        echo '<button style="color: white;" class="add-btn" onclick="toggleAddMilestonesObjective2()">+</button>';
        echo '</div>';
      }
      ?>

      <?php

        echo '<div id="edit2">';
        echo '<button id="edit2" style="color:white; background-color: #DE5F4C;" class="add-btn" onclick="toggleEditMilestonesObjective2()">Edit</button>';
        echo '</div>';
        echo '<div id="cancel2" style="display: none;">';
        echo '<button id=cancel2 style="color:white; background-color: #DE5F4C;" class="add-btn" onclick="toggleCancelMilestonesObjective2()">Cancel</button>';
        echo '</div>';
      
      ?>
      </div></div></div></div></div>




        
      <div class="popup" id="popup-AddMilestonesObjective2">
        <div class="overlay"></div>
          <div class = "content">
          <div class="close-btn" onclick="toggleAddMilestonesObjective2()">&times;</div>

          <form action="index.php" method="POST" class="form">
          <div class="MilestoneBox">
            <div style="display: flex; justify-content: center; align-items: center;">
              <label>Add Milestone</label>
            </div>
            <div style="display: inline-flex; float: right;">
              <label>Name:</label>
              <input type="text" id="NewObjective2MilestoneName" class="MilestoneInput" name="NewObjective2MilestoneName" value="" placeholder="MyMilestone">
            </div>
            <br>
            <div style="display: inline-flex; float: right;">
              <label>Due: </label>
             <input type="text" id="NewObjective2MilestoneDate" class="MilestoneInput" name="NewObjective2MilestoneDate" value="" placeholder="06/30/23">
            </div>
            <br>
            <div style="display: inline-flex; float: right;">
              <label>Status: </label>
             <input type="text" id="NewObjective2MilestoneStatus" class="MilestoneInput" name="NewObjective2MilestoneStatus" disabled value="Pending">
            </div>
            <br><br>
            <div style="display: inline-flex; justify-content: center; align-items: center;">
              <button id="SaveNewMilestone" style="color:white; background-color: #C95746;" class="add-btn">Save</button>
            </div>
            

          </div>
          </form>
            <br>
        </div>
      </div>








<div id="popup-Objective3" style="display: none">
    <div style="display: flex; justify-content: center; align-items: center;">
  <div class="box" style="border-radius: 50px; background: beige;"><div class="in-box">
    <div style="display: flex; justify-content: center; align-items:">
      <h2>My Milestones for</h2>
    </div>

    <form action="index.php" method="POST" class="form">
      <div style="display: flex; justify-content: center; align-items: center;">
        <input type="text" id="MyObjectives3" class="MilestoneInput" name="MyObjectives3" disabled value=" <?php echo $user_data['MyObjectives3']; ?> ">
      </div>
      <div style="display: flex; justify-content: center; align-items: center;">
        <input type="text" id="MyObjectivesDate3" class="MilestoneInput" name="MyObjectivesDate3" disabled value=" <?php echo dateget($user_data['MyObjectivesDate3']); ?> ">
      </div>
      <br>
      
      <div class="container" style="grid-gap: 20px 130px;">
    
      
      <?php 
      $Objective3variable = 0;
      if ($user_data['MyObjective3Milestones1'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 1</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective3MilestoneDates1" class="MilestoneInput" name="MyObjective3MilestoneDates1" disabled value="';
        echo dateget($user_data['MyObjective3MilestoneDates1']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective3Milestones1" class="MilestoneInput" name="MyObjective3Milestones1" disabled value="';
        echo $user_data['MyObjective3Milestones1']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective3MilestoneStatus1" class="MilestoneInput" name="MyObjective3MilestoneStatus1">';
        if (($user_data['MyObjective3MilestoneStatus1']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
        $Objective3variable = 1;
      }

      if ($user_data['MyObjective3Milestones2'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 2</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective3MilestoneDates2" class="MilestoneInput" name="MyObjective3MilestoneDates2" disabled value="';
        echo dateget($user_data['MyObjective3MilestoneDates2']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective3Milestones2" class="MilestoneInput" name="MyObjective3Milestones2" disabled value="';
        echo $user_data['MyObjective3Milestones2']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective3MilestoneStatus2" class="MilestoneInput" name="MyObjective3MilestoneStatus2">';
        if (($user_data['MyObjective3MilestoneStatus2']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective3Milestones3'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 3</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective3MilestoneDates3" class="MilestoneInput" name="MyObjective3MilestoneDates3" disabled value="';
        echo dateget($user_data['MyObjective3MilestoneDates3']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective3Milestones3" class="MilestoneInput" name="MyObjective3Milestones3" disabled value="';
        echo $user_data['MyObjective3Milestones3']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective3MilestoneStatus3" class="MilestoneInput" name="MyObjective3MilestoneStatus3">';
        if (($user_data['MyObjective3MilestoneStatus3']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective3Milestones4'] != '') {
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 4</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective3MilestoneDates4" class="MilestoneInput" name="MyObjective3MilestoneDates4" disabled value="';
        echo dateget($user_data['MyObjective3MilestoneDates4']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective3Milestones4" class="MilestoneInput" name="MyObjective3Milestones4" disabled value="';
        echo $user_data['MyObjective3Milestones4']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective3MilestoneStatus4" class="MilestoneInput" name="MyObjective3MilestoneStatus4">';
        if (($user_data['MyObjective3MilestoneStatus4']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }

      if ($user_data['MyObjective3Milestones5'] != '') {
        $Objective3variable = 2;
        echo '<div class="MilestoneBox">';
        echo '<div style="display: flex; justify-content: center; align-items: center;"><label>Milestone 5</label></div>';
        echo '<div style="display: inline-flex; float: right;"><label>Due:</label>';
        echo '<input type="text" id="MyObjective3MilestoneDates5" class="MilestoneInput" name="MyObjective3MilestoneDates5" disabled value="';
        echo dateget($user_data['MyObjective3MilestoneDates5']);
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Name: </label>';
        echo '<input type="text" id="MyObjective3Milestones5" class="MilestoneInput" name="MyObjective3Milestones5" disabled value="';
        echo $user_data['MyObjective3Milestones5']; 
        echo '"></div><br>';
        echo '<div style="display: inline-flex; float: right;"><label>Status: </label>';
        echo '<select disabled id="MyObjective3MilestoneStatus5" class="MilestoneInput" name="MyObjective3MilestoneStatus5">';
        if (($user_data['MyObjective3MilestoneStatus5']) == 'Pending') {
          echo '<option value="Pending">Pending</option>';
          echo '<option value="Completed">Completed</option></select></div>';
        } else {
          echo '<option value="Completed">Completed</option>';
          echo '<option value="Pending">Pending</option></select></div>';
        }
        echo '</div>';
      }
      ?>
      </div>
      <br>
      <div style="display: flex; justify-content: center; align-items: center;">
        <button id="save3" disabled style="color:white; background-color: #C95746;" class="add-btn">Save</button>
      </div>
    
      </form>
      <br>

      <div class="container" style="grid-gap: 20px 20px;">
    
      <?php
      if ($Objective3variable != 2) {
        echo '<div class="add">';
        echo '<button style="color: white;" class="add-btn" onclick="toggleAddMilestonesObjective3()">+</button>';
        echo '</div>';
      }
      ?>

      <?php
      if ($Objective3variable != 0) {
        echo '<div id="edit3">';
        echo '<button id="edit3" style="color:white; background-color: #DE5F4C;" class="add-btn" onclick="toggleEditMilestonesObjective3()">Edit</button>';
        echo '</div>';
        echo '<div id="cancel3" style="display: none;">';
        echo '<button id=cancel3 style="color:white; background-color: #DE5F4C;" class="add-btn" onclick="toggleCancelMilestonesObjective3()">Cancel</button>';
        echo '</div>';
      }
      ?>
      </div></div></div></div></div>




        
      <div class="popup" id="popup-AddMilestonesObjective3">
        <div class="overlay"></div>
          <div class = "content">
          <div class="close-btn" onclick="toggleAddMilestonesObjective3()">&times;</div>

          <form action="index.php" method="POST" class="form">
          <div class="MilestoneBox">
            <div style="display: flex; justify-content: center; align-items: center;">
              <label>Add Milestone</label>
            </div>
            <div style="display: inline-flex; float: right;">
              <label>Name:</label>
              <input type="text" id="NewObjective3MilestoneName" class="MilestoneInput" name="NewObjective3MilestoneName" value="" placeholder="MyMilestone">
            </div>
            <br>
            <div style="display: inline-flex; float: right;">
              <label>Due: </label>
             <input type="text" id="NewObjective3MilestoneDate" class="MilestoneInput" name="NewObjective3MilestoneDate" value="" placeholder="06/30/23">
            </div>
            <br>
            <div style="display: inline-flex; float: right;">
              <label>Status: </label>
             <input type="text" id="NewObjective3MilestoneStatus" class="MilestoneInput" name="NewObjective3MilestoneStatus" disabled value="Pending">
            </div>
            <br><br>
            <div style="display: inline-flex; justify-content: center; align-items: center;">
              <button id="SaveNewMilestone" style="color:white; background-color: #C95746;" class="add-btn">Save</button>
            </div>
            

          </div>
          </form>
            <br>
        </div>
      </div>
      





    




    <br><br><br>
    </body>
    </html>
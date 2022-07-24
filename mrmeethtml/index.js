
  // Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);

// Create a new list item when clicking on the "Add" button
function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}

function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}





var show;
function toggleObjective(ObjectiveNo){
  if (show == ObjectiveNo) {
    show = 0;
    document.getElementById("popup-Objective1").style.display = "none";
    document.getElementById("popup-Objective2").style.display = "none";
    document.getElementById("popup-Objective3").style.display = "none";
  }
  else {
    if (ObjectiveNo == 1) {
      show = 1;
      document.getElementById("popup-Objective1").style.display = "block";
      document.getElementById("popup-Objective2").style.display = "none";
      document.getElementById("popup-Objective3").style.display = "none";
    }
    else if (ObjectiveNo == 2) {
      show = 2;
      document.getElementById("popup-Objective1").style.display = "none";
      document.getElementById("popup-Objective2").style.display = "block";
      document.getElementById("popup-Objective3").style.display = "none";
    }
    else if (ObjectiveNo == 3) {
      show = 3;
      document.getElementById("popup-Objective1").style.display = "none";
      document.getElementById("popup-Objective2").style.display = "none";
      document.getElementById("popup-Objective3").style.display = "block";
    }
    
  }
    
}

//popup
function toggleAddObjectives(){
  document.getElementById("popup-AddObjectives").classList.toggle("active");
}

function toggleAddMilestonesObjective1(){
  document.getElementById("popup-AddMilestonesObjective1").classList.toggle("active");
}

function toggleAddMilestonesObjective2(){
  document.getElementById("popup-AddMilestonesObjective2").classList.toggle("active");
}

function toggleAddMilestonesObjective3(){
  document.getElementById("popup-AddMilestonesObjective3").classList.toggle("active");
}


function toggleCancelMilestonesObjective1(){
    document.getElementById("edit1").style.display = "block";
    document.getElementById("cancel1").style.display = "none";

    document.getElementById("save1").disabled = true;
    document.getElementById("save1").style.background = "#C95746";

    document.getElementById("MyObjectives1").disabled = true;
    document.getElementById("MyObjectivesDate1").disabled = true;
    document.getElementById("MyObjective1MilestoneDates1").disabled = true;
    document.getElementById("MyObjective1Milestones1").disabled = true;
    document.getElementById("MyObjective1MilestoneStatus1").disabled = true;
  
    document.getElementById("MyObjective1MilestoneDates2").disabled = true;
    document.getElementById("MyObjective1Milestones2").disabled = true;
    document.getElementById("MyObjective1MilestoneStatus2").disabled = true;

    document.getElementById("MyObjective1MilestoneDates3").disabled = true;
    document.getElementById("MyObjective1Milestones3").disabled = true;
    document.getElementById("MyObjective1MilestoneStatus3").disabled = true;
  
    document.getElementById("MyObjective1MilestoneDates4").disabled = true;
    document.getElementById("MyObjective1Milestones4").disabled = true;
    document.getElementById("MyObjective1MilestoneStatus4").disabled = true;
  
    document.getElementById("MyObjective1MilestoneDates5").disabled = true;
    document.getElementById("MyObjective1Milestones5").disabled = true;
    document.getElementById("MyObjective1MilestoneStatus5").disabled = true;
}





function toggleEditMilestonesObjective1(){
    document.getElementById("edit1").style.display = "none";
    document.getElementById("cancel1").style.display = "block";
    
    document.getElementById("save1").style.background = "#DE5F4C";
    document.getElementById("save1").disabled = false;
  
    document.getElementById("MyObjectives1").disabled = false;
    document.getElementById("MyObjectivesDate1").disabled = false;
    document.getElementById("MyObjective1MilestoneDates1").disabled = false;
    document.getElementById("MyObjective1Milestones1").disabled = false;
    document.getElementById("MyObjective1MilestoneStatus1").disabled = false;
  
    document.getElementById("MyObjective1MilestoneDates2").disabled = false;
    document.getElementById("MyObjective1Milestones2").disabled = false;
    document.getElementById("MyObjective1MilestoneStatus2").disabled = false;

    document.getElementById("MyObjective1MilestoneDates3").disabled = false;
    document.getElementById("MyObjective1Milestones3").disabled = false;
    document.getElementById("MyObjective1MilestoneStatus3").disabled = false;
  
    document.getElementById("MyObjective1MilestoneDates4").disabled = false;
    document.getElementById("MyObjective1Milestones4").disabled = false;
    document.getElementById("MyObjective1MilestoneStatus4").disabled = false;
  
    document.getElementById("MyObjective1MilestoneDates5").disabled = false;
    document.getElementById("MyObjective1Milestones5").disabled = false;
    document.getElementById("MyObjective1MilestoneStatus5").disabled = false;

  
}




function toggleCancelMilestonesObjective2(){
    document.getElementById("edit2").style.display = "block";
    document.getElementById("cancel2").style.display = "none";

    document.getElementById("save2").disabled = true;
    document.getElementById("save2").style.background = "#C95746";

    document.getElementById("MyObjectives2").disabled = true;
    document.getElementById("MyObjectivesDate2").disabled = true;
    document.getElementById("MyObjective2MilestoneDates1").disabled = true;
    document.getElementById("MyObjective2Milestones1").disabled = true;
    document.getElementById("MyObjective2MilestoneStatus1").disabled = true;
  
    document.getElementById("MyObjective2MilestoneDates2").disabled = true;
    document.getElementById("MyObjective2Milestones2").disabled = true;
    document.getElementById("MyObjective2MilestoneStatus2").disabled = true;

    document.getElementById("MyObjective2MilestoneDates3").disabled = true;
    document.getElementById("MyObjective2Milestones3").disabled = true;
    document.getElementById("MyObjective2MilestoneStatus3").disabled = true;
  
    document.getElementById("MyObjective2MilestoneDates4").disabled = true;
    document.getElementById("MyObjective2Milestones4").disabled = true;
    document.getElementById("MyObjective2MilestoneStatus4").disabled = true;
  
    document.getElementById("MyObjective2MilestoneDates5").disabled = true;
    document.getElementById("MyObjective2Milestones5").disabled = true;
    document.getElementById("MyObjective2MilestoneStatus5").disabled = true;
}





function toggleEditMilestonesObjective2(){
    document.getElementById("edit2").style.display = "none";
    document.getElementById("cancel2").style.display = "block";
    
    document.getElementById("save2").style.background = "#DE5F4C";
    document.getElementById("save2").disabled = false;
  
    document.getElementById("MyObjectives2").disabled = false;
    document.getElementById("MyObjectivesDate2").disabled = false;
    document.getElementById("MyObjective2MilestoneDates1").disabled = false;
    document.getElementById("MyObjective2Milestones1").disabled = false;
    document.getElementById("MyObjective2MilestoneStatus1").disabled = false;
  
    document.getElementById("MyObjective2MilestoneDates2").disabled = false;
    document.getElementById("MyObjective2Milestones2").disabled = false;
    document.getElementById("MyObjective2MilestoneStatus2").disabled = false;

    document.getElementById("MyObjective2MilestoneDates3").disabled = false;
    document.getElementById("MyObjective2Milestones3").disabled = false;
    document.getElementById("MyObjective2MilestoneStatus3").disabled = false;
  
    document.getElementById("MyObjective2MilestoneDates4").disabled = false;
    document.getElementById("MyObjective2Milestones4").disabled = false;
    document.getElementById("MyObjective2MilestoneStatus4").disabled = false;
  
    document.getElementById("MyObjective2MilestoneDates5").disabled = false;
    document.getElementById("MyObjective2Milestones5").disabled = false;
    document.getElementById("MyObjective2MilestoneStatus5").disabled = false;

  
}


function toggleCancelMilestonesObjective3(){
    document.getElementById("edit3").style.display = "block";
    document.getElementById("cancel3").style.display = "none";

    document.getElementById("save3").disabled = true;
    document.getElementById("save3").style.background = "#C95746";

    document.getElementById("MyObjectives3").disabled = true;
    document.getElementById("MyObjectivesDate3").disabled = true;
    document.getElementById("MyObjective3MilestoneDates1").disabled = true;
    document.getElementById("MyObjective3Milestones1").disabled = true;
    document.getElementById("MyObjective3MilestoneStatus1").disabled = true;
  
    document.getElementById("MyObjective3MilestoneDates2").disabled = true;
    document.getElementById("MyObjective3Milestones2").disabled = true;
    document.getElementById("MyObjective3MilestoneStatus2").disabled = true;

    document.getElementById("MyObjective3MilestoneDates3").disabled = true;
    document.getElementById("MyObjective3Milestones3").disabled = true;
    document.getElementById("MyObjective3MilestoneStatus3").disabled = true;
  
    document.getElementById("MyObjective3MilestoneDates4").disabled = true;
    document.getElementById("MyObjective3Milestones4").disabled = true;
    document.getElementById("MyObjective3MilestoneStatus4").disabled = true;
  
    document.getElementById("MyObjective3MilestoneDates5").disabled = true;
    document.getElementById("MyObjective3Milestones5").disabled = true;
    document.getElementById("MyObjective3MilestoneStatus5").disabled = true;
}





function toggleEditMilestonesObjective3(){
    document.getElementById("edit3").style.display = "none";
    document.getElementById("cancel3").style.display = "block";
    
    document.getElementById("save3").style.background = "#DE5F4C";
    document.getElementById("save3").disabled = false;
  
    document.getElementById("MyObjectives3").disabled = false;
    document.getElementById("MyObjectivesDate3").disabled = false;
    document.getElementById("MyObjective3MilestoneDates1").disabled = false;
    document.getElementById("MyObjective3Milestones1").disabled = false;
    document.getElementById("MyObjective3MilestoneStatus1").disabled = false;
  
    document.getElementById("MyObjective3MilestoneDates2").disabled = false;
    document.getElementById("MyObjective3Milestones2").disabled = false;
    document.getElementById("MyObjective3MilestoneStatus2").disabled = false;

    document.getElementById("MyObjective3MilestoneDates3").disabled = false;
    document.getElementById("MyObjective3Milestones3").disabled = false;
    document.getElementById("MyObjective3MilestoneStatus3").disabled = false;
  
    document.getElementById("MyObjective3MilestoneDates4").disabled = false;
    document.getElementById("MyObjective3Milestones4").disabled = false;
    document.getElementById("MyObjective3MilestoneStatus4").disabled = false;
  
    document.getElementById("MyObjective3MilestoneDates5").disabled = false;
    document.getElementById("MyObjective3Milestones5").disabled = false;
    document.getElementById("MyObjective3MilestoneStatus5").disabled = false;

  
}



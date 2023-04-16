function f(){
var b=document.getElementById("b").innerHTML;
if(b==""){}
if(b=="0"){alert("please give a valid image \n -->image shouldn`t consist of multiple people \n -->both the eyes of the person must be visible");}
if(b=="1"){document.getElementById("d1").style.animation="anime 0.1s 3";document.getElementById("d1").style.background="green";}
if(b=="3"){
document.getElementById("d2").style.background="green";document.getElementById("d2").style.animation="anime 0.1s 3";
}
if(b=="2"){ 
document.getElementById("d3").style.background="green";document.getElementById("d3").style.animation="anime 0.1s 3; 
}
}

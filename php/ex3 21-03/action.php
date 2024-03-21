<?php

include("connect.php");
session_start( );


$username = mysqli_real_escape_string($con,$_POST["username"]);
$password =mysqli_real_escape_string($con,$_POST["password"]);


if (empty ($username) || empty ($password)){
    header ("location: index.html");
    exit();
    } 
    
    $query = "SELECT * FROM user WHERE username = '$username' AND passw = '$password'";
    echo $query;
    $result = mysqli_query($con, $query);

    $row = mysqli_num_rows($result);



echo $row;

if($row == 1){
    header ('location:admin.html');
    exit();
}
else{
    header('location: index.html');
    exit();
}


?>
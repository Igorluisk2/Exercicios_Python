<?php

include("connect.php");
session_start( );


$nome = mysqli_real_escape_string($con,$_POST["username"]);
$senha =mysqli_real_escape_string($con,$_POST["password"]);


if (empty ($nome) || empty ($senha)){
    header ("location: index.html");
    exit();
    } 
    
    $query = "SELECT * FROM users WHERE username = '$nome' AND password = '$senha'";
    echo $query;
    $result = mysqli_query($con, $query);

    $row = mysqli_num_rows($result);
echo $row;

?>
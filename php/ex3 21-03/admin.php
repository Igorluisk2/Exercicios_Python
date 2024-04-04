<?php
include("verificacao.php");
include("connect.php");
$query = "SELECT * FROM FABRICAUSERS";
$usuarios = mysqli_query($con,$query);
?>
<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<link rel="stylesheet" href="./style.css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<nav class="navbar navbar-default navbar-static-top">
	<div class="container-fluid">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="#">
				Brand
			</a>
		</div>

		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">			
			<form class="navbar-form navbar-left" method="GET" role="search">
				<div class="form-group">
					<input type="text" name="q" class="form-control" placeholder="Search">
				</div>
				<button type="submit" class="btn btn-default"><i class="glyphicon glyphicon-search"></i></button>
			</form>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="logout.php" target="">Logout</a></li>
				<li class="dropdown ">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
						Account
						<span class="caret"></span></a>
						<ul class="dropdown-menu" role="menu">
							<li class="dropdown-header">SETTINGS</li>
							<li class=""><a href="#">Other Link</a></li>
							<li class=""><a href="#">Other Link</a></li>
							<li class=""><a href="#">Other Link</a></li>
							<li class="divider"></li>
							<li><a href="#">Logout</a></li>
						</ul>
					</li>
				</ul>
			</div><!-- /.navbar-collapse -->
		</div><!-- /.container-fluid -->
	</nav>
	<div class="container-fluid main-container">
		<div class="col-md-2 sidebar">
			<ul class="nav nav-pills nav-stacked">
				<li class="active"><a href="#">Home</a></li>
			</ul>
		</div>
		<div class="col-md-10 content">
            <div class="panel panel-default">
                <div class="panel-heading">
                    Relatório dos cadastros
                </div>
				<div class="panel panel-default">
    <div class="panel-body">
        <div class="table-responsive">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>CPF</th>
                        <th>RG</th>
                        <th>Telefone</th>
                        <th>Email</th>
                        <th>Mãe</th>
                        <th>Pai</th>
                        <th>Rua</th>
                        <th>Bairro</th>
                        <th>Nº</th>
                        <th>CEP</th>
                        <th>Complemento</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while ($usuario = mysqli_fetch_array($usuarios)) { ?>
                        <tr>
                            <td><?php echo $usuario["name"]; ?></td>
                            <td><?php echo $usuario["cpf"]; ?></td>
                            <td><?php echo $usuario["rg"]; ?></td>
                            <td><?php echo $usuario["telefone"]; ?></td>
                            <td><?php echo $usuario["email"]; ?></td>
                            <td><?php echo $usuario["mother"]; ?></td>
                            <td><?php echo $usuario["father"]; ?></td>
                            <td><?php echo $usuario["street"]; ?></td>
                            <td><?php echo $usuario["neighborhood"]; ?></td>
                            <td><?php echo $usuario["number"]; ?></td>
                            <td><?php echo $usuario["cep"]; ?></td>
                            <td><?php echo $usuario["complement"]; ?></td>
                        </tr>
                    <?php } ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

		<footer class="pull-left footer">
			<p class="col-md-12">
				<hr class="divider">
				Copyright &COPY; 2015 <a href="http://www.pingpong-labs.com">Gravitano</a>
			</p>
		</footer>
	</div>
<!DOCTYPE html>

<html>
<head>
    <title>Informações do Formulário</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtendo os valores dos campos do formulário
    $nome = $_POST["nome"];
    $rg = $_POST["rg"];
    $cpf = $_POST["cpf"];
    $endereco = $_POST["endereco"];
    $idade = $_POST["idade"];
    $data = $_POST["data"];
    $estacoes = isset($_POST["estacao"]) ? $_POST["estacao"] : array();
    $genero = $_POST["genero"];
    $cor = $_POST["cor"];

    //Tabela
    echo "<h2>Dados do Formulário</h2>";
    echo "<table>";
    echo "<tr><th>Campo</th><th>Preenchido</th></tr>";
    echo "<tr><td>Nome</td><td>$nome</td></tr>";
    echo "<tr><td>RG</td><td>$rg</td></tr>";
    echo "<tr><td>CPF</td><td>$cpf</td></tr>";
    echo "<tr><td>Endereço</td><td>$endereco</td></tr>";
    echo "<tr><td>Idade</td><td>$idade</td></tr>";
    echo "<tr><td>Data</td><td>$data</td></tr>";
    echo "<tr><td>Épocas do Ano</td><td>";
    if (!empty($estacoes)) {
        echo implode(", ", $estacoes);
    } else {
        echo "Nenhuma estação selecionada";
    }
    echo "</td></tr>";
    echo "<tr><td>Gênero</td><td>$genero</td></tr>";
    echo "<tr><td>Cor Preferida</td><td style='background-color: $cor;'></td></tr>";
    echo "</table>";
}
?>
</body>
</html>

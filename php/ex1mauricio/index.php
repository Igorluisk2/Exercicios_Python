//1.	Fazer um algoritmo que: Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. Calcule e escreva a idade média deste grupo de indivíduos.

<!DOCTYPE html>
<html>
<head>
    <title>Calculadora de Idade Média</title>
</head>
<body>

<h2>Calculadora de Idade Média</h2>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $idades = $_POST["idades"];

    // Separa as idades em um array
    $idades_array = explode("\n", $idades);

    // Remove linhas vazias e espaços em branco
    $idades_array = array_filter(array_map('trim', $idades_array));

    $idades_total = 0;
    $quantidade = count($idades_array);

    // Calcula a soma das idades
    foreach ($idades_array as $idade) {
        $idades_total += intval($idade);
    }

    // Calcula a idade média, verificando se há pelo menos uma idade
    if ($quantidade > 0) {
        $media = $idades_total / $quantidade;
        echo "A idade média deste grupo de indivíduos é: " . number_format($media, 2);
    } else {
        echo "Nenhuma idade foi inserida.";
    }
}
?>

<form method="post">
    <label>Digite as idades (uma por linha):</label><br>
    <textarea name="idades" rows="5" cols="40"></textarea><br>
    <input type="submit" value="Calcular Média">
</form>

</body>
</html>

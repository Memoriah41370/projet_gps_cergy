<!DOCTYPE html>
<html lang="fr">
  <head>
    <title>Google map en mieux</title>
    <meta name="generator" content="Atom">
    <meta name="author" content="Nathan">
    <meta name="date" content="2021-02-16">
    <meta name="copyright" content="true">
    <meta name="keywords" content="">
    <meta name="description" content="cour de PHP">
    <link type="text/css" rel="stylesheet" href="style.css">
  </head>
<body>
  <ul>
    <li><a href="https://googlemapenmieux.wordpress.com/blog/">Accueil</a></li>
  </ul>
  <div class="marron">
    <h1 id="centre">- - - Cergy Map - - -</h1>
    <img src="logo.png" height="50" alt="Logo">
  </div>
  <div id="premier">
    <form action="index.php" method="post">
      <span>Depart :     <input type="text" name="choixvillededepart" /></span>
      <span>Arrive :     <input type="text" name="choixvillearrive" /></span>
      <input type="submit" name="submit" />
    </form>
    <?php
            if(isset($_POST["submit"]))
            {
                $choixvillededepart = $_POST["choixvillededepart"];
                $choixvillearrive = $_POST["choixvillearrive"];
                $command = escapeshellcmd ('python oui.py ' . $choixvillededepart .' ' . $choixvillearrive );
                $output = exec($command);
                echo $output;
             }
    ?>
    <div id="France">
      <img src="carte_de_france.png" height="450" alt="carte">
    </div>
  </div>
</body>
</html>

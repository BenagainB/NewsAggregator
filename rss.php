<?php
    
?>
<html>
    <head>
        <title>User Dashboard</title>
    </head>
    <body>
        <h1>Dashboard</h1>
        <p> Hey, <?php echo $username ?>! </p>
        <p> You are now on the User Dashboard page. </p>
        <p> <a href="logout.php"> Logout </a>
        <h2>Select the books you wish</h2>
        
        <form method="post" action="">
            <?php
                f ($fp = fopen('http://www.google.com/', 'r')) {
                    $content = '';
                    while ($line = fread($fp, 1024)) {
                       $content .= $line;
                    }
                 } else {
                    // an error occured when trying to open the specified url 
                 }
            ?>
            <br><br>
            <input type='submit' name='submit'> <br>
        </form>

        
        
        
    </body>
</html>

<!DOCTYPE HTML>  
<html>
    <head>
        <style>
        </style>
    </head>
    <body>  
        <?php
            $servername = "localhost";
            $dbname = "quotes_database.db";
            $username = "username";
            $password = "password";
            $conn = new mysqli($servername, $username, $password, $dbname);
            if ($conn -> connect_error) {
                die("Connection failed: " . $conn -> connect_error);
            }
            $quote = "SELECT * FROM quotes order by RANDOM() limit 1";
            $result = $conn -> query($quote);
            while ($row = $result -> fetch_assoc())
                echo $row["quote"]. "\n\t -- " . $row["author"]. "<br>";
            $conn->close();
        ?>
    </body>
</html>

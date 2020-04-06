<?php
    // Curls start with an initialization:
    $curl = curl_init();
    $url = "age-of-empires-2-api.herokuapp.com/api/v1/civilizations";
    // Then options must be set:
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($curl, CURLOPT_HEADER, 0);

    // Saves the output to a variable. Here we call it "output" for simplicity:
    $output = curl_exec($curl);

    if($output === FALSE) {
        echo "cURL Error: " + curl_error($curl);
    }

    // Close and free up the curl handle:
    curl_close($curl);

    print_r($output);
?>

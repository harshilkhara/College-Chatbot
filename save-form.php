<?php

if($_POST['tag'] != '' && $_POST['patterns'] != '' && $_POST['responses'] != ''){
	
	if(file_exists('json/student_data.json')){

		$current_data = file_get_contents('json/student_data.json');
		$array_data = json_decode($current_data, true);
		$new_data = array( 
								'tag' => $_POST['tag'],
								'patterns' => [$_POST['patterns']],
								'responses' => [$_POST['responses']]
						
							);

		$array_data[] = $new_data;
		

		$json_data = json_encode($array_data,JSON_PRETTY_PRINT);

		if(file_put_contents('json/student_data.json', $json_data))
		{
			echo "<h3>Successfully saved data in JSON file.</h3>";
		}else{
			echo "<h3>UnSuccessfully saved data in JSON file.</h3>";
		}
	}else{
		echo "<h3>JSON file not exist.</h3>";
	}
}else{
	echo "<h3>All form fields are required.</h3>";
}


?>

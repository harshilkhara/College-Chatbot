<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>PHP & JSON File</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div id="main">
    <div id="header">
      <h1>Save Form Data in JSON File</h1>
    </div>

    <div id="table-data">
      <form id="submit_form" method="post" action="save-form.php">  
        <table width="100%" cellpadding="10px">
          <tr>
            <td width="150px"><label>Tag</label></td>
            <td><input type="text" name="tag" autocomplete="off" /></td>
          </tr>
          <tr>
            <td><label>Patterns</label></td>
            <td><input type="text" name="patterns" autocomplete="off" /></td>
          </tr>
          <tr>
            <td><label>Responses</label></td>
            <td>
              <input type="text" name="responses" autocomplete="off" />   
            </td>
          </tr>
          </tr>
          <tr>
            <td></td>
            <td><input type="submit" name="submit" id="submit" /></td>
          </tr>
        </table>
      </form>  
    </div>
  </div>

</body>
</html>

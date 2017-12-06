<?php
opcache_reset();
echo "What User am I?";
exec('whoami 2>&1', $output, $return_var);
var_dump($output);
exec('sudo -S whoami 2>&1 true', $output, $return_var);
var_dump($output);
return 0;
?>

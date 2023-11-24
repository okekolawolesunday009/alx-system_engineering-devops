# Kill the process named 'killmenow'
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}

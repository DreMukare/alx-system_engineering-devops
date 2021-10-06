# increase nginx file limit to allow more requests to be made
exec {'fix--for-nginx':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'sed -i '/error_log.*/a \\\topen_file_cache max=200000 inactive=20s;' /etc/nginx/nginx.conf &&\
             sed -i '/error_log.*/a \\\topen_file_cache_valid 30s;' /etc/nginx/nginx.conf &&\
             sed -i '/error_log.*/a \\\topen_file_cache_min_uses 2;' /etc/nginx/nginx.conf &&\
             sed -i '/error_log.*/a \\\topen_file_cache_errors on;' /etc/nginx/nginx.conf',
}

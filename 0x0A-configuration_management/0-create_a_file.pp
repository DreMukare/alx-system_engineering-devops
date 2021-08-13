# creating a file in /tmp with specific requirements

file {'holberton':
    path    => '/tmp/holberton',
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
}

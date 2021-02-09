# Shell Permissions
This directory contains various shell commands to manipulate different shell permissions. 

All scripts start with `#!/bin/bash`

## Change my user ID to betty
```
su betty
```

## Print effective user id of current user
```
whoami
```

## Print all the groups that current user is part of 
```
groups
```

## Change owner of the file hello to the user betty
```
chown betty hello
```

## Create empty file called hello 
```
touch hello
```

## Add execute permissions to owner of file hello
```
chmod u+x hello
```

## Add execute permissions to the owner and the group owner and read permission to other users to hello
```
chmod u+x,g+x,o+r hello
```

## Add execute permissions to everyone on file hello 
```
chmod +x hello
```

## Give owner and group no permissions and group all permissions
```
chmod 007 hello
```

## Set mode of the file hello to `-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`
```
chmod 753 hello
```

## Set mode of hello the same as olleh
```
chmod --reference=olleh hello
```

## Add execute permission to all subdirectories of current directory for all users. Regular files not changed
```
chmod a+X *
```

## Create a directory called dir_holberton with permissions 751 in current working directory
```
mkdir -m751 dir_holberton
```

## Change group owner of hello to holberton
```
chgrp holberton hello
```

## Change owner to betty and group owner to holberton for all files and directories in working directory
```
sudo chown -R betty:holberton *
```

## Change owner and group owner of symbolic link __hello to betty and holberton
```
sudo chown -h betty:holberton _hello
```

## Change owner of hello to betty only if it is owned by guillaume
```
chown --from=guillaume betty hello
```

## Play star wars episode IV in terminal
```
telnet towel.blinkenlights.nl
```



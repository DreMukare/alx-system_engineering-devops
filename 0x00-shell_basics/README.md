# Shell Basics

This directory covers various basic shell commands

## Current working directory
```
pwd
```

## Display contents of current working directory
```
ls
```

## Change working directory to users home directory
```
cd
```

## Display directory contents in long format
```
ls -l
```

## Display directory contents including hiddent files
```
ls -la
```

## Display directory contents with user and group ids displayed numerically 
```
ls -lan
```

## Create directory named holberton in /tmp/ directory
```
mkdir /tmp/holberton
```

## Move file betty from /tmp/ to /tmp/holberton
```
mv /tmp/betty /tmp/holberton
```

## Delete the file betty in /tmp/holberton
```
rm /tmp/holberton/betty
```

## Delete directory holberton in the /tmp/ directory
```
rmdir /tmp/holberton
```

## Change working directory to previous one
```
cd -
```

## List all files in current directory, parent directory or working directory and in the /boot directory in long format
```
ls -la . .. /boot
```

## Print type of iamafile in /tmp directory
```
file /tmp/iamafile
```

## Create symbolic link to /bin/ls named __ls__
```
ln -s /bin/ls __ls__
```

## Copy all html files from current directory to parent directory. Only copy fles that don't exist in parent or are newer versions
```
cp -u *.html ..
```

## Move all files beginning with an uppercase letter to /tmp/u
```
mv [[:upper:]]* /tmp/u
```

## Delete all files that end with tilde
```
rm *~
```

## Create the directories welcome/, welcome/to/ and welcome/to/holberton
```
mkdir -p welcome/to/holberton
```

## List all files and directories of current directory separated by commas
```
ls -lapm
```



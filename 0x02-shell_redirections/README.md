# Shell Redirections and Filters
This repository contains scripts that carry out commands to do with shell redirections and filters.

Each script starts with `#!/bin/bash`

## Script that prints "Hello, World" followed by new line to standard output
```
echo "Hello, World"
```

## Script that displays "(Ôo)'
```
echo -e "\x22\x28\xC3\x94\x6F\x29\x27"
```

## Display content of /etc/passwd
```
less /etc/passwd 
```

## Display content of /etc/passwd and /etc/hosts
```
cat /etc/passwd /etc/hosts 
```

## Display 10 last lines of /etc/passwd
```
tail /etc/passwd
```

## Display 10 first lines of /etc/passwd
```
head /etc/passwd
```

## Display third line of iacta
```
head -n 3 iacta | tail -n 1 
```

## Create file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text "Holberton School"
```
printf "Holberton School\n" > "\\*\\\\'\"Holberton School\"\'\\\\*$\\?\*\*\*\*\*:)" 
```

## Write into ls_cwd_content results of ls -la
```
ls -la > ls_cwd_content
```

## Duplicate last line of iacta
```
tail -n 1 iacta >> iacta  
```

## Delete all files (not directories) with a .js extension in current directory and all subdirectories
```
find . -type f -name '*.js' -delete 
```

## Count number of directories and subdirectories in current directory
```
ls -lR | grep ^d | wc -l 
```

## Display 10 newest files in current directory
```
find . -type d | ls -t | head  
```

## Take long list of words as input and print only words that appear once
```
sort | uniq -u 
```

## Display linees containing pattern "root" from /etc/passwd
```
grep root /etc/passwd 
```

## Count the number of lines that contain the pattern "bin" in /etc/passwd
```
grep -c bin /etc/passwd
```

## Display lines containing pattern "root" and 3 lines after them in /etc/passwd
```
grep -A 3 root /etc/passwd
```

## Display all the lines that do not contain "bin" in /etc/passwd
```
grep -v bin /etc/passwd  
```

## Display all the lines of /etc/ssh/sshd_config starting with letter
```
grep ^[[:alpha:]] /etc/ssh/sshd_config
```

## Replace all characters A and c from input to Z and e respectively
```
tr "Ac" "Ze" 
```

## Remove all letters c and C from input
```
tr -d 'cC' 
```

## Reverse input
```
rev
```

## Display all users and home directories sorted by user
```
cat /etc/passwd | cut -d ':' -f 1,6 | sort
```





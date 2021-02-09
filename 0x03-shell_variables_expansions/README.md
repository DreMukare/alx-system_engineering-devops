# Shell Variables and Expansion

This directory contains commands that explore shell variables and expansions as well as init files. 

Every script starts with `#!/bin/bash`

## Create an alias named `ls` with the value `rm *`
```
alias ls='rm *'
```

## Print "hello user" where user is the current Linux user
```
echo "hello $USER" 
```

## Add /action to the /PATH
```
export PATH="$PATH:/action"
```

## Count the number of directories in the PATH
```
echo $PATH | tr ":" "\n" | wc -l
```

## List environment variables
```
printenv
```

## List all local variables and environment variables and functions
```
set
```

## Create new local variable named "BETTY" with value "Holberton"
```
BETTY="Holberton"
```

## Create global variable named "HOLBERTON" with value "Betty"
```
export HOLBERTON="Betty"
```

## Print result of the addition of 128 with value stored in environment variable TRUEKNOWLEDGE
```
echo "$((128 + $TRUEKNOWLEDGE))"
```

## Print result of POWER divided by DIVIDE
```
echo "$(($POWER / $DIVIDE))"
```

## Display result of BREATH to the power of LOVE
```
echo "$(($BREATH ** $LOVE))"
```

## Convert number from base 2 to base 10 
```
echo "$((2#$BINARY))"
```

## Print all combinations of two letters except oo
```
echo {a..z}{a..z} | tr " " "\n" | grep -v "oo"
```

## Print a number with two decimal places and store in environment variable NUM
```
printf "%0.2f\n" $NUM
```

## Convert number from base 10 to base 16
```
printf "%x\n" $DECIMAL
```

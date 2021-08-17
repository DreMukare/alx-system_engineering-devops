# 0x0D. Web stack debugging #0

This project goes over the process of debugging a webstack. 
The task is to debug why expected output is not recieved when querying the root page of an apache2 server running on a docker container.

## Test and verify your assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:
- is the web server started? - You can check using the service manager, also double check by checking process list.
- On what port should it listen? - Check your web server configuration
- Is it actually listening on this port? `netstat -lpdn` run as root or sudo so that you can see the process for each listening port
- It is listening on the correct server IP? - netstat is also your friend here
- Is there a firewall enabled?
- Have you looked at logs? - usually in /var/log and tail -f is your friend
- Can I connect to the HTTP port from the location I am browsing from? - curl is your friend

# Installing LibreOffice with Python on Debian

1. Install libreoffice and python3 globally

    $ sudo apt install libreoffice libreoffice-calc python3-uno -y

2. Create virtual environment

It is always recommended to create a separate virtual environment for every work with Python.
For some oppinionated information and guidance about this topic, please visit:

http://github.com/frgomes/bash-scripts

In other words, execute the commands below:

    $ curl -s https://raw.githubusercontent.com/frgomes/bash-scripts/master/unsafe/bashrc-up | sh

The open a new terminal and create a virtual environment for working on this project, like this:

    $ mkvirtualenv soffice --system-site-packages
    $ workon soffice

If everything is according to plan, wyou shoudl see a message "(soffice)" at the beginning of your prompt, like this:

    (soffice) [2024-07-26 23:33:23] rgomes@mars:~/Sync$

Great! You are now inside a virtual environment intended to work on this project.


# Connecting to a LibreOffice server instance

1. Open LibreOffice in listening mode

    $ soffice --calc --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager"

2. Run a simple test program, which actually only tests the ability to import UNO library:

    $ python3 price_analysis.py


# References

  * https://www.youtube.com/watch?v=g8I8uGjaXA8

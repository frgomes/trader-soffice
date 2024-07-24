# Installing LibreOffice with Python on Debian

1. Install libreoffice and python3 globally

    $ sudo apt install libreoffice libreoffice-calc python3-uno -y

2. Create virtual environment

It is always recommended to create a separate virtual environment for every work with Python.
For some oppinionated information and guidance about this topic, please visit:

http://github.com/frgomes/bash-scripts

# Open LibreOffice in listening mode

    $ soffice --calc --accept="socket,host=localhost,port=20000;urp;StarOffice.ServiceManager"

# References

  * https://www.youtube.com/watch?v=g8I8uGjaXA8

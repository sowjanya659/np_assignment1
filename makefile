all: say_hello help server client
say_hello:
                @echo "Hello"

help:
        @echo "---------------HELP------------------------------"
        @echo "To know the server status type make server"
        @echo "To know the client status type make client"
        @echo "To delete .pyc and _pycache files type make clean"
        @echo "--------------------------------------------------"

PYTHON = python3
server:
        ${PYTHON} server 127.0.0.1:5050
client:
        ${PYTHON} client 127.0.0.1:5050
clean:
        find . -type f -name *.pyc -delete
        find . -type d -name _pycache_ -delete

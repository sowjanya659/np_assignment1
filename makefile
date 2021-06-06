all: say_hello

say_hello:
		@echo "Hello"

clean:
	find . -type f -name *.pyc -delete
	find . -type d -name _pycache_ -delete

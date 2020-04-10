compile:
	python -c "import py_compile; py_compile.compile('main.py')"

run: compile
	python __pycache__/main.cpython-37.pyc

install:
	pip install uncompyle6

decompile: compile install
	uncompyle6 __pycache__/main.cpython-37.pyc > decompiled_main.py

disasm:
	python -c "import main, dis; print(dis.dis(main))"


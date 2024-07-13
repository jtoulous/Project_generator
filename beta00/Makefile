all: venv install

venv:
	@python -m venv VirtualEnvironnement

install:
	@. VirtualEnvironnement/bin/activate && pip install -r requirements.txt

clean:
	@rm -rf VirtualEnvironnement



.PHONY:	all venv install clean
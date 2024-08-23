# var
PEPS = E26,E302,E305,E401,E402,E701,E702

# tool
CURL = curl -L -o
PY   = /usr/bin/python3
PIP  = /usr/bin/pip3
PEP  = /usr/bin/autopep8

# src
Y += $(wildcard src/*.py)

# all
.PHONY: all
all: run

.PHONY: run
run: $(PY) $(Y)
	$^

# format
.PHONY: format
format: tmp/format_py
tmp/format_py: $(Y)
	$(PEP) --ignore $(PEPS) -i $? && touch $@

# install
.PHONY: install update ref gz
install: ref gz
	$(MAKE) update
update:
	sudo apt update
	sudo apt install -uy `cat apt.txt`
ref:
gz:

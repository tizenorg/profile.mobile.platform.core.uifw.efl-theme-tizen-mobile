PREFIX ?= /usr

all:
	cd themes && make

install: 
	cd themes && make $@

uninstall:
	cd themes && make $@

clean:
	cd themes && make $@

distclean: clean

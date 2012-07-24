PREFIX ?= /usr

all:
	cd themes && make

install: all
	cd themes && make $@

uninstall:
	cd themes && make $@

clean:
	cd themes && make $@

distclean: clean

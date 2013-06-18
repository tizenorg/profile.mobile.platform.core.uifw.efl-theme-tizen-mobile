PREFIX ?= /usr

all:
	cp themes/tizen.edc themes/light.edc
	cp themes/tizen.edc themes/dark.edc
	cd themes && make

install: 
	cd themes && make $@
	rm -rf themes/light.edc themes/dark.edc

uninstall:
	cd themes && make $@

clean:
	cd themes && make $@

distclean: clean

PREFIX ?= /usr
INSTALL=install -c
themedir=$(DESTDIR)$(PREFIX)/share/elementary/themes

all: nbeat nbeat-blue nbeat-purple nbeat-green nbeat-black
	echo $(escaped_prefix)

.SUFFIXES: .edc .edj
.edc.edj:
	cp ./inc/$(@:.edj=-inc.edc) ./inc/tmp-inc.edc
	#edje_cc -v -id ./images/$(@:.edj=) -sd ./sounds -fd ../objects $(@:.edj=.edc) # commented -sd ./sounds
	edje_cc -v -id ./images/$(@:.edj=) -fd ../objects $(@:.edj=.edc)
	rm ./inc/tmp-inc.edc

nbeat: nbeat.edj
nbeat-blue: nbeat-blue.edj
nbeat-purple: nbeat-purple.edj
nbeat-green: nbeat-green.edj
nbeat-black: nbeat-black.edj

clean:
	rm -f *.edj

install:
	mkdir -p $(themedir)
	$(INSTALL) nbeat*.edj $(themedir)

distclean: clean

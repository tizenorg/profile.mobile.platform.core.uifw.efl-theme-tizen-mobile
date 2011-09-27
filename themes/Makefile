PREFIX ?= /usr
INSTALL=install -c
themedir=$(DESTDIR)$(PREFIX)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v

all: nbeat nbeat-black nbeat-hd nbeat-black-hd
	echo $(escaped_prefix)

.SUFFIXES: .edc .edj
.edc.edj:
	cp ./inc/$(@:.edj=-inc.edc) ./inc/tmp-inc.edc
	#edje_cc -v -id ./images/$(@:.edj=) -sd ./sounds -fd ../objects $(@:.edj=.edc) # commented -sd ./sounds
	edje_cc $(EDJE_FLAGS_$(V)) -id ./images/$(@:.edj=) -fd ../objects $(@:.edj=.edc)
	rm ./inc/tmp-inc.edc

nbeat: nbeat.edj
nbeat-black: nbeat-black.edj
nbeat-hd: nbeat-hd.edj
nbeat-black-hd: nbeat-black-hd.edj

clean:
	rm -f *.edj

install:
	mkdir -p $(themedir)
	$(INSTALL) nbeat*.edj $(themedir)

distclean: clean

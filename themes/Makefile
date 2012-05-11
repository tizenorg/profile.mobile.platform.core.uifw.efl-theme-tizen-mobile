PREFIX ?= /usr
INSTALL=install -c
themedir=$(DESTDIR)$(PREFIX)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v

all: tizen-hd tizen-black-hd
	echo $(escaped_prefix)

.SUFFIXES: .edc .edj
.edc.edj:
	cp ./inc/$(@:.edj=-inc.edc) ./inc/tmp-inc.edc
	edje_cc $(EDJE_FLAGS_$(V)) -id ./images/$(@:.edj=) -sd ./sounds -fd ../objects $(@:.edj=.edc)
	rm ./inc/tmp-inc.edc

tizen-hd: tizen-hd.edj
tizen-black-hd: tizen-black-hd.edj

clean:
	rm -f *.edj

install:
	mkdir -p $(themedir)
	$(INSTALL) tizen*.edj $(themedir)

distclean: clean

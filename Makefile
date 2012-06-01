PREFIX ?= /usr
INSTALL_DIR=$(DESTDIR)/opt/var/efl-theme-tizen-edc

INSTALL=install -c

$(warning $(CC) )

all: themes
	echo $(escaped_prefix)

themes: copy_edc	
	cd themes && make
	rm themes/tizen-*.edc

install_themes:
	cd themes && make install

install_edc:
	mkdir -p $(INSTALL_DIR)
	cp themes/tizen.edc themes/widgets $(INSTALL_DIR) -r

install: install_themes install_edc

copy_edc:
	cp themes/tizen.edc themes/tizen-hd.edc

tizen-hd:
	cp themes/tizen.edc themes/$@.edc
	cd themes && make $@
	rm themes/tizen-*.edc

clean:
	rm -rf themes/*.edj
	rm -rf themes/tizen-*.edc

distclean: clean

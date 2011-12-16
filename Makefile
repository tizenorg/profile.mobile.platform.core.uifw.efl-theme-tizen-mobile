PREFIX ?= /usr

INSTALL=install -c

$(warning $(CC) )

all: themes
	echo $(escaped_prefix)

themes: copy_edc	
	cd themes && make
	rm themes/tizen-*.edc

install_themes:
	cd themes && make install
	
install: install_themes

copy_edc:
	cp themes/tizen.edc themes/tizen-black.edc
	cp themes/tizen.edc themes/tizen-hd.edc
	cp themes/tizen.edc themes/tizen-black-hd.edc

tizen:
	cd themes && make $@

tizen-black:
	cp themes/tizen.edc themes/$@.edc
	cd themes && make $@
	rm themes/tizen-*.edc

tizen-hd:
	cp themes/tizen.edc themes/$@.edc
	cd themes && make $@
	rm themes/tizen-*.edc

tizen-black-hd:
	cp themes/tizen.edc themes/$@.edc
	cd themes && make $@
	rm themes/tizen-*.edc

clean:
	rm -rf themes/*.edj
	rm -rf themes/tizen-*.edc

distclean: clean

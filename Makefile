PREFIX ?= /usr

INSTALL=install -c

$(warning $(CC) )

all: themes
	echo $(escaped_prefix)

themes: copy_edc	
	cd themes && make
	rm themes/nbeat-*.edc

install_themes:
	cd themes && make install
	
install: install_themes

copy_edc:
	cp themes/nbeat.edc themes/nbeat-black.edc
	cp themes/nbeat.edc themes/nbeat-hd.edc

nbeat:
	cd themes && make $@

nbeat-black:
	cp themes/nbeat.edc themes/$@.edc
	cd themes && make $@
	rm themes/nbeat-*.edc

nbeat-hd:
	cp themes/nbeat.edc themes/$@.edc
	cd themes && make $@
	rm themes/nbeat-*.edc

clean:
	rm -rf themes/*.edj
	rm -rf themes/nbeat-*.edc

distclean: clean

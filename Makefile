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
	cp themes/nbeat.edc themes/nbeat-blue.edc
	cp themes/nbeat.edc themes/nbeat-purple.edc
	cp themes/nbeat.edc themes/nbeat-green.edc
	cp themes/nbeat.edc themes/nbeat-black.edc

nbeat:
	cd themes && make $@ 

nbeat-blue nbeat-purple nbeat-green nbeat-black: 
	cp themes/nbeat.edc themes/$@.edc
	cd themes && make $@ 
	rm themes/nbeat-*.edc

clean:
	rm -rf themes/*.edj
	rm -rf themes/nbeat-*.edc

distclean: clean

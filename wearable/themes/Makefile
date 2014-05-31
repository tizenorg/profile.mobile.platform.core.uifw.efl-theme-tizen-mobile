PREFIX ?= /usr
INSTALL=install -c
EDC_DIR=$(DESTDIR)/opt/var/efl-theme-tizen-edc
THEME_DIR=$(DESTDIR)$(PREFIX)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
SRC=tizen

all: default.edj
	echo  $(escaped_prefix)

.SUFFIXES: .edc .edj
.edc.edj:
	perl -pi -e 's/TIZEN_TMP_INC/".\/inc\/theme_$*_inc.edc"/g' $*.edc
	edje_cc $(EDJE_FLAGS_$(V))\
	 -id ./images/$(@:.edj=)\
	 -id ./images/$(@:.edj=)/Action\ bar\
	 -id ./images/$(@:.edj=)/Progress\
	 -id ./images/$(@:.edj=)/TimePicker\
	 -id ./images/$(@:.edj=)/slider\
	 -id ./images/$(@:.edj=)/Body\
	 -id ./images/$(@:.edj=)/Controller_icon\
	 -id ./images/$(@:.edj=)/List\ Edge\ Glow\ Effect\
	 -id ./images/$(@:.edj=)/Overscrolling\
	 -id ./images/$(@:.edj=)/Overscrolling/Top\
	 -id ./images/$(@:.edj=)/Overscrolling/Bottom\
	 -id ./images/$(@:.edj=)/Overscrolling/Left\
	 -id ./images/$(@:.edj=)/Overscrolling/Right\
	 -id ./images/$(@:.edj=)/Popup\
	 -id ./images/$(@:.edj=)/Scroll\
	 -id ./images/$(@:.edj=)/VI\
	 -id ./images/$(@:.edj=)/temp\
	 -id ./images/$(@:.edj=)/temp/Copy_Paste\
	 -id ./images/$(@:.edj=)/temp/swipe\
	 -id ./images/$(@:.edj=)/Apps\
	 -id ./images/$(@:.edj=)/Apps/Call\
	 -id ./images/$(@:.edj=)/Apps/Call/call\ menu\
	 -id ./images/$(@:.edj=)/Apps/Music_player\
	 -id ./images/$(@:.edj=)/Apps/Email\
	 -id ./images/$(@:.edj=)/Apps/Gallery\
	 -id ./images/$(@:.edj=)/Apps/Logs\
	 -id ./images/$(@:.edj=)/Apps/Widget_schedule\
	 -sd ./sounds\
	 -id ./apps/elm_demo_tizen/images/\
	 -sd ./apps/elm_demo_tizen/sounds/\
	 $*.edc $(SRC)-$*.edj

clean:
	rm -f *.edj

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) tizen*.edj $(THEME_DIR)
	mkdir -p $(EDC_DIR)
	cp -r $(SRC).edc widgets $(EDC_DIR)
	rm -rf themes/$*.edc

uninstall:
	rm -f $(EDC_DIR)/$(SRC.edc) && rm -rf $(EDC_DIR)/widgets

distclean: clean

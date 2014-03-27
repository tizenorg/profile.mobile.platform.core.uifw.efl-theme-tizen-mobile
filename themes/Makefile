PREFIX ?= /usr
INSTALL=install -c
EDC_DIR=$(DESTDIR)/opt/var/efl-theme-tizen-edc
THEME_DIR=$(DESTDIR)$(PREFIX)/share/elementary/themes
TABLE_DIR=$(DESTDIR)$(PREFIX)/share/elementary/themes/tables
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
SRC=tizen
TARGET=HD

all: light dark InputColors
	echo  $(escaped_prefix)

.SUFFIXES: .edc .edj
.edc.edj:
	perl -pi -e 's/TIZEN_TMP_INC/".\/inc\/$(SRC)-$*-inc.edc"/g' $*.edc
	edje_cc $(EDJE_FLAGS_$(V))\
	 -id ./images/$(TARGET)/$(@:.edj=)\
	 -id ./images/$(TARGET)/$(@:.edj=)/Content_views\
	 -id ./images/$(TARGET)/$(@:.edj=)/Content_views/Gengrid\
	 -id ./images/$(TARGET)/$(@:.edj=)/Controls\
	 -id ./images/$(TARGET)/$(@:.edj=)/Controls/00_Progress_circle_bg\
	 -id ./images/$(TARGET)/$(@:.edj=)/Controls/Button\
	 -id ./images/$(TARGET)/$(@:.edj=)/Controls/Check_box\
	 -id ./images/$(TARGET)/$(@:.edj=)/Controls/Radio_button\
	 -id ./images/$(TARGET)/$(@:.edj=)/Copy_Paste\
	 -id ./images/$(TARGET)/$(@:.edj=)/Focus\
	 -id ./images/$(TARGET)/$(@:.edj=)/GUI_Style_Guide\
	 -id ./images/$(TARGET)/$(@:.edj=)/Indicator\
	 -id ./images/$(TARGET)/$(@:.edj=)/Map\
	 -id ./images/$(TARGET)/$(@:.edj=)/Naviframe\
	 -id ./images/$(TARGET)/$(@:.edj=)/Naviframe/Icon\
	 -id ./images/$(TARGET)/$(@:.edj=)/Overscrolling\
	 -id ./images/$(TARGET)/$(@:.edj=)/Overscrolling/Top\
	 -id ./images/$(TARGET)/$(@:.edj=)/Overscrolling/Bottom\
	 -id ./images/$(TARGET)/$(@:.edj=)/Overscrolling/Left\
	 -id ./images/$(TARGET)/$(@:.edj=)/Overscrolling/Right\
	 -id ./images/$(TARGET)/$(@:.edj=)/Popup\
	 -id ./images/$(TARGET)/$(@:.edj=)/Process\
	 -id ./images/$(TARGET)/$(@:.edj=)/Screen_Reader\
	 -sd ./sounds -fd ../objects \
	 $*.edc $(SRC)-$(TARGET)-$@

light: light.edj
dark: dark.edj

InputColors:
	eet -e tables/$@.cfg config tables/$@.src 1

clean:
	rm -f *.edj
	rm -f table/*.cfg

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) tizen*.edj $(THEME_DIR)
	mkdir -p $(TABLE_DIR)
	$(INSTALL) tables/*.cfg $(TABLE_DIR)
	$(INSTALL) tables/*.xml $(TABLE_DIR)
	mkdir -p $(EDC_DIR)
	cp -r $(SRC).edc widgets $(EDC_DIR)

uninstall:
	rm -f $(EDC_DIR)/$(SRC.edc) && rm -rf $(EDC_DIR)/widgets

distclean: clean

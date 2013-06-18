PREFIX ?= /usr
INSTALL=install -c
EDC_DIR=$(DESTDIR)/opt/var/efl-theme-tizen-edc
THEME_DIR=$(DESTDIR)$(PREFIX)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
TMP_INC=tmp-inc.edc
SRC=tizen
TARGET=HD

all: light dark
	echo  $(escaped_prefix)

.SUFFIXES: .edc .edj
.edc.edj:
	echo $(SRC)
	echo $(EDJE_FLAGS_$(V))
	echo "/inc/$(@:.edj=)"
	echo $(TARGET)/$(SRC)-$(TARGET)-$(@:.edj=)
	cp -f ./inc/$(SRC)-$(@:.edj=-inc.edc) ./inc/$(TMP_INC)
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
	 -id ./images/$(TARGET)/$(@:.edj=)/Map\
	 -id ./images/$(TARGET)/$(@:.edj=)/Naviframe\
	 -id ./images/$(TARGET)/$(@:.edj=)/Naviframe/Icon\
	 -id ./images/$(TARGET)/$(@:.edj=)/Overscrolling\
	 -id ./images/$(TARGET)/$(@:.edj=)/Popup\
	 -id ./images/$(TARGET)/$(@:.edj=)/Process\
	 -id ./images/$(TARGET)/$(@:.edj=)/Screen_Reader\
	 -sd ./sounds -fd ../objects $(SRC).edc \
	 $(SRC)-$(TARGET)-$@
	rm -rf ./inc/tmp-inc.edc

light: light.edj
dark: dark.edj

clean:
	rm -f *.edj

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) tizen*.edj $(THEME_DIR)
	mkdir -p $(EDC_DIR)
	cp -r $(SRC).edc widgets $(EDC_DIR)

uninstall:
	rm -f $(EDC_DIR)/$(SRC.edc) && rm -rf $(EDC_DIR)/widgets

distclean: clean
	      ~

PREFIX ?= /usr
INSTALL=install -c
EDC_DIR=$(DESTDIR)/opt/var/efl-theme-tizen-edc
THEME_DIR=$(DESTDIR)$(PREFIX)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
SRC=tizen
TARGET=tizen.edj

.SUFFIXES: .edc .edj
.edc.edj:
	perl -pi -e 's/TIZEN_TMP_INC/".\/inc\/$(SRC)-inc.edc"/g' $(SRC).edc
	edje_cc $(EDJE_FLAGS_$(V))\
	 -id ./images/\
	 -id ./images/Content_views\
	 -id ./images/Content_views/Gengrid\
	 -id ./images/Controls\
	 -id ./images/Controls/00_Progress_circle_bg\
	 -id ./images/Controls/Button\
	 -id ./images/Controls/Check_box\
	 -id ./images/Controls/Radio_button\
	 -id ./images/Copy_Paste\
	 -id ./images/Focus\
	 -id ./images/GUI_Style_Guide\
	 -id ./images/Indicator\
	 -id ./images/Map\
	 -id ./images/Naviframe\
	 -id ./images/Naviframe/Icon\
	 -id ./images/Overscrolling\
	 -id ./images/Overscrolling/Top\
	 -id ./images/Overscrolling/Bottom\
	 -id ./images/Overscrolling/Left\
	 -id ./images/Overscrolling/Right\
	 -id ./images/Popup\
	 -id ./images/Process\
	 -id ./images/Screen_Reader\
	 -sd ./sounds -fd ../objects \
	 $(SRC).edc $@

$(SRC): tizen.edj

clean:
	rm -f *.edj

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) $(TARGET) $(THEME_DIR)
	mkdir -p $(EDC_DIR)
	cp -r $(SRC).edc widgets $(EDC_DIR)

uninstall:
	rm -f $(EDC_DIR)/$(SRC.edc) && rm -rf $(EDC_DIR)/widgets

distclean: clean

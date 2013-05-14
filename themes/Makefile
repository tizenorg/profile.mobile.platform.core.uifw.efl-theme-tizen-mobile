TARGET=tizen-hd.edj

PREFIX?=/usr
INSTALL=install -c
EDC_DIR=$(DESTDIR)/opt/var/efl-theme-tizen-edc
THEME_DIR=$(DESTDIR)$(PREFIX)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
TMP_INC=tmp-inc.edc
SRC=tizen.edc

all: $(TARGET)

$(TARGET): clean
	cp -f ./inc/$(@:.edj=-inc.edc) ./inc/$(TMP_INC)
	edje_cc $(EDJE_FLAGS_$(V))\
	 -id ./images/$(@:.edj=)\
	 -id ./images/$(@:.edj=)/Content_views\
	 -id ./images/$(@:.edj=)/Content_views/Gengrid\
	 -id ./images/$(@:.edj=)/Controls\
	 -id ./images/$(@:.edj=)/Controls/00_Progress_circle_bg\
	 -id ./images/$(@:.edj=)/Controls/Button\
	 -id ./images/$(@:.edj=)/Controls/Check_box\
	 -id ./images/$(@:.edj=)/Controls/Radio_button\
	 -id ./images/$(@:.edj=)/Copy_Paste\
	 -id ./images/$(@:.edj=)/Focus\
	 -id ./images/$(@:.edj=)/GUI_Style_Guide\
	 -id ./images/$(@:.edj=)/Map\
	 -id ./images/$(@:.edj=)/Naviframe\
	 -id ./images/$(@:.edj=)/Naviframe/Icon\
	 -id ./images/$(@:.edj=)/Others\
	 -id ./images/$(@:.edj=)/Overscrolling\
	 -id ./images/$(@:.edj=)/Popup\
	 -id ./images/$(@:.edj=)/Process\
	 -sd ./sounds -fd ../objects $(SRC) $@

clean:
	rm -f *.edj
	rm -f ./inc/$(TMP_INC)

distclean: clean

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) $(TARGET) $(THEME_DIR)
	mkdir -p $(EDC_DIR)
	cp -r $(SRC) widgets $(EDC_DIR)

uninstall:
	rm -f $(THEME_DIR)/$(TARGET)
	rm -f $(EDC_DIR)/$(SRC) && rm -rf $(EDC_DIR)/widgets

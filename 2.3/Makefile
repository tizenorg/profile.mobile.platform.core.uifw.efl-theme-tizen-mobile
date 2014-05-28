PREFIX ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)$(PREFIX)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
SRC=tizen
SIZE=HD HVGA

all:
	for s in $(SIZE); do \
		cp $(SRC).edc $(SRC)-$(TARGET)-$$s.edc; \
		perl -pi -e "s/TIZEN_TMP_INC/\"$$s-inc.edc\"/g" $(SRC)-$(TARGET)-$$s.edc; \
		edje_cc $(EDJE_FLAGS_$(V))\
		-id ./$$s/images/\
		-id ./$$s/images/Content_views\
		-id ./$$s/images/Content_views/Gengrid\
		-id ./$$s/images/Controls\
		-id ./$$s/images/Controls/00_Progress_circle_bg\
		-id ./$$s/images/Controls/Button\
		-id ./$$s/images/Controls/Check_box\
		-id ./$$s/images/Controls/Radio_button\
		-id ./$$s/images/Copy_Paste\
		-id ./$$s/images/Focus\
		-id ./$$s/images/GUI_Style_Guide\
		-id ./$$s/images/Indicator\
		-id ./$$s/images/Map\
		-id ./$$s/images/Naviframe\
		-id ./$$s/images/Naviframe/Icon\
		-id ./$$s/images/Overscrolling\
		-id ./$$s/images/Overscrolling/Top\
		-id ./$$s/images/Overscrolling/Bottom\
		-id ./$$s/images/Overscrolling/Left\
		-id ./$$s/images/Overscrolling/Right\
		-id ./$$s/images/Popup\
		-id ./$$s/images/Process\
		-id ./$$s/images/Screen_Reader\
		-sd ./$$s/sounds -fd ../objects \
		$(SRC)-$(TARGET)-$$s.edc $(SRC)-$(TARGET)-$$s.edj; \
	done

clean:
	for s in $(SIZE); do \
		rm -rf $(SRC)-$(TARGET)-$$s.*; \
	done

install:
	mkdir -p $(THEME_DIR)
	for s in $(SIZE); do \
		$(INSTALL) $(SRC)-$(TARGET)-$$s.edj $(THEME_DIR); \
	done

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean

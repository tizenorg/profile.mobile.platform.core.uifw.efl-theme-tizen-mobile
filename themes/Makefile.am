prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
EDJE_FLAGS =
SRC=tizen

all:
	edje_cc $(EDJE_FLAGS) $(EDJE_FLAGS_$(V)) \
		-id ./SMALL/images/ \
		-id ./SMALL/images/Activity_indicator/ \
		-id ./SMALL/images/Activity_indicator/large \
		-id ./SMALL/images/Activity_indicator/medium \
		-id ./SMALL/images/Activity_indicator/small \
		-id ./SMALL/images/Content_views \
		-id ./SMALL/images/Controls \
		-id ./SMALL/images/Copy_Paste \
		-id ./SMALL/images/Emoticon \
		-id ./SMALL/images/Navigation_elements \
		-id ./SMALL/images/Popups \
		-id ./SMALL/images/Indicator \
		-sd ./SMALL/sounds -fd ../objects \
		-id ./MIDDLE/images/ \
		-id ./MIDDLE/images/Activity_indicator/ \
		-id ./MIDDLE/images/Activity_indicator/large \
		-id ./MIDDLE/images/Activity_indicator/medium \
		-id ./MIDDLE/images/Activity_indicator/small \
		-id ./MIDDLE/images/Content_views \
		-id ./MIDDLE/images/Controls \
		-id ./MIDDLE/images/Copy_Paste \
		-id ./MIDDLE/images/Emoticon \
		-id ./MIDDLE/images/Navigation_elements \
		-id ./MIDDLE/images/Popups \
		-sd ./MIDDLE/sounds -fd ../objects \
	$(SRC).edc $(SRC)-mobile.edj;
	edje_cc $(EDJE_FLAGS_$(V)) \
		-id default/images -sd default/sounds -fd ../objects \
		-id ./SMALL/images/\
		-id ./SMALL/images/Activity_indicator/\
		-id ./SMALL/images/Activity_indicator/large\
		-id ./SMALL/images/Activity_indicator/medium\
		-id ./SMALL/images/Activity_indicator/small\
		-id ./SMALL/images/Content_views\
		-id ./SMALL/images/Controls\
		-id ./SMALL/images/Copy_Paste\
		-id ./SMALL/images/Emoticon\
		-id ./SMALL/images/Navigation_elements\
		-id ./SMALL/images/Popups\
		default.edc default.edj


clean:
	rm -rf $(SRC)-mobile.edj;
	rm -rf default.edj;

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) $(SRC)-mobile.edj $(THEME_DIR);
	$(INSTALL) default.edj $(THEME_DIR);

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean

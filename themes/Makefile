prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
EDJE_FLAGS = -no-save
SRC=tizen

all:
	edje_cc $(EDJE_FLAGS) $(EDJE_FLAGS_$(V))\
	-id ./WVGA/images/\
	-id ./WVGA/images/Activity_indicator/\
	-id ./WVGA/images/Activity_indicator/large\
	-id ./WVGA/images/Activity_indicator/medium\
	-id ./WVGA/images/Activity_indicator/small\
	-id ./WVGA/images/Content_views\
	-id ./WVGA/images/Controls\
	-id ./WVGA/images/Copy_Paste\
	-id ./WVGA/images/Emoticon\
	-id ./WVGA/images/Navigation_elements\
	-id ./WVGA/images/Popups\
	-id ./WVGA/images/Indicator\
	-sd ./WVGA/sounds -fd ../objects \
	-id ./HD/images/\
	-id ./HD/images/Activity_indicator/\
	-id ./HD/images/Activity_indicator/large\
	-id ./HD/images/Activity_indicator/medium\
	-id ./HD/images/Activity_indicator/small\
	-id ./HD/images/Content_views\
	-id ./HD/images/Controls\
	-id ./HD/images/Copy_Paste\
	-id ./HD/images/Emoticon\
	-id ./HD/images/Navigation_elements\
	-id ./HD/images/Popups\
	-sd ./HD/sounds -fd ../objects \
	$(SRC).edc $(SRC).edj;

clean:
	rm -rf $(SRC).*;

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) $(SRC).edj $(THEME_DIR);

uninstall:
	rm -rf $(THEME_DIR)

distclean: clean

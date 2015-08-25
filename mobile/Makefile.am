prefix ?= /usr
INSTALL=install -c
THEME_DIR=$(DESTDIR)/$(prefix)/share/elementary/themes
EDJE_FLAGS_VERBOSE_ =
EDJE_FLAGS_VERBOSE_0 =
EDJE_FLAGS_VERBOSE_1 = -v
EDJE_FLAGS =
SRC=efl-theme-tizen-mobile
DEFAULT_SRC=default-mobile

all:
	edje_cc $(EDJE_FLAGS) $(EDJE_FLAGS_$(V)) \
		-id ./HD/images/\
		-id ./HD/images/Navigation_elements\
		-id ./HD/images/Presentation_views\
		-id ./HD/images/User_Input_Elements\
		-id ./HD/images/Assist_Views\
		-id ./HD/images/Copy_Paste\
		-id ./HD/images/Emoticon\
		-id ./HD/images/Old\
		-sd ./HD/sounds -fd ../objects \
		$(SRC).edc $(SRC).edj;
	edje_cc $(EDJE_FLAGS_$(V)) \
		-id default/images/tizen-hd -sd default/sounds -fd ../objects \
		-id ./HD/images/\
		-id ./HD/images/Navigation_elements\
		-id ./HD/images/Presentation_views\
		-id ./HD/images/User_Input_Elements\
		-id ./HD/images/Assist_Views\
		-id ./HD/images/Copy_Paste\
		-id ./HD/images/Emoticon\
		-id ./HD/images/Old\
		$(DEFAULT_SRC).edc $(DEFAULT_SRC).edj;


clean:
	rm -rf $(SRC).edj;
	rm -rf $(DEFAULT_SRC).edj;

install:
	mkdir -p $(THEME_DIR)
	$(INSTALL) $(SRC).edj $(THEME_DIR);
	$(INSTALL) $(DEFAULT_SRC).edj $(THEME_DIR);

uninstall:
	rm -rf $(THEME_DIR)/

distclean: clean

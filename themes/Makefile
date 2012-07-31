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
	edje_cc $(EDJE_FLAGS_$(V)) -id ./images/$(@:.edj=) -sd ./sounds -fd ../objects $(SRC) $@

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

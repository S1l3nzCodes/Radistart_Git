
all:
	cd sipgen
	$(MAKE)
	@cd ..
	cd siplib
	$(MAKE)
	@cd ..

install:
	cd sipgen
	$(MAKE) install
	@cd ..
	cd siplib
	$(MAKE) install
	@cd ..
	@if not exist c:\python27\Lib\site-packages mkdir c:\python27\Lib\site-packages
	copy /y sipconfig.py c:\python27\Lib\site-packages\sipconfig.py
	copy /y E:\sip-4.15.4\sipdistutils.py c:\python27\Lib\site-packages\sipdistutils.py

clean:
	cd sipgen
	$(MAKE) clean
	@cd ..
	cd siplib
	$(MAKE) clean
	@cd ..

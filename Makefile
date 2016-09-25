serve:
	cd docs && python3 -m http.server

clean:
	rm -rf docs/*

build: clean
	mkdir -p docs
	python3 build.py
	cp -r css docs/
	echo votecuz.com > docs/CNAME

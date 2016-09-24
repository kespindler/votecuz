serve:
	cd docs && python3 -m http.server

clean:
	rm -rf docs/*

build: clean
	mkdir -p docs
	python3 build.py
	echo votecuz.com > docs/CNAME


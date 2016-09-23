serve:
	cd dist && python3 -m http.server

clean:
	rm -rf dist/*

build: clean
	mkdir -p dist
	python3 build.py


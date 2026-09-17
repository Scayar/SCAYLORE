.PHONY: brand check

brand:
	python3 scripts/build_brand_assets.py

check:
	python3 scripts/verify_brand.py

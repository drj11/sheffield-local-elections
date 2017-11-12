all: out/2016locals.csv out/2016turnout.csv

out/2016locals.csv:
	bin/wards.py

out/2016turnout.csv:
	bin/turnout.py

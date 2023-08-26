.PHONY: all clean clean_after thesis open clc

all: clc clean thesis clean_after open

clc:
	clear

thesis:
	lualatex -shell-escape thesis
	biber thesis
	lualatex -shell-escape thesis
	lualatex -shell-escape thesis

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml

clean_after:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml

open:
	open thesis.pdf
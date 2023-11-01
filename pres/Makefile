.PHONY: all clean clean_after build open clc convert

all: clc clean convert build clean_after open

clc:
	clear

build:
	pdflatex -shell-escape pres
	bibtex pres
	pdflatex -shell-escape pres
	pdflatex -shell-escape pres

convert:
	python convert.py

clean:
	rm -f *.bbl *.blg *.log *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml *.snm *.nav *.vrb *.pyg *.listing

clean_after:
	rm -f *.bbl *.blg *.log *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml *.snm *.nav *.vrb *.pyg *.listing

open:
	open pres.pdf
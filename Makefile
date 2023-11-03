.PHONY: all clean clean_after thesis open clc commit

all: clc clean thesis open commit

clc:
	clear

thesis:
	lualatex -shell-escape thesis
	biber thesis
	lualatex -shell-escape thesis
	lualatex -shell-escape thesis

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml *.snm *.nav

clean_after:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.idx *.lot *.lof *.fls *.fdb* *.bcf *.lol *.run.xml *.snm *.nav

commit:
	git add --all
	git commit -m "Update"
	git push origin

open:
	open thesis.pdf
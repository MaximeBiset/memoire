
all: 
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex

op: 
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex
	evince main.pdf

lecture: 
	pdflatex main_lecture.tex
	evince main_lecture.pdf

clean:
	rm *.log *.aux *.bbl *.blg *.dvi *.synctex.gz *.out *.pdf | true


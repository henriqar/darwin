
DARWINDIR=darwin.opt
EXECDIR=darwin.exec
CC = gcc -lm 

all: sanity

sanity: sanity.c
	$(CC) $^ -o darwin.opt/sanity 

clean: sanity
	rm -f $(DARWINDIR)/sanity darwin.log output.txt
	rm -rf $(EXECDIR)


DARWINDIR=darwin.opt
EXECDIR=darwin.exec
CC = gcc

all: sanity

sanity: sanity.c
	$(CC) $^ -o $(DARWINDIR)/sanity -lm

clean: sanity
	rm -f $(DARWINDIR)/sanity darwin.log output.txt
	rm -rf $(EXECDIR)

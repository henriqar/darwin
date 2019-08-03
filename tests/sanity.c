
#include<math.h>
#include<limits.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>

double cos_cos(double x, double y) {

  double result = 0.0;

  result = cos(x)*cos(y) + sin(y)*sin(x) + 2;
  /* result = cos(x)*cos(y)*exp((-pow(x, 2))*(-pow(y, 2))) + 20; */

  return result;
}

int main(int argc, char **argv) {

  FILE *fp;
  double x, y, result;
  int i;
  char *name;

  name = (char*)malloc(500*sizeof(char));

  printf("argc %d\n", argc);
  /* printf("aqui-5000"); */
  printf("argvs:\n");
  for (i = 0; i < argc; i++) {
    printf("%s\n", argv[i]);
  }
    /* printf("aqui-5000"); */

    /* printf("aqui-1"); */
  if (argc < 5) {
    return (double)INT_MAX;
  } 

    /* printf("aqui0"); */
  x = atof(argv[2]);
  y = atof(argv[4]);

  result = cos_cos(x, y);

  if (argc > 5) {
    strcpy(name, argv[6]);
    strcat(name, "/output.txt");
    fp = fopen(name, "w+");
    printf("%s\n", name);
  }
  else {
    fp = fopen("output.txt", "w+");
  }
  fprintf(fp, "%f\n", result);
  return 0;
  fclose(fp);

  return 0;
}


#include<math.h>
#include<limits.h>
#include<stdlib.h>
#include<stdio.h>

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

  printf("argc %d\n", argc);

  printf("argvs:\n");
  for (i = 0; i < argc; ++i) {
    printf("%s\n", argv[i]);
  }

  if (argc < 5) {
    return (double)INT_MAX;
  } 

  x = atof(argv[2]);
  y = atof(argv[4]);

  result = cos_cos(x, y);

  fp = fopen("output.txt", "w+");
  fprintf(fp, "%f", result);
  fclose(fp);

  return 0;
}

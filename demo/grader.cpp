// grader.cpp
#include <bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for (int i = (a); i <= (b); ++i)

int a, b;
int main() {
  FILE *inf = fopen("in.txt", "r");
  fscanf(inf, "%d%d", &a, &b);
  fclose(inf);

  assert(a <= b);

  printf("%d\n", b);
  fflush(stdout);

  FOR(_, 1, 30) {
    char x[5];
    int y;
    scanf("%s%d", x, &y);
    fprintf(stderr, "%s %d\n", x, y);
    if (x[0] == '?') {
      printf("%d\n", a >= y);
      fflush(stdout);
      fprintf(stderr, "%d\n", a >= y);
    } else {
      assert(x[0] == '!');
      if (y == a) {
        fprintf(stderr, "AC\n");
      } else {
        fprintf(stderr, "WA\n");
      }
      return 0;
    }
  }

  fprintf(stderr, "WA\n");
  return 0;
}
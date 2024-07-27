// problem.cpp
#include <bits/stdc++.h>
using namespace std;

bool check(int x) {
  printf("? %d\n", x); // check if ? >= x
  fflush(stdout);
  scanf("%d", &x);
  return x == 1;
}
int main() {
  int n;
  scanf("%d", &n);
  int l = 1, r = n, mid;
  while (l < r)
    mid = (l + r + 1) >> 1, check(mid) ? l = mid : r = mid - 1;
  printf("! %d\n", l);
  return 0;
}
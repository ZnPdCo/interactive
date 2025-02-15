#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[]) {
    setName("Interactor A+B");
    registerInteraction(argc, argv);

    rnd.setSeed(time(NULL));
    int a = rnd.next(1000);
    int b = rnd.next(1000);
    // writes query to the solution, endl makes flush
    cout << a << " " << b << endl;
    int ans;
    cin >> ans;
    if (a + b == ans)
        quitf(_ok, "!");
    else
        quitf(_wa, "?");
}

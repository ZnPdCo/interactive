# interactive

一个多平台支持的 stdio 交互题调试工具

可以在 Releases 页面下载预编译好的可执行文件（当前仅有 Windows，欢迎贡献），将其添加到环境变量中便于使用。

以猜数游戏为例，使用方法：

```bash
$ cd demo
$ g++ ./problem.cpp -o ./problem
$ g++ ./grader.cpp -o ./grader
$ python ../interactive.py ./problem ./grader
./grader: 514
./problem: ? 258
./grader: 0     
./problem: ? 129
./grader: 0     
./problem: ? 65 
./grader: 1
./problem: ? 97
./grader: 1
./problem: ? 113
./grader: 1
./problem: ? 121
./grader: 0
./problem: ? 117
./grader: 0
./problem: ? 115
./grader: 0
./problem: ? 114
./grader: 1
./problem: ! 114
AC
$ 
```

使用了 testlib 的交互库也是可以的：

```
$ cd testlib_demo
$ g++ ./problem.cpp -o ./problem
$ g++ ./grader.cpp -o ./grader
$ python ../interactive.py ./problem "./grader in.txt out.txt"
./grader in.txt out.txt: 39 600
./problem: 639
ok !
$ 
```

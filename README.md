# interactive

一个多平台支持的 stdio 交互题调试工具

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

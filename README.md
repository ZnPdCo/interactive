# interactive

一个多平台支持的 stdio 交互题调试工具

使用方法：

```bash
$ cd demo
$ g++ ./problem.cpp -o ./problem
$ g++ ./grader.cpp -o ./grader
$ python ../interactive.py ./problem ./grader
? 258
0    
? 129
0    
? 65 
1    
? 97 
1    
? 113
1    
? 121
0
? 117
0
? 115
0
? 114
1
! 114
AC
$ 
```

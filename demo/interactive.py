import sys
import subprocess
from threading import Thread

def judger(argv):
    if len(argv) != 3:
        print(f"Usage: {argv[0]} [command1] [command2]", file=sys.stderr)
        return 1
    
    command1 = argv[1]
    command2 = argv[2]

    def run_command(p1, p2):
        while True:
            line = p2.stdout.readline()
            if not line:
                break
            p1.stdin.write(line)
            p1.stdin.flush()

    p1 = subprocess.Popen(command1, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(command2, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    t1 = Thread(target=run_command, args=(p1, p2))
    t2 = Thread(target=run_command, args=(p2, p1))

    t1.start()
    t2.start()

    p1.wait()
    p2.wait()

    return 0

if __name__ == "__main__":
    sys.exit(judger(sys.argv))

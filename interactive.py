import sys
import subprocess
from threading import Thread, Lock

stop = False

def judger(argv):
    if len(argv) != 3:
        print(f"Usage: {argv[0]} [command1] [command2]", file=sys.stderr)
        return 1
    
    command1 = argv[1]
    command2 = argv[2]

    def run_command(name, p1, p2):
        global stop
        while True:
            lock = Lock()
            lock.acquire()
            line = p1.stdout.readline()
            if not line or stop:
                stop = True
                lock.release()
                break
            print(name + ": " + line.decode(), end="")
            p2.stdin.write(line)
            p2.stdin.flush()
            lock.release()

    p1 = subprocess.Popen(command1, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(command2, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    t1 = Thread(target=run_command, args=(command1, p1, p2))
    t2 = Thread(target=run_command, args=(command2, p2, p1))

    t1.start()
    t2.start()

    p1.wait()
    p2.wait()

    return 0

if __name__ == "__main__":
    sys.exit(judger(sys.argv))

import get_info
import time

if __name__ == '__main__':
    get_info.single_release('https://api.github.com/repos/tensorflow/tensorflow/releases', 1)
    time.sleep(5)
    get_info.single_release('https://api.github.com/repos/tensorflow/tensorflow/releases', 2)

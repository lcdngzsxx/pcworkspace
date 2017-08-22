import time

__author__ = 'herexu'
__copyright__ = 'copyright 2017-2018'


def worker(n):
    print('start at :{}'.format(time.ctime()))
    time.sleep(n)
    print('end at : {}'.format(time.ctime()))


def main():
    print('main satr at : <{}>'.format(time.ctime()))
    worker(4)
    worker(2)
    print('main end at : <{}>'.format(time.ctime()))


if __name__ == '__main__':
    main()

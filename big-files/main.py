import time
import os
import sys
import argparse


FILE_NAME = 'int_list.txt'

def create_big_file(size=10):
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

    big_list = list(range(1,size + 2))

    with open(FILE_NAME, 'wt') as f:
        f.write('\n'.join(str(el) for el in big_list))

def read_big_file():
    big_list_as_dict = {}
    with open(FILE_NAME) as f:
        for i, el in enumerate(f):
            big_list_as_dict[i] = el.strip()

    print(big_list_as_dict)

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', action='store_true')
    parser.add_argument('-r', action='store_true')
    parser.add_argument('--size', type=int)
    args, unknown = parser.parse_known_args(argv)

    if args.w:
        if args.size:
            create_big_file(args.size)
        create_big_file()

    if args.r:
        read_big_file()

if __name__ == '__main__':
    start_time = time.time()
    main(sys.argv)
    print(f'--- {time.time() - start_time} seconds ---')

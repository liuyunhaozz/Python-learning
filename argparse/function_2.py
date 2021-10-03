# 一个解析器，多个参数

import argparse


def handle_read(args):
    print(args)
    print(args.path, args.length, args.key)


def handle_write(args):
    print(args)
    print(args.path, args.encoding)


def main():
    read_parser = argparse.ArgumentParser()


    
    read_parser.add_argument('--path', required=True, help="file path")
    read_parser.add_argument('--length', required=True, help="file length")
    read_parser.add_argument('--key', required=True, help="file key")
    read_parser.set_defaults(func=handle_read)	# 绑定处理函数


    args = read_parser.parse_args()
    # 执行函数功能
    args.func(args)


if __name__ == '__main__':
    main()

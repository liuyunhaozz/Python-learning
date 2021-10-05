# 一个解析器有两个子解析器，两个子解析器有各自的参数

import argparse


def handle_read(args):
    print(args)
    print(args.path, args.length, args.key)


def handle_write(args):
    print(args)
    print(args.path, args.encoding)


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands')

    read_parser = subparsers.add_parser(name='--read', help='read file')
    read_parser.add_argument('--path', required=True, help="file path")
    read_parser.add_argument('--length', required=True, help="file length")
    read_parser.add_argument('--key', required=True, help="file key")
    read_parser.set_defaults(func=handle_read)	# 绑定处理函数

    write_parser = subparsers.add_parser(name='--write', help='write file')
    write_parser.add_argument('--path', required=True, help="file path")
    write_parser.add_argument('--encoding', required=True, help="file encoding")
    write_parser.set_defaults(func=handle_write)	# 绑定处理函数

    args = parser.parse_args()
    # 执行函数功能
    args.func(args)


if __name__ == '__main__':
    main()

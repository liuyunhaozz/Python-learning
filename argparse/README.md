## [Python] argparse处理多个功能和不同的多参数



### 0. 前情提要

我想要使Python脚本能处理多个功能，每个功能都有多个不同的参数，就像git一样:

```shell
$ git add -h
usage: git add [<options>] [--] <pathspec>...

    -n, --dry-run         dry run
    -v, --verbose         be verbose
    -i, --interactive     interactive picking
    -p, --patch[=<patch-mode>]
                          select hunks interactively
	...


$ git push -h
usage: git push [<options>] [<repository> [<refspec>...]]

    -v, --verbose         be more verbose
    -q, --quiet           be more quiet
    --repo <repository>   repository
    --all                 push all refs
    --mirror              mirror all refs
    -d, --delete          delete refs
	...
	
```

git相当于python的调用，即`git add -h` 可以理解为调用 `python argpares1.py add -h`，`git push -h`可以理解为调用`python argparse1.py push -h`。argparse1.py这脚本里有多个功能，每个功能有不同的参数。先看我写脚本的效果，一个是read参数，另一个是write参数：

```shell
$ python argparse1.py read -h
usage: argparse1.py read [-h] --path PATH --length LENGTH --key KEY

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      file path
  --length LENGTH  file length
  --key KEY        file key

$ python argparse1.py write -h
usage: argparse1.py write [-h] --path PATH --encoding ENCODING

optional arguments:
  -h, --help           show this help message and exit
  --path PATH          file path
  --encoding ENCODING  file encoding

```

### 1. 使用add_subparsers处理多个功能使用多个不同参数

```python
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

    read_parser = subparsers.add_parser(name='read', help='read file')
    read_parser.add_argument('--path', required=True, help="file path")
    read_parser.add_argument('--length', required=True, help="file length")
    read_parser.add_argument('--key', required=True, help="file key")
    read_parser.set_defaults(func=handle_read)	# 绑定处理函数

    write_parser = subparsers.add_parser(name='write', help='write file')
    write_parser.add_argument('--path', required=True, help="file path")
    write_parser.add_argument('--encoding', required=True, help="file encoding")
    write_parser.set_defaults(func=handle_write)	# 绑定处理函数

    args = parser.parse_args()
    # 执行函数功能
    args.func(args)


if __name__ == '__main__':
    main()
```

使用效果如前文一样：

```shell
$ python argparse3.py read -h
usage: argparse3.py read [-h] --path PATH --length LENGTH --key KEY

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      file path
  --length LENGTH  file length
  --key KEY        file key


$ python argparse3.py write -h
usage: argparse3.py write [-h] --path PATH --encoding ENCODING

optional arguments:
  -h, --help           show this help message and exit
  --path PATH          file path
  --encoding ENCODING  file encoding
  
  
$ python argparse3.py read --path C:/desktop --length 10 --key project
Namespace(func=<function handle_read at 0x000001AC47B14EE8>, key='project', length='10', path='C:/desktop')
C:/desktop 10 project


$ python argparse3.py write --path C:/desktop --encoding utf-8
Namespace(encoding='utf-8', func=<function handle_write at 0x000001CB2BDF9438>, path='C:/desktop')
C:/desktop utf-8
```



### 2.**Python arg解析没有参数的命令行标志**

添加一个快速片段执行：

**资料来源：**

```python
import argparse
parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
parser.add_argument('-w', action='store_true')

args = parser.parse_args()
print args.w
```

**用法：**

```sh
python myparser.py -w
>> True
```


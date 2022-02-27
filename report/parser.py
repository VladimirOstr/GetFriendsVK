import argparse
import os


def parse_arg(args: list[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', help="VK_API токен", type=str, required=True)
    parser.add_argument('-u', '--user_id', help="ID пользователя", type=int, required=True)
    parser.add_argument('-f', '--format', help='Формат отчета', default='csv',
                        type=str, choices=['csv', 'tsv', 'json'])
    parser.add_argument('-c', '--catalog', help='Папка отчета',  
                        default=os.getcwd(),type=str)

    return parser.parse_args(args)
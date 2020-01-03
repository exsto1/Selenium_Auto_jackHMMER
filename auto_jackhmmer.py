import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-I', help='Number of iterations', default=3)
parser.add_argument('-F', help='ABSOLUTE path to file', default='')
parser.add_argument('-B', help='Base name of images and summary file', default='')
parser.add_argument('-M', help='ABSOLUTE path to folder with files', default='')
args = parser.parse_args()

WEBBROWSER = open('config/config.txt').readlines()[1].rstrip()


def multi_open(multi):
    list_of_files = os.listdir(multi)
    for i in list_of_files:
        if '.' in i:
            base = i.split('.')[0]
        else:
            base = i
        os.system(f'python3 file_process.py -W {WEBBROWSER} -F {multi}{i} -B {base} -I {args.I}')


if args.F == '' and args.M == '':
    os.system('python3 open_gui.py')
elif args.F and args.M:
    print('Cannot read one and multi files at the same time!')
    parser.print_help()
    exit(1)
elif args.F:
    if args.B:
        os.system(f'python3 file_process.py -W {WEBBROWSER} -F {args.F} -B {args.B} -I {args.I}')
    else:
        print('Base name missing!')
        parser.print_help()
        exit(1)
elif args.M:
    multi_open(args.M)

'-F /home/exsto/PycharmProjects/selenium_testing/PF16777_full_renamed.fasta -B PF16777 -I 2'

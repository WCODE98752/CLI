import argparse
import sys


def cal(args):                   
    if args.o == 'add':
        return args.x + args.y
    
    elif args.o == 'mul':
        return args.x * args.y
    
    elif args.o == 'sub':
        return args.x - args.y
    
    elif args.o == 'div':
        return args.x / args.y
    



pars = argparse.ArgumentParser()


pars.add_argument('--x', type=float, default=1.0,help='ENter a first num!')

pars.add_argument('--y', type=float, default=1.0,help='ENter a first num!')

pars.add_argument('--o',help='ENter a first num!')


args = pars.parse_args()
sys.stdout.write(str(cal(args)))
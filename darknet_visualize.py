from read_cfg import read_cfg
from graph import viz_simple
import argparse


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('cfg',help='config file path')
    parser.add_argument('--format','-f',help='graph format, default=png',default='png')
    parser.add_argument('--show',help='show the graph',default=True)
    args=parser.parse_args()
    cfg=read_cfg(args.cfg)
    g=viz_simple(cfg,args.format)
    g.view()
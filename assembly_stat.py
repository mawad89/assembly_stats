#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:51:26 2019

@author: awad
"""

def assembly_stat(path):
    '''
    This function calculate genome statistics
    '''
    a=list(open(path))
    a=''.join(a)
    a=a.split('>')
    del a[0]
    b=[]
    d=[]
    for base in a:
        c=base.split('\n')
        b.append('>'+c[0])
        b.append(''.join(c[1:])+'\n')
        d.append(len(''.join(c[1:])))
    genome_length=sum(d)
    d.sort(reverse=True)
    no_of_contigs=len(d)
    longest_contig=d[0]
    length=genome_length/2
    n=0
    z=0
    while z<length:
        z=z+d[n]
        n=n+1
    L50=n
    N50=d[n-1]
    length=genome_length*0.75
    n=0
    z=0
    while z<length:
        z=z+d[n]
        n=n+1
    L75=n
    N75=d[n-1]
    path=path.replace('.fasta','')
    path=path.replace('.fa','')
    f=open(path+'_stat','w')
    f.writelines('genome_length= '+str(genome_length)+'\n'+'no_of_contigs= '+str(no_of_contigs)+'\n'+'longest_contig= '+str(longest_contig)+'\n'+'L50= '+str(L50)+'\n'+'N50= '+str(N50)+'\n'+'L75= '+str(L75)+'\n'+'N75= '+str(N75)+'\n'+'Citation:https://github.com/mawad89/assembly_stats.git')
    print('genome_length= '+str(genome_length)+'\n'+'no_of_contigs= '+str(no_of_contigs)+'\n'+'longest_contig= '+str(longest_contig)+'\n'+'L50= '+str(L50)+'\n'+'N50= '+str(N50)+'\n'+'L75= '+str(L75)+'\n'+'N75= '+str(N75)+'\n')
    return()

import argparse
parser = argparse.ArgumentParser(prog="genome statistics",usage='%(prog)s -h [options] -p <path> ',description='calculate genome statistics',)
parser.add_argument("path",nargs=1,metavar='genome as fasta')
args = parser.parse_args()

path=args.path[0]
assembly_stat(path)

import os
import multiprocessing
from multiprocessing import Pool

blast_bin = '/home/jrymut/ncbi-blast-2.2.30+/bin'
makeblastdb = blast_bin + '/makeblastdb'
genomes = './genomes/'
dbs_dir = './dbs/'

def get_bacterias():
    query = 'mtu'
    bacterias = []
    with open('bacteria.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            bacterias.append(line[0])
    return query, bacterias

query, bacterias = get_bacterias()

def run(bacteria):
    input_fn = genomes + bacteria +'.fasta'
    log_fn = bacteria + '.log'
    command = makeblastdb + ' -in ' + input_fn + ' -dbtype prot' + ' -out ' + dbs_dir + bacteria + ' -logfile ' + log_fn
    os.system(command)


if __name__ == '__main__':
    workers = multiprocessing.cpu_count()
    pool = Pool(workers)
    res = pool.imap_unordered(run, bacterias, chunksize=3)
    for r in res:
       print(r)

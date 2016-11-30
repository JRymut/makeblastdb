import os
import multiprocessing
from multiprocessing import Pool


def get_bacterias():
    query = 'bsu'
    bacterias = []
    with open('bacteria.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            bacterias.append(line[0])
    return query, bacterias

blast_bin = '/home/jrymut/ncbi-blast-2.2.30+/bin'
blastp = blast_bin + '/blastp'
makeblastdb = blast_bin + '/makeblastdb'
genomes = './genomes/'
dbs = './dbs/'
blast = './blasts/'
query, bacterias = get_bacterias()
query_fn = genomes + query + '.fasta'



def run(bacteria):
    print(bacteria)
    out = blast + bacteria + '.out'
    command = blastp +' -evalue 1e-10 -db '+ dbs+bacteria + ' -query ' + query_fn + ' -out ' +blast+ bacteria + '.out -outfmt 6'
    os.system(command)


if __name__ == '__main__':
    workers = multiprocessing.cpu_count()
    pool = Pool(workers)
    res = pool.imap_unordered(run, bacterias, chunksize=3)
    for r in res:
       print(r)

    
    
    
    
#kill -9 `ps x | grep multi | awk '{print $1}'`    (ubijanie procesow)

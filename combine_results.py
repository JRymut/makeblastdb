def get_bacterias_out():
    bacterias = []
    with open('bacteria.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            bacterias.append(line[0]+".out")
    return bacterias

def otwieranie(bacteria):
    global geny
    geny = []
    with open(bacteria, "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.split()
        if line[2] >= 50 and eval(line[-2]) <= 10**10:
            geny.append([line[0], line[3]])

def obrobka(gen):
    global result, final
    result = []
    final = []
    liczba_pow = geny.count(gen)
    n = gen
    n.append(str(liczba_pow))
    result.append(n)

def obrobka_cd(gen):
    if gen not in final:
        final.append(gen)
    return final

def zapisywanie():
    with open("results.csv", "w") as f:
        for line in final:
            f.write(','.join(line))
            f.write("\n")
            
if __name__ == '__main__':
    os.chdir(./blasts)
    workers = multiprocessing.cpu_count()
    pool = Pool(workers)
    res = pool.imap_unordered(otwieranie, bacterias, chunksize=3)
    for r in res:
       print(r)
    res2 = pool.imap_unordered(obrobka, geny, chunksize=3)
    for r in res2:
       print(r)
    res3 = pool.imap_unordered(obrobka_cd, result, chunksize=3)
    for r in res3:
       print(r)
    zapisywanie()

import numpy  # type: ignore
import argparse
import csv
import json


def parseData(file):
    f = open(file)
    reader = csv.DictReader(f)  

    
    for row in reader:
        prodList[row['product']] = {}
        prodList[row['product']]['limits'] = {}
        
        prodList[row['product']]['limits']['maxProd'] = int(row['maxProd'])
        prodList[row['product']]['limits']['maxTime'] = int(row['maxTime'])

    f.close()  

def genProducts(prodList):
    for k in prodList.keys():
        prodList[k]['quantity'] = numpy.random.randint(1, high = prodList[k]['limits']['maxProd'])


def genTimes(prodList):
    for k in prodList.keys():
        prodList[k]['time'] = numpy.random.randint(1, high = prodList[k]['limits']['maxTime'])


def genProdTime(prodList):
    time = 0

    
    for k in prodList.keys():
        time += prodList[k]['quantity'] * prodList[k]['time']

    return time  


def printProd(prodList):
    retstr = ''  

    for k in prodList.keys():
        if k != 'total time':  
            retstr += f" - {k}: {prodList[k]['quantity']} unità, ognuna {prodList[k]['time']} minuti\n"  

    return retstr  

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True) 
parser.add_argument('-o', '--output')  


args = parser.parse_args()

prodList = {}  

parseData(args.file)

genProducts(prodList)
genTimes(prodList)


prodList['total time'] = genProdTime(prodList)

print(f'''
Prodotti: 
{printProd(prodList)}
Tempo di produzione totale: {prodList['total time'] if prodList['total time'] < 60 else round(prodList['total time'] / 60)} {'minuti' if prodList['total time'] < 60 else 'ore'}
''')

if args.output:
    of = open(args.output, 'w') 

    
    json.dump(prodList, of, indent = 4)
    
    of.close() 

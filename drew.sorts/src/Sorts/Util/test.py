'''
@author: Drew.Xiu    
@2013.12.29

'''

from random import shuffle

def cardHeap(volume):
    cardHeap = list(range(volume))
    
    shuffle(cardHeap)
    print(cardHeap)
    return cardHeap
    


if __name__ == '__main__':
    cardHeap(30)
    pass
import xml.etree.ElementTree as ET
import heapq as hq
from queue import PriorityQueue
filename = "bcd.xml"
tree = ET.parse(filename)
root = tree.getroot()
ob = {}

def pq():
    return []
mpo = {} # map of orders
def execute(book,order):
    return 0
def addOrder(book, order):
    if (order[0] == "BUY"):
        if(book['SELL'].top <= order[1]):
            execute(book,order)
        else:
            book['BUY'].push(order)
    else:
        if(book['BUY'].top >= order[1]):
            execute(book,order)
        else:
            book['SELL'].push(order)
    return []
for el in root:
    # print(el.attrib)
    if(el.tag == 'AddOrder'):
        if(el.attrib['book'] not in ob):
            ob[el.attrib['book']] = {"BUY": pq(),"SELL":pq()}
        mpo[el.attrib['orderId']] = [el.attrib['operation'],el.attrib['price'],el.attrib['volume']]
        addOrder(ob[el.attrib['book']],[el.attrib['operation'],el.attrib['price'],el.attrib['volume']])
    
    else:
        print('no')

#Ek Data structure maan le OrderQueueAtParticularPrice
#Ye ek Doubly linked list hai. Jisme saare orders same price ke hai, depending on new order, list me usko end me add kardenge as when they come
# Fir Priority queue of OrderQueueAtParticularPrice objects maintain karenge
# Jisse hamare pass sorted order me honge ye doubly linked lists
#Aur finally do maps maintain karne hai
# Ek to individual order id ka pointer kya hai, basically uska meta data
# aur ek map hoga jo batayega particular price ki list konsi hai
# Call this priceMap
# This orderMap

#Jab naye price aayega. to pahle to check karoge ki wo price map me present hai ya nahi, Hai to uss price ki list nikalo(OrderQueueAtParticularPrice object) aur usme add kar do at the end
# nahi hai present to nayi OrderQueueAtParticularPrice object banao of that price usme ye element add karo aur uss naye list object ko priceMap me add kar do
#Jab bhi naya order aayga to usko orderMap me add karna hi karna hai
#Do maps aur ek priority queue se ho ajyega
# Sab O(1) ya O(log n0 operation honge
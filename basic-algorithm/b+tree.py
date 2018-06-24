from bisect import bisect_right,bisect_left
from collections import deque


class KeyValue(object):
    __slots__=('key', 'value')

    def __init__(self,key,value):
        self.key=key
        self.value=value

    def __str__(self):
        return str((self.key,self.value))

    def __cmp__(self, key):
        if self.key > key:
            return 1
        elif self.key == key:
            return 0
        else:
            return -1


class Bptree_InterNode(object):
    def __init__(self,M):
        self.__M=M
        self.clist=[]
        self.ilist=[]
        self.par=None

    def isleaf(self):
        return False

    def isfull(self):
        return len(self.ilist)>=self.M-1

    def isempty(self):
        return len(self.ilist)<=(self.M+1)/2-1

    @property
    def M(self):
        return self.__M


class Bptree_Leaf(object):
    def __init__(self,L):
        self.__L=L
        self.vlist=[]
        self.bro=None
        self.par=None

    def isleaf(self):
        return True

    def isfull(self):
        return len(self.vlist)>self.L

    def isempty(self):
        return len(self.vlist)<=(self.L+1)/2

    @property
    def L(self):
        return self.__L


class Bptree(object):

    def __init__(self,M, L):
        if L>M:
            print("error")
        else:
            self.__M=M
            self.__L=L
            self.__root=Bptree_Leaf(L)
            self.__leaf=self.__root

    @property
    def M(self):
        return self.__M

    @property
    def L(self):
        return self.__L

    def insert(self,key_value):
        node=self.__root

        def split_node(n1):
            mid=self.M/2
            newnode=Bptree_InterNode(self.M)
            newnode.ilist=n1.ilist[mid:]
            newnode.clist=n1.clist[mid:]
            newnode.par=n1.par
            for c in newnode.clist:
                c.par=newnode
            if n1.par is None:
                newroot=Bptree_InterNode(self.M)
                newroot.ilist=[n1.ilist[mid-1]]
                newroot.clist=[n1,newnode]
                n1.par=newnode.par=newroot
                self.__root=newroot
            else:
                i=n1.par.clist.index(n1)
                n1.par.ilist.insert(i,n1.ilist[mid-1])
                n1.par.clist.insert(i+1,newnode)
            n1.ilist=n1.ilist[:mid-1]
            n1.clist=n1.clist[:mid]
            return n1.par

        def split_leaf(n2):
            mid=(self.L+1)/2
            newleaf=Bptree_Leaf(self.L)
            newleaf.vlist=n2.vlist[mid:]

            if n2.par is None:
                newroot=Bptree_InterNode(self.M)
                newroot.ilist=[n2.vlist[mid].key]
                newroot.clist=[n2,newleaf]
                n2.par=newleaf.par=newroot
                self.__root=newroot
            else:
                i=n2.par.clist.index(n2)
                n2.par.ilist.insert(i,n2.vlist[mid].key)
                n2.par.clist.insert(i+1,newleaf)
                newleaf.par=n2.par

            n2.vlist=n2.vlist[:mid]
            n2.bro=newleaf

        def insert_node(n):
            if not n.isleaf():
                if n.isfull():
                    insert_node(split_node(n))
                else:
                    p=bisect_right(n.ilist, key_value)
                    insert_node(n.clist[p])
            else:
                p=bisect_right(n.vlist,key_value)
                n.vlist.insert(p,key_value)
                if n.isfull():
                    split_leaf(n)
                else:
                    return
        insert_node(node)

    def search(self,mi=None,ma=None):
        result=[]
        node=self.__root
        leaf=self.__leaf

        def search_key(n,k):
            if n.isleaf():
                p=bisect_left(n.vlist,k)
                return (p,n)
            else:
                p=bisect_right(n.ilist,k)
                return search_key(n.clist[p],k)
        if mi is None:
            while True:
                for kv in leaf.vlist:
                    if kv<=ma:
                        result.append(kv)
                    else:
                        return result

                if leaf.bro is None:
                    return result
                else:
                    leaf=leaf.bro
        elif ma is None:
            index,leaf=search_key(node,mi)
            result.extend(leaf.vlist[index:])
            while True:
                if leaf.bro is None:
                    return result
                else:
                    leaf=leaf.bro
                    result.extend(leaf.vlist)
        else:
            if mi==ma:
                i,l=search_key(node,mi)
                try:
                    if l.vlist[i]==mi:
                        result.append(l.vlist[i])
                        return result
                    else:
                        return result
                except IndexError:
                    return result
            else:
                i1,l1=search_key(node,mi)
                i2,l2=search_key(node,ma)
                if l1 is l2:
                    if i1==i2:
                        return result
                    else:
                        result.extend(l.vlist[i1:i2])
                        return result
                else:
                    result.extend(l1.vlist[i1:])
                    l=l1
                    while True:
                        if l.bro==l2:
                            result.extend(l2.vlist[:i2+1])
                            return result
                        else:
                            result.extend(l.bro.vlist)
                            l=l.bro

    def traversal(self):
        result=[]
        l=self.__leaf
        while True:
            result.extend(l.vlist)
            if l.bro is None:
                return result
            else:
                l=l.bro

    def show(self):
        print('this b+tree is:\n')
        q=deque()
        h=0
        q.append([self.__root,h])
        while True:
            try:
                w,hei=q.popleft()
            except IndexError:
                return
            else:
                if not w.isleaf():
                    print(w.ilist,'the height is',hei)
                    if hei==h:
                        h+=1
                    q.extend([[i,h] for i in w.clist])
                else:
                    print([v.key for v in w.vlist],'the leaf is,',hei)

    def delete(self,key_value):
        def merge(n,i):
            if n.clist[i].isleaf():
                n.clist[i].vlist=n.clist[i].vlist+n.clist[i+1].vlist
                n.clist[i].bro=n.clist[i+1].bro
            else:
                n.clist[i].ilist=n.clist[i].ilist+[n.ilist[i]]+n.clist[i+1].ilist
                n.clist[i].clist=n.clist[i].clist+n.clist[i+1].clist
            n.clist.remove(n.clist[i+1])
            n.ilist.remove(n.ilist[i])
            if n.ilist==[]:
                n.clist[0].par=None
                self.__root=n.clist[0]
                del n
                return self.__root
            else:
                return n
        def tran_l2r(n,i):
            if not n.clist[i].isleaf():
                n.clist[i+1].clist.insert(0,n.clist[i].clist[-1])
                n.clist[i].clist[-1].par=n.clist[i+1]
                n.clist[i+1].ilist.insert(0,n.ilist[i])
                n.ilist[i]=n.clist[i].ilist[-1]
                n.clist[i].clist.pop()
                n.clist[i].ilist.pop()
            else:
                n.clist[i+1].vlist.insert(0,n.clist[i].vlist[-1])
                n.clist[i].vlist.pop()
                n.ilist[i]=n.clist[i+1].vlist[0].key
        def tran_r2l(n,i):
            if not n.clist[i].isleaf():
                n.clist[i].clist.append(n.clist[i+1].clist[0])
                n.clist[i+1].clist[0].par=n.clist[i]
                n.clist[i].ilist.append(n.ilist[i])
                n.ilist[i]=n.clist[i+1].ilist[0]
                n.clist[i+1].clist.remove(n.clist[i+1].clist[0])
                n.clist[i+1].ilist.remove(n.clist[i+1].ilist[0])
            else:
                n.clist[i].vlist.append(n.clist[i+1].vlist[0])
                n.clist[i+1].vlist.remove(n.clist[i+1].vlist[0])
                n.ilist[i]=n.clist[i+1].vlist[0].key
        def del_node(n,kv):
            if not n.isleaf():
                p=bisect_right(n.ilist,kv)
                if p==len(n.ilist):
                    if not n.clist[p].isempty():
                        return del_node(n.clist[p],kv)
                    elif not n.clist[p-1].isempty():
                        tran_l2r(n,p-1)
                        return del_node(n.clist[p],kv)
                    else:
                        return del_node(merge(n,p),kv)
                else:
                    if not n.clist[p].isempty():
                        return del_node(n.clist[p],kv)
                    elif not n.clist[p+1].isempty():
                        tran_r2l(n,p)
                        return del_node(n.clist[p],kv)
                    else:
                        return del_node(merge(n,p),kv)
            else:
                p=bisect_left(n.vlist,kv)
                try:
                    pp=n.vlist[p]
                except IndexError:
                    return -1
                else:
                    if pp!=kv:
                        return -1
                    else:
                        n.vlist.remove(kv)
                        return 0
        del_node(self.__root,key_value)


def test():
    testlist=[]
    for i in range(1,100):
        key=i
        value=i
        testlist.append(KeyValue(key,value))

    mybptree=Bptree(4,4)
    for kv in testlist:
        mybptree.insert(kv)
    mybptree.delete(testlist[0])
    mybptree.show()
    print('key of this b+tree is:',
          [kv.key for kv in mybptree.traversal()])

    mini=2
    maxi=60
    #print [kv.key for kv in mybptree.search(mini,maxi)]

if __name__=='__main__':
    test()
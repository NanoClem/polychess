# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:37:39 2018

@author: dupouyj
@doc : Clément
"""
import math
class Node:
    """
        Cette classe modelise un noeud
    """
    cpt1=0
    cpt2=0
    
    def __init__(self,content,children=[]):
        """
            CONSTRUCTEUR
            :param content: etiquette du noeud
            :param children: liste des enfant du noeud
            :type content: str
            :type children: list
        """
        self.content=content
        self.children=children
    

    
    def get_content(self):
        """
            accesseur de l'etiquette du noeud
            :return: etiquette du noeud
        """
        return self.content


    
    def get_children(self):
        """
            accesseur des enfants du noeud
            :return: liste des enfants du noeud
        """
        ret=[]
        if self.children==ret:
            return self.children
        else:
            for i in range(len(self.children)):
                if self.children[i]!=None:
                    ret.append(self.children[i])
            return ret

 
    def is_leaf(self):
        """
            permet de savoir si le noeud est une feuille
            :return: booleen
        """
        return self.get_children() == []



    
    def minmax(self, maximizingPlayer):
        Node.cpt1+=1
        if self.is_leaf():
            return self.content
        if maximizingPlayer:
            value=-math.inf
            for i in range(len(self.get_children())):
                value=max(value,float(self.get_children()[i].minmax( False)))
            return value
        else:
            value=math.inf
            for i in range(len(self.get_children())):
                value=min(value,float(self.get_children()[i].minmax( True)))
            return value
    
    
    def minmaxAB(self, A, B, maximizingPlayer):
        Node.cpt2+=1
        if self.is_leaf():
            return self.content
        Alpha=A
        Beta=B
        if maximizingPlayer:
            for i in range(len(self.get_children())):
                Alpha=max(Alpha,float(self.get_children()[i].minmaxAB(Alpha, Beta, False)))
                if Alpha>=Beta:
                    return Beta
            return Alpha
        else:
            for i in range(len(self.get_children())):
                Beta=min(Beta,float(self.get_children()[i].minmaxAB(Alpha, Beta, True)))
                if Alpha>=Beta:
                    return Alpha
            return Beta
    




if __name__=="__main__" :
    # =============================================================================
    # Implementation de l'arborescence
    # =============================================================================
    
    n12=Node('45')
    n11=Node('-2')
    n10=Node('6')
    n9=Node('23')
    n8=Node('-8')
    n7=Node('22')
    n6=Node('9')
    n5=Node('3')
    n4=Node('3')
    n3=Node('',[n10,n11,n12])
    n2=Node('',[n7,n8,n9])
    n1=Node('',[n4,n5,n6])
    n0=Node('',[n1,n2,n3])
    
    print("minmax", n0.minmax(True), "cpt=", Node.cpt1)
    print("minmaxAB", n0.minmaxAB(-math.inf, math.inf, True), "cpt=", Node.cpt2)

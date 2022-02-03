#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[27]:


#exercie 1 Écrivez un programme qui trouvera tous ces nombres qui sont divisibles par 7 mais qui ne sont pas un multiple de 5, entre 2000 et 3200 (les deux inclus). 
#Les nombres obtenus doivent être imprimés en séquence sur une seule ligne.
for i in range(2000,3201):
    if (i % 5) != 0 and (i % 7) == 0:
        print (i)


# In[30]:


#exercie2 Écrire un programme capable de calculer la factorielle d'un nombre donné. Les résultats doivent être imprimés en séquence sur une seule ligne. 
#Supposons que l'entrée suivante soit fournie au programme : 5 Alors, la sortie devrait être : 120
nbr = int(input('Entrez un nombre : '))
x = 1
for i in range(1, nbr+1):
    x = x * i
print (nbr,'! = ',x)


# In[25]:


#question 3 
#Avec un nombre entier n donné, 
#écrivez un programme pour générer un dictionnaire qui contient (i, i*i) 
#tel qu'il soit un nombre entier compris entre 1 et n (tous deux inclus). 
#puis le programme doit imprimer le dictionnaire. Supposons que l'entrée suivante soit fournie au programme :
# 8 Ensuite, la sortie doit être : {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25, 6 : 36, 7 : 49, 8 : 64 } 

n = int(input('Entrez un nombre : '))
{x: x*x for x in range(1,n+1)}


# In[26]:


#question4
#Étant donné une chaîne non vide et un int n, 
#renvoie une nouvelle chaîne où le caractère à l'index n a été supprimé. La valeur de n sera un index valide d'un caractère
#dans la chaîne d'origine (c'est-à-dire que n sera compris entre 0..len(str)-1 inclus). 
#missing_char('kitten', 1) → 'ktten' par exemple ici on supprime "i" qui se trouve dans l'index 1
#missing_char('kitten', 0) → 'itten' ici on supprime "k" qui est dans l'index 0
#missing_char('kitten', 4) → 'kittn' ici on supprime "e" qui est dans l'index 4
mot = str(input("entrez un mot:"))
f = int(input("numero de caractère à supprimer "))
print(mot.replace(mot[f],"",1))


# In[ ]:





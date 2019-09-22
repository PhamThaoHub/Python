#tap cac phan tu la
List_words =  list(open('data.txt').read().split())
print ('list of world',List_words)
print ('\n')
print ('------\n')
from collections import Counter
print ('1. Cach khac de dem cac phan tu khong trung lap:')
print ('Cac phan tu khong trung la:      ', Counter(List_words).keys())
print ('So luong tung phan tu tuong ung: ', Counter(List_words).values())

print ('------\n')

print ('2. Dem khong lap lai cac phan tu:')
listOfStrings = list();
for word in List_words:
    if word not in listOfStrings :
        listOfStrings.append(word)
        print("\t",word, "=", List_words.count(word))   
print ("\t",'Tong so phan tu khong lap lai la:',len(listOfStrings),'\n')

print ('------\n')
print ('3. Dem toan bo (co lap lai):')
for word in List_words:
    print("\t",word, "=", List_words.count(word))   
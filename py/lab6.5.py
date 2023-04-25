list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
anawords = ["evil","levi", "levy", "brick"]

def intersectlist(lista,listb):
    seta=set(lista)
    setb=set(listb)
    inter=seta.intersection(setb)
    return list(inter)


def palindrome(palstring):
    return palstring == palstring[::-1]


def sieve(targetnum):
    numbers=[x for x in range(1,targetnum+1)]
    numbers.remove(1)
    n = 0
    prime=numbers[n]
    while prime*prime <= targetnum:
        for y in numbers:
            if y % prime == 0 and y != prime:
                numbers.remove(y)
        n += 1
        prime = numbers[n]
    return numbers


def anagram(anaword, anagramlist):
    targetlist=[i for i in anaword]
    targetlist.sort()
    final = []
    for j in anagramlist:
        templist = [k for k in j]
        templist.sort()
        if targetlist == templist:
            final.append(j)

    return final



print(intersectlist(list1,list2))
print(palindrome("among"))
print(palindrome("tacocat"))
print(sieve(50))
print(anagram("vile", anawords))
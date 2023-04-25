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


def sieve(numbers):
    nonprime = [0,1]
    for x in nonprime:
        for y in numbers:
            if x in numbers: numbers.remove(x)

    maxval = max(numbers)
    prime = 2
    while prime*prime <= maxval:
        for y in numbers:
            if y % prime == 0 and y != prime:
                numbers.remove(y)

        prime +=1
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


print("Intersection of the given lists: ")
print(intersectlist(list1,list2))
print("Is 'among' a palindrome?")
print(palindrome("among"))
print("Is 'tacocat' a palindrome?")
print(palindrome("tacocat"))
sievenumbers = [1,4,6,89,2,6,9,34,23,4,0]
print("Primes from given list: ")
print(sieve(sievenumbers))
print("Anagrams for 'vile':")
print(anagram("vile", anawords))
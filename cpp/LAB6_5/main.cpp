#include <iostream>
#include <vector> //had to.
#include <unordered_set>
#include <algorithm> //How a reverse string is done exists on previous labs, I'd like to cut it shorter by importing the reverse function

using namespace std;

//Strictly assuming no duplicates exist on the lists. Deduplication is out of scope.
vector<int> intersection(int list1[],int s1, int list2[], int s2){ //list1 and list2 are arrays, s1 and s2 are sizes for each
    unordered_set<int> set2(list2, list2 + s2);
    vector<int> result;

    for(int i = 0; i < s1; i++){
        if(set2.find(list1[i]) != set2.end()){
            result.push_back(list1[i]);
        }
    }
    return result;
}

bool palindrome (string paltest){
    string revstring = paltest;
    reverse(revstring.begin(),revstring.end());
    return(paltest == revstring);
}


vector<int> primesieve(int source[], int so1){
    int max = *max_element(source, source + so1);
    vector<bool> is_prime(max + 1, true); //Couldn't really find a way to one-list this
    vector<int> primes;
    for (int ctr = 2; ctr * ctr <= max; ctr++) {
        if (is_prime[ctr]) {
            for (int i = ctr * ctr; i <= max; i += ctr) {
                is_prime[i] = false;
            }
        }
    }
    for (int i = 0; i < so1; i++) {
        if (source[i] >= 2 && is_prime[source[i]]) {
            primes.push_back(source[i]);
        }
    }
    return primes;

}

vector<string> anagrams(string anaword, string words[], int wordnum){
    vector<string> wordvector(words, words + wordnum); //You want to pass an array? Too bad it's just a pointer to the head of it
    vector<string> anaresult;
    sort(anaword.begin(), anaword.end());
    for (string z : wordvector){
        string temp = z;
        sort(z.begin(),z.end());
        if (z == anaword){
            anaresult.push_back(temp);
        }
    }
    return anaresult;
}



int main() {
    int arr1[]= {1,2,3,4,5,6};
    int arr2[]={3,4,5,6,7,8};
    vector<int> final = intersection(arr1,6,arr2,6);
    cout << "Intersection: ";
    for(int x : final){
        cout << x << " ";
    }
    cout << endl;
    cout << "Is 'test' a palindrome?: ";
    cout << palindrome("test") << endl;
    cout << "Is 'tacocat' a palindrome?: ";
    cout << palindrome("tacocat") << endl;

    int numbers[] = {3,5,0,1,6,8,23};
    int numbersize = 7;
    vector<int> primer = primesieve(numbers,numbersize);
    cout << "Primes in given array: ";
    for(int y : primer){
        cout << y << " ";
    }
    cout << endl;

    string anagramtest = "evil";
    string wordlist[] = {"vile", "wipe", "with", "levi"};
    vector<string> anagram = anagrams(anagramtest,wordlist,4);
    cout << "Anagrams against 'evil' in the array: ";
    for(string c : anagram){
        cout << c << " ";
    }
    cout << endl;

    return 0;
}

#include <iostream>
using namespace std;

int main() {
    //Task 1
    string name;
    string number;
    cout << "What is your name?";
    cin >> name;
    cout << "Hello, " << name << endl;
    cout << "What is your student ID?";
    cin >> number;
    cout << "Your number is " << number << endl;

    //Task 2
    int var1;
    int var2;
    int sum, diff, prod;
    cout << "First number:";
    cin >> var1;
    cout << "What's the second number?";
    cin >> var2;
    sum = (var1 + var2);
    diff = (var1 - var2);
    prod = (var1 * var2);
    cout << "The sum is " << sum << ", the diff is " << diff << ", and the product is " << prod << "." << endl;

    //Task 3
    string studentname;
    int lab, midterm, finals;
    float grade;
    cout << "Please enter a student name:";
    cin >> studentname;
    cout << "Please enter the lab score:";
    cin >> lab;
    cout << "Please enter the midterm score:";
    cin >> midterm;
    cout << "Please enter the final score:";
    cin >> finals;
    grade = (lab * 0.25) + (midterm * 0.35) + (finals * 0.4);
    cout << "Name: " << studentname << endl << "Lab: " << lab << endl << "Midterm: " << midterm << endl << "Final: " << finals << endl <<"Grade: " << grade << endl;

    //Task 4
    cout << "*" << endl << "**" << endl << "***" << endl << "**" << endl << "*";
    return 0;
}

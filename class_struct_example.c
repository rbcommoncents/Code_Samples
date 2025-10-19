#include <stdio.h>

typedef struct {
    char name[50];
    int age;
} Person;

void print_person(Person p) {
    printf("Name: %s, Age: %d\n", p.name, p.age);
}

int main() {
    Person p = {"Ryszard", 32};
    print_person(p);
    return 0;
}

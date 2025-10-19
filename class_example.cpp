#include <iostream>
#include <string>
using namespace std;

class Device {
public:
    string name;
    int id;

    Device(string n, int i) : name(n), id(i) {}

    void display() const {
        cout << "Device: " << name << ", ID: " << id << endl;
    }
};

int main() {
    Device d("ESP32-S3", 101);
    d.display();
    return 0;
}

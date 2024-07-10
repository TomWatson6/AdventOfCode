#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    ifstream inputFile("input.txt");

    if (inputFile.is_open()) {
        string line;

        // Read and output file contents line by line
        while (getline(inputFile, line, ' ')) {
            
            vector<string> segments;
            stringstream ss(line);

            for(const auto& s: segments) {

            }
        }

        inputFile.close(); // Don't forget to close the file when done
    } else {
        std::cout << "Unable to open file." << std::endl;
    }

    return 0;
}


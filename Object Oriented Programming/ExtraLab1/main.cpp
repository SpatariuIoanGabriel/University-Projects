#include "Puzzle.h"
#include <iostream>

int main()
{
    Puzzle p("words_alpha.txt");
    int choice;
    std::string word1, word2;
    std::vector<std::string> path;

    do {
        std::cout << "Menu:\n";
        std::cout << "1. Generate graph\n";
        std::cout << "2. Get path\n";
        std::cout << "3. Quit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter word length: ";
                int length;
                std::cin >> length;
                p.generateGraph(length);
                std::cout << "Graph generated!\n";
                break;
            case 2:
                std::cout << "Enter start word: ";
                std::cin >> word1;
                std::cout << "Enter end word: ";
                std::cin >> word2;
                path = p.getPath(word1, word2);
                std::cout << "Path found:\n";
                for (const auto& it : path) {
                    std::cout << it << " ";
                }
                std::cout << "\n";
                break;
            case 3:
                std::cout << "Goodbye!\n";
                break;
            default:
                std::cout << "Invalid choice!\n";
                break;
        }
    } while (choice != 3);

    return 0;
}

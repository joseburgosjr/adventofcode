#include <cstdio>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./solution <input_file>\n");
        return 1;
    }

    ifstream input(argv[1]);
    if (!input.is_open())
    {
        printf("Could not open file: %s\n", argv[1]);
        return 1;
    }

    int answer = 0;
    int dial = 1000000000 + 50;

    string line;
    while (getline(input, line))
    {
        const int rotateBy = stoi(line.substr(1));
        for (int i = 0; i < rotateBy; i++)
        {
            if (line[0] == 'L')
            {
                dial -= 1;
            }
            else
            {
                dial += 1;
            }

            if ((dial % 100) == 0)
            {
                answer++;
            }
        }
    }

    printf("Answer: %d\n", answer);
    return 0;
}

#include <iostream>
#include <vector>
using namespace std;

int main()
{

    int num = 0;

    cin >> num;

    vector<vector<double>> initmatrix(num, vector<double>(num, 0));

    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
        {
            cin >> initmatrix[i][j];
        }
    }

    int counter = 1;
    while (true)
    {
        cin >> num;

        if (!cin)
            break;

        ++counter;

        double temp = 0.0;
        for (int i = 0; i < num; i++)
        {
            for(int j = 0; j < num; j++)
            {
                cin >> temp;

                initmatrix[i][j] += temp;
            }
        }
    }

    cout << num << endl;
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
        {
            cout << initmatrix[i][j] / counter << " ";
        }
        cout << '\n';
    }


return 0;
}

#include <iostream>
#include <vector>

using namespace std;

// Function to rotate the array
void rotateArr(int x, int y, int r, int z, vector<vector<int>> &arr)
{
    int startX = x - r, startY = y - r;
    int endX = x + r, endY = y + r;
    int arrSize = 2 * r + 1;

    // Extract the subarray
    vector<vector<int>> tmpArr(arrSize, vector<int>(arrSize));
    for (int i = startX; i <= endX; ++i)
    {
        for (int j = startY; j <= endY; ++j)
        {
            tmpArr[i - startX][j - startY] = arr[i][j];
        }
    }

    // Rotate the subarray
    vector<vector<int>> rotatedArr(arrSize, vector<int>(arrSize));
    if (z == 1)
    {
        for (int i = 0; i < arrSize; ++i)
        {
            for (int j = 0; j < arrSize; ++j)
            {
                rotatedArr[i][j] = tmpArr[j][2 * r - i];
            }
        }
    }
    else
    {
        for (int i = 0; i < arrSize; ++i)
        {
            for (int j = 0; j < arrSize; ++j)
            {
                rotatedArr[i][j] = tmpArr[2 * r - j][i];
            }
        }
    }

    // Update the original array
    for (int i = startX; i <= endX; ++i)
    {
        for (int j = startY; j <= endY; ++j)
        {
            arr[i][j] = rotatedArr[i - startX][j - startY];
        }
    }
}

int main()
{
    int n, m;
    cin >> n >> m;

    // Initialize the array
    vector<vector<int>> arr(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            arr[i][j] = n * i + j + 1;
        }
    }

    // Perform rotations
    for (int k = 0; k < m; ++k)
    {
        int x, y, r, z;
        cin >> x >> y >> r >> z;

        // Adjust coordinates for 0-based indexing
        x--;
        y--;

        if (r > 0)
        {
            rotateArr(x, y, r, z, arr);
        }
    }

    // Print the final array
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n - 1; ++j)
        {
            cout << arr[i][j] << " ";
        }
        cout << arr[i][n - 1] << endl;
    }

    return 0;
}

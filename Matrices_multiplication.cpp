#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;
using std::cerr;
using std::end;
using std::endl;

vector<vector<int>> multiplyMatrices(const vector<vector<int>>& A, const vector<vector<int>>& B) {
    int rowsA = A.size();
    int colsA = A[0].size();
    int rowsB = B.size();
    int colsB = B[0].size();

    vector<vector<int>> result(rowsA, vector<int>(colsB, 0));

    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            for (int k = 0; k < colsA; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return result;
}

void outMatrix(const vector<vector<int>>& matrix) {
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[i].size(); ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int rowsA, colsA, rowsB, colsB;

    cin >> rowsA >> colsA;
    cin >> rowsB >> colsB;

    if (colsA != rowsB) {
        cerr << "Error: Matrices cannot be multiplied, size mismatch" << endl;
        return 1;
    }

    vector<vector<int>> A(rowsA, vector<int>(colsA));
    for (int i = 0; i < rowsA; ++i)
        for (int j = 0; j < colsA; ++j)
            cin >> A[i][j];

    vector<vector<int>> B(rowsB, vector<int>(colsB));
    for (int i = 0; i < rowsB; ++i)
        for (int j = 0; j < colsB; ++j)
            cin >> B[i][j];

    vector<vector<int>> result = multiplyMatrices(A, B);
    outMatrix(result);

    return 0;
}

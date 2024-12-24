void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    
    int n = matrixSize;
    int m = matrixColSize[0];
    int row[n];
    int col[m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (matrix[i][j] == 0)
            {
                row[i] = 1;
                col[j] = 1;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (row[i] == 1)
        {
            for (int j = 0; j < m; j++)
            {
                matrix[i][j] = 0;
            }
        }
    }
    for (int i = 0; i < m; i++)
    {
        if (col[i] == 1)
        {
            for (int j = 0; j < n; j++)
            {
                matrix[j][i] = 0;
            }
        }
    }

}

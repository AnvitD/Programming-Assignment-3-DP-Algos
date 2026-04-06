# Programming-Assignment-3-DP-Algos

Anvit Dhamnekar 15965003
Kalim Qazi 85459363

How to Run this code. 

File Format: 

    src\
        main.py
        graph.py
    tests\
        all test .in and .out files
    results\
        plot and timining data.


to run this project you can simply go to main.py and run the file. Make sure to be in the parent directory so the code is able to find the required test files and the tests directory. Doing this it will automatically go through all 10 .in files and create thier subsequent .out files. 

The graph.py file can also be run to create the .out files and the timing graph along with a .csv with all the timing data. 

Q1 

<img width="1500" height="750" alt="image" src="https://github.com/user-attachments/assets/30907e6c-7978-465a-89b6-ab05c9e1a3eb" />


Q2 

Let dp[i][j] be the maximum value of any common subsequence of the first i characters of A
and the first j characters of B.
Base case: dp[i][0] = dp[0][j] = 0, since an empty prefix has no characters.
Recurrence: If A[i] == B[j], then dp[i][j] = dp[i-1][j-1] + v(A[i]). Otherwise, dp[i][j] =
max(dp[i-1][j], dp[i][j-1]).
This is correct because when characters match we take that character and add its value to
the best solution on the remaining prefixes. When they don't match, we skip one character
from either A or B and take the better result. The answer is dp[m][n].

Q3

HVLCS(A, B):
set every dp[i][0] to 0 for all i (empty B has no value)
set every dp[0][j] to 0 for all j (empty A has no value)
for each position i in A:
for each position j in B:
if the character A[i] equals B[j]:
take this character and add its value to the best solution so far
dp[i][j] = dp[i-1][j-1] + v(A[i])
otherwise:
skip one character from either A or B, take whichever is better
dp[i][j] = max(dp[i-1][j], dp[i][j-1])

return dp[m][n] (this is the maximum value)
Runtime
O(mn)

class Solution {
public:
    string convert(string s, int numRows) {
        // Edge case: if rows = 1, the pattern is just the string itself
        if (numRows <= 1 || numRows >= s.length()) return s;

        vector<string> rows(min(numRows, (int)s.length()));
        int currentRow = 0;
        bool goingDown = false;

        for (char c : s) {
            rows[currentRow] += c;
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }
            
            currentRow += goingDown ? 1 : -1;
        }
        string result;
        for (const string& row : rows) {
            result += row;
        }
        return result;
    }
};

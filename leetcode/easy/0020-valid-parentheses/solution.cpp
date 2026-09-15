class Solution {
public:
    bool isValid(string s) {

        stack<char> st;

        for (char ch : s) {

            // Opening brackets
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            }

            // Closing brackets
            else {

                if (st.empty())
                    return false;

                if ((ch == ')' && st.top() == '(') ||
                    (ch == '}' && st.top() == '{') ||
                    (ch == ']' && st.top() == '[')) {

                    st.pop();
                }
                else {
                    return false;
                }
            }
        }

        return st.empty();
    }
};
            
        
        
   
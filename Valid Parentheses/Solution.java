class Solution {
    public boolean isValid(String s) {        
        Stack st = new Stack();
        
        for (int i=0; i<s.length(); i++) {
            if ((s.charAt(i)=='(') || (s.charAt(i)=='{') || (s.charAt(i)=='[')) {
                st.push(s.charAt(i));
            }
            else {
                if (st.empty()) {
                    return false;
                }
                if (s.charAt(i) == ')') {
                    char top = (Character) st.pop();
                    if (top != '('){
                        return false;
                    }
                }
                else if (s.charAt(i) == '}') {
                    char top = (Character) st.pop();
                    if (top != '{'){
                        return false;
                    }
                }
                else if (s.charAt(i) == ']') {
                    char top = (Character) st.pop();
                    if (top != '['){
                        return false;
                    }
                }
            }
        }
        return (st.empty());
    }
}
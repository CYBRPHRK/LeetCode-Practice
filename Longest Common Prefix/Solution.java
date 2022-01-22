class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        int index = 0;
        int i = 0;
        while(i<=200){
            if(strs[0].length() > index){
                char check = strs[0].charAt(index);
                for (i=1; i<strs.length; i++){
                    if ((strs[i].length() <= index) || (check != strs[i].charAt(index))){
                        return prefix;
                    }
                }
                prefix = prefix + strs[0].charAt(index);
                index++;
            }
            else{
                return prefix;
            }
        }
        return null;
    }
}
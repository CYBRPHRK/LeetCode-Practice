class Solution {
    public int romanToInt(String s) {
        int num = 0;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        
        for(int i=0; i<s.length(); i++){
            if (i < s.length() - 1){
                switch(s.charAt(i)){
                    case 'I':
                        if((s.charAt(i+1) == 'V') || (s.charAt(i+1) == 'X')){
                            num = num + map.get(s.charAt(i+1)) - 1;
                            i++;
                        }
                        else{
                            num = num + 1;
                        }
                        break;
                    case 'X':
                        if((s.charAt(i+1) == 'L') || (s.charAt(i+1) == 'C')){
                            num = num + map.get(s.charAt(i+1)) - 10;
                            i++;
                        }
                        else{
                            num = num + 10;
                        }
                        break;
                    case 'C':
                        if((s.charAt(i+1) == 'D') || (s.charAt(i+1) == 'M')){
                            num = num + map.get(s.charAt(i+1)) - 100;
                            i++;
                        }
                        else{
                            num = num + 100;
                        }
                        break;
                    default:
                        num = num + map.get(s.charAt(i));
                }
            }
            else{
                num = num + map.get(s.charAt(i));
            }
        }
        return num;
    }
}
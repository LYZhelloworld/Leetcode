class Solution {
    public int longestPalindrome(String s) {
        if(s.length() == 0) {
            return 0;
        }
        
        boolean allSame = true;
        for(int i = 1; i < s.length(); ++i) {
            if(s.charAt(i) != s.charAt(0)) {
                allSame = false;
                break;
            }
        }
        if(allSame) {
            return s.length();
        }
        
        StringBuilder sb = new StringBuilder(s);
        int count = 0;
        for(int i = 0, n; sb.length() > 1 && i < sb.length();) {
            n = sb.indexOf(Character.toString(sb.charAt(i)), i + 1);
            if(n != -1) {
                sb.deleteCharAt(n);
                sb.deleteCharAt(i);
                count += 2;
            } else
                ++i;
        }
        
        if(sb.length() > 0) {
            ++count;
        }
        return count;
    }
}

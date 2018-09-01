import java.util.*;

class Solution {
    public String longestPalindrome(String s) {
        if(s.length() == 0) {
            return "";
        }
        
        List<Integer> list2Core = find2Core(s);
        List<Integer> list3Core = find3Core(s);
        
        List<String> substrs = new LinkedList();
        for(int core : list2Core) {
            substrs.add(check2Core(s, core));
        }
        for(int core : list3Core) {
            substrs.add(check3Core(s, core));
        }
        
        if(substrs.isEmpty()) {
            return Character.toString(s.charAt(0));
        }
        return Collections.max(substrs, Comparator.comparing(k -> k.length()));
    }
    
    public List<Integer> find2Core(String s) {
        // Find substrings like "bb"
        // Keep the position of first character
        List<Integer> result = new LinkedList();
        for(int i = 0; i < s.length() - 1; ++i) {
            if(s.charAt(i) == s.charAt(i + 1)) {
                result.add(i);
            }
        }
        return result;
    }
    
    public List<Integer> find3Core(String s) {
        // Find substrings like "bab" or "bbb"
        // Keep the position of second character
        List<Integer> result = new LinkedList();
        for(int i = 0; i < s.length() - 2; ++i) {
            if(s.charAt(i) == s.charAt(i + 2)) {
                result.add(i + 1);
            }
        }
        return result;
    }
    
    public String check2Core(String s, int pos) {
        // Check if we can extend the substring while keeping it palindromic
        // Return substring
        String substr = s.substring(pos, pos + 2);
        for(int i = 1; pos - i >= 0 && pos + i + 1 < s.length(); ++i) {
            if(s.charAt(pos - i) == s.charAt(pos + i + 1)) {
                substr = "" + s.charAt(pos - i) + substr + s.charAt(pos + i + 1);
            } else {
                break;
            }
        }
        return substr;
    }
    
    public String check3Core(String s, int pos) {
        // Check if we can extend the substring while keeping it palindromic
        // Return substring
        String substr = s.substring(pos - 1, pos + 2);
        for(int i = 1; pos - i - 1 >= 0 && pos + i + 1 < s.length(); ++i) {
            if(s.charAt(pos - i - 1) == s.charAt(pos + i + 1)) {
                substr = "" + s.charAt(pos - i - 1) + substr + s.charAt(pos + i + 1);
            } else {
                break;
            }
        }
        return substr;
    }
}

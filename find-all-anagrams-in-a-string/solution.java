class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        if(s.length() < p.length()) return new LinkedList<>();
        
        List<Integer> result = new LinkedList<>();
        Map<Character, Integer> mp = new HashMap<>();
        Map<Character, Integer> ms = new HashMap<>();
        
        char[] pArray = p.toCharArray();
        for(char c : pArray) {
            if(mp.containsKey(c)) {
                mp.put(c, mp.get(c) + 1);
            } else {
                mp.put(c, 1);
            }
        }
        
        char[] sArray = s.toCharArray();
        for(int i = 0; i < p.length(); i++) {
            if(ms.containsKey(sArray[i])) {
                ms.put(sArray[i], ms.get(sArray[i]) + 1);
            } else {
                ms.put(sArray[i], 1);
            }
        }
        
        if(mp.equals(ms)) result.add(0);
        int length_diff = s.length() - p.length();
        
        for(int i = 1; i <= length_diff; i++) {
            char old_char = sArray[i - 1];
            char new_char = sArray[i + p.length() - 1];
            
            ms.put(old_char, ms.get(old_char) - 1);
            if(ms.get(old_char) == 0) {
                ms.remove(old_char);
            }
            
            if(ms.containsKey(new_char)) {
                ms.put(new_char, ms.get(new_char) + 1);
            } else {
                ms.put(new_char, 1);
            }
            
            if(mp.equals(ms)) result.add(i);
        }
        
        return result;
    }
}

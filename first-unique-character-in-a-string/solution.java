class Solution {
    public int firstUniqChar(String s) {
        Map<Character, int[]> count = new HashMap<>();
        char c;
        
        for(int i = 0; i < s.length(); ++i) {
            c = s.charAt(i);
            if(count.containsKey(new Character(c))) {
                count.get(new Character(c))[0]++;
            } else {
                count.put(new Character(c), new int[]{1, i});
            }
        }
        
        int result = Integer.MAX_VALUE;
        for(Map.Entry<Character, int[]> entry : count.entrySet()) {
            if(entry.getValue()[0] == 1)
                if(entry.getValue()[1] < result)
                    result = entry.getValue()[1];
        }
        
        if(result != Integer.MAX_VALUE) {
            return result;
        } else {
            return -1;
        }
    }
}

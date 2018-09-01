class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxSubStr = 0, length;
        String tmpStr = "";
        
        for(char c : s.toCharArray()) {
            if(tmpStr.indexOf(c) == -1) {
                tmpStr += c;
            } else {
                length = tmpStr.length();
                if(length > maxSubStr) {
                    maxSubStr = length;
                }
                tmpStr = tmpStr.substring(tmpStr.lastIndexOf(c) + 1) + c;
            }
        }
        
        length = tmpStr.length();
        if(length > maxSubStr) {
            maxSubStr = length;
        }
        return maxSubStr;
    }
}

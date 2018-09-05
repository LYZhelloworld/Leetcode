class Solution {
    public char findTheDifference(String s, String t) {
        StringBuilder sb = new StringBuilder(t);
        for(char c : s.toCharArray()) {
            sb.deleteCharAt(sb.indexOf(Character.toString(c)));
        }
        return sb.charAt(0);
    }
}

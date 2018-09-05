class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        StringBuilder sb = new StringBuilder(magazine);
        int i;
        
        for(char c : ransomNote.toCharArray()) {
            if((i = sb.indexOf(Character.toString(c))) != -1)
                sb.deleteCharAt(i);
            else
                return false;
        }
        return true;
    }
}

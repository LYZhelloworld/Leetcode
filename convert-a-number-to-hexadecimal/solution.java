class Solution {
    private String hex = "0123456789abcdef";
    
    public String toHex(int num) {
        if(num == 0) return "0";
        
        long numL = Integer.toUnsignedLong(num);
        int r;
        StringBuilder sb = new StringBuilder();
        while(numL > 0) {
            r = (int) (numL % 16);
            sb.append(hex.charAt(r));
            numL /= 16L;
        }
        return sb.reverse().toString();
    }
}

class Solution {
    public String licenseKeyFormatting(String S, int K) {
        StringBuilder sb = new StringBuilder();
        for(int i = S.length() - 1, j = 0; i >= 0; i--) {
            if(S.charAt(i) == '-') continue;
            sb.append(Character.toUpperCase(S.charAt(i)));
            j++;
            if(j % K == 0) {
                sb.append('-');
            }
        }
        if(sb.length() > 0 && sb.charAt(sb.length() - 1) == '-') sb.deleteCharAt(sb.length() - 1);
        return sb.reverse().toString();
    }
}

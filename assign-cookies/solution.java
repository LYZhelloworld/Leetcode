class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int i, j;
        Arrays.sort(s);
        Arrays.sort(g);
        for(i = 0, j = 0; i < s.length && j < g.length;) {
            if(g[j] <= s[i]) {
                i++;
                j++;
            } else {
                i++;
            }
        }
        return j;
    }
}

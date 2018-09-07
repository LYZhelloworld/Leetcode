class Solution {
    public boolean repeatedSubstringPattern(String s) {
        // If a string contains substring (ignore spaces): AAABBB AAABBB
        // Repeat it and cut the head and tail: AABBB AAABBB AAABBB AAABB
        // You still can find the string in the middle.
        //
        // If a string does not contain substring: AAABBBCCC
        // Do the same steps: AABBBCCC AAABBBCC
        // You are unable to find the pattern now.
        return (s + s).substring(1, s.length() * 2 - 1).contains(s);
    }
}

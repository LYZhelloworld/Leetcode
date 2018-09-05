class Solution {
    public String addStrings(String num1, String num2) {
        int a, b, s, c = 0;
        StringBuilder sb = new StringBuilder();
        if(num1.length() != num2.length()) {
            if(num1.length() > num2.length()) {
                num2 = new String(new char[num1.length() - num2.length()]).replace("\0", "0") + num2;
            } else {
                num1 = new String(new char[num2.length() - num1.length()]).replace("\0", "0") + num1;
            }
        }
        
        for(int i = num1.length() - 1; i >= 0; --i) {
            a = (int)(num1.charAt(i) - '0');
            b = (int)(num2.charAt(i) - '0');
            s = a + b + c;
            c = s / 10;
            s %= 10;
            sb.append((char)(s + '0'));
        }
        if(c > 0) sb.append(1);
        return sb.reverse().toString();
    }
}

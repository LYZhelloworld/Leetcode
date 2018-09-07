class Solution {
    public int findComplement(int num) {
        int mask = -1;
        int tmpNum = num;
        for(int c = 0; tmpNum != 0; tmpNum >>= 1, mask ^= (1 << c), c++);
        return ~num ^ mask;
    }
}

int getSum(int a, int b) {
    int addition, carry;

    for(;b != 0;) {
        addition = a ^ b;
        carry = a & b;
        b = carry << 1;
        a = addition;
    }
    return a;
}

int hammingWeight(uint32_t n) {
    int sum = 0;

    while(n) {
        sum++;
        n &= (n - 1);
        /*
        If there is 1 in N, suppose N will be like this:
        ...100000000
        Then N-1 will be like this:
        ...011111111
        AND them so that:
        ...000000000
        while the higher bits are not affected. Increase the counter by 1.
        */
    }
    return sum;
}

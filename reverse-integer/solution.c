int reverse(int x) {
    int result = 0, temp;

    for(;x != 0;) {
        temp = result * 10 + x % 10;
        if(temp / 10 != result) {
            return 0;
        }
        result = temp;
        x /= 10;
    }

    return result;
}

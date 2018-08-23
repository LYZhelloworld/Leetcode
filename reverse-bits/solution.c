uint32_t reverseBits(uint32_t n) {
    uint8_t bit = 0;
    uint8_t i;
    uint32_t result = 0;
    uint32_t input = n;

    for(i = 0; i < 32; ++i) {
        result = (result << 1) | (input % 2);
        input >>= 1;
    }
    return result;
}

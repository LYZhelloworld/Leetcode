class Solution {
    public int compress(char[] chars) {
        if(chars.length == 0) return 0;
        
        int currentPtr = 0, readingPtr = 0;
        int count = 1;
        char currentChar = chars[readingPtr];
        
        for(readingPtr = 1; readingPtr < chars.length; ++readingPtr) {
            if(chars[readingPtr] != currentChar) {
                // Character changed
                if(count == 1) {
                    // No compression. Continue.
                    chars[currentPtr] = currentChar;
                    currentPtr += 1;
                    currentChar = chars[readingPtr];
                    count = 1;
                } else {
                    chars[currentPtr] = currentChar;
                    char[] compressionValue = String.valueOf(count).toCharArray();
                    for(int i = 0; i < compressionValue.length; ++i) {
                        chars[currentPtr + i + 1] = compressionValue[i];
                    }
                    currentPtr += compressionValue.length + 1;
                    currentChar = chars[readingPtr];
                    count = 1;
                }
            } else {
                // No changes
                ++count;
            }
        }
        
        if(count == 1) {
            chars[currentPtr] = currentChar;
            return currentPtr + 1;
        } else {
            chars[currentPtr] = currentChar;
            char[] compressionValue = String.valueOf(count).toCharArray();
            for(int i = 0; i < compressionValue.length; ++i) {
                chars[currentPtr + i + 1] = compressionValue[i];
            }
            return currentPtr + compressionValue.length + 1;
        }
    }
}

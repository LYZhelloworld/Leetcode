/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int start = 0, end = n, mid = n / 2;
        int r;
        while(start <= end) {
            mid = start + (end - start) / 2;
            r = guess(mid);
            if(r > 0) {
                start = mid + 1;
            } else if(r < 0) {
                end = mid - 1;
            } else {
                break;
            }
        }
        return mid;
    }
}

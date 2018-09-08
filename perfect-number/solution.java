class Solution {
    public boolean checkPerfectNumber(int num) {
        switch(num) {
            case 6:
            case 28:
            case 496:
            case 8128:
            case 33550336:
                return true;
            default:
                return false;
        }
    }
}

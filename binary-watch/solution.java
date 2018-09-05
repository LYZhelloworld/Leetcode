class Solution {
    private List<String[]> hours;
    private List<String[]> minutes;
    
    public List<String> readBinaryWatch(int num) {
        hours = new ArrayList<>();
        hours.add(new String[]{"0:"});
        hours.add(new String[]{"1:","2:","4:","8:"});
        hours.add(new String[]{"3:","5:","6:","9:","10:"});
        hours.add(new String[]{"7:","11:"});
        
        minutes = new ArrayList<>();
        minutes.add(new String[]{"00"});
        minutes.add(new String[]{"01","02","04","08","16","32"});
        minutes.add(new String[]{"03","05","06","09","10","12","17","18","20","24","33","34","36","40","48"});
        minutes.add(new String[]{"07","11","13","14","19","21","22","25","26","28","35","37","38","41","42","44","49","50","52","56"});
        minutes.add(new String[]{"58","57","54","53","51","46","45","43","39","30","29","27","23","15"});
        minutes.add(new String[]{"31","47","55","59"});
        
        List<String> times = new LinkedList<>();
        for(int i = 0; i < 4 && i <= num; ++i) {
            if(num - i >= 6) continue;
            times.addAll(getAllTimes(i, num - i));
        }
        return times;
    }
    
    private List<String> getAllTimes(int hour, int minute) {
        List<String> result = new LinkedList<>();
        for(String h : hours.get(hour)) {
            for(String m : minutes.get(minute)) {
                result.add(h + m);
            }
        }
        return result;
    }
}

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        if(root == null) return new LinkedList<List<Integer>>();
        Queue<Node> queue = new LinkedList<Node>();
        Queue<Node> tmpQueue;
        queue.add(root);
        List<List<Integer>> result = new LinkedList<>();
        
        while(!queue.isEmpty()) {
            tmpQueue = new LinkedList<Node>();
            List<Integer> newLevel = new LinkedList<>();
            Node n;
            while((n = queue.poll()) != null) {
                newLevel.add(n.val);
                for(Node child : n.children) {
                    tmpQueue.add(child);
                }
            }
            queue = tmpQueue;
            result.add(newLevel);
        }
        return result;
    }
}

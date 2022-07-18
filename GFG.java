// JAVA code for the above approach
import java.util.*;
class GFG
{

     public static class Node {
        int value;
        Node left, right;
    }
    public static Node newNode(int data)
    {
        Node temp = new Node();
        temp.value = data;
        temp.left = temp.right = null;
        return temp;
    }
    // DFS function to convert
    // binary tree to proper tree
    public static void dfs(Node root)
    {

        if (root == null)
        return;

        if (root.left != null && root.left.value % 2 == 1) {
        root.left.value -= 1;
        count_of_changes++;
        }

        if (root.right != null && root.right.value % 2 == 0) {
        root.right.value += 1;
        count_of_changes++;
        }
        dfs(root.left);

        dfs(root.right);
    }

     /* using array for implementing queue  */
    static void printLevelOrder(Node root)
    {
        Queue<Node> queue = new LinkedList<Node>();
      
        queue.add(root);
        while (!queue.isEmpty()) {
 
            /* poll() removes the present head.
            For more information on poll() visit
            http://www.tutorialspoint.com/java/
            util/linkedlist_poll.htm */
            Node tempNode = queue.poll();
            System.out.print(tempNode.data + " ");
 
            /*Enqueue left child */
            if (tempNode.left != null) {
                queue.add(tempNode.left);
            }
 
            /*Enqueue right child */
            if (tempNode.right != null) {
                queue.add(tempNode.right);
            }
        }
    }


    // Driver code
    public static void main(String[] args)
    {
        // Taking input
        Node root = newNode(1);
        root.left = newNode(2);
        root.right = newNode(2);
        root.left.left = newNode(5);
        root.right.left = newNode(6);
        root.right.right = newNode(8);
        dfs(root);
        // Function call
       printLevelOrder(root);

    }
}

// This code is contributed by jana_sayantan.

import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {

        int n = Integer.parseInt(br.readLine());
        Node root = new Node();

        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());

            Node currentNode = root;

            for(int j=1; j<=k; j++) {
                currentNode = currentNode.addChildNode(j, st.nextToken());
            }
        }

        root.printChildNodes();

        bw.flush();
        br.close();
        bw.close();
    }

    private static class Node {
        private final String name;
        private final Map<String, Node> childNodes = new TreeMap<>();
        private final int floor;
        public Node() {
            floor = 1;
            name = null;
        }

        public Node(int depth, String name) {
            this.floor = depth;
            this.name = name;
        }

        public String getName() {
            return name;
        }

        public Node addChildNode(int depth, String name) {
            if(!childNodes.containsKey(name))
                childNodes.put(name, new Node(depth, name));

            return childNodes.get(name);
        }

        public void printChildNodes() throws IOException {
            if(name != null) {
                StringBuilder sb = new StringBuilder();
                for(int i=2; i<=floor; i++) {
                    sb.append("--");
                }
                sb.append(getName());
                sb.append("\n");
                bw.write(sb.toString());
            }

            for(Node childNode : childNodes.values()) {
                childNode.printChildNodes();
            }
        }
    }
}
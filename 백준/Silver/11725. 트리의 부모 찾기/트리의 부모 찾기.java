import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        Map<Integer, List<Integer>> tree = new HashMap<>();

        for(int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());

            if(!tree.containsKey(node1))
                tree.put(node1, new ArrayList<>());
            if(!tree.containsKey(node2))
                tree.put(node2, new ArrayList<>());

            tree.get(node1).add(node2);
            tree.get(node2).add(node1);
        }

        int[] result = new int[n + 1];

        Set<Integer> visited = new HashSet<>();
        Deque<Integer> stack = new ArrayDeque<>();

        stack.addLast(1);

        while(!stack.isEmpty()) {
            int parentNode = stack.removeLast();
            visited.add(parentNode);

            for(int childNode : tree.get(parentNode)) {
                if(visited.contains(childNode))
                    continue;

                stack.addLast(childNode);
                result[childNode] = parentNode;
            }
        }

        for(int i=2; i<=n; i++) {
            bw.write(result[i] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
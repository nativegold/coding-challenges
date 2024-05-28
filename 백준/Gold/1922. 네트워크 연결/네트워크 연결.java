import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[] parent = new int[n + 1];

        for(int i=0; i<=n; i++) {
            parent[i] = i;
        }

        List<Edge> edges = new ArrayList<>();

        for(int i=0; i<m; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());

            int v1 = Integer.parseInt(st2.nextToken());
            int v2 = Integer.parseInt(st2.nextToken());
            int cost = Integer.parseInt(st2.nextToken());

            edges.add(new Edge(v1, v2, cost));
        }

        Collections.sort(edges);

        int totalCost = 0;
        for(Edge edge : edges) {
            if(find(parent, edge.getV1()) != find(parent, edge.getV2())) {
                union(parent, edge.getV1(), edge.getV2());
                totalCost += edge.getCost();
            }
        }

        bw.write(totalCost + "\n");

        bw.flush();
        bw.close();
        br.close();
    }

    private static void union(int[] parent, int v1, int v2) {
        v1 = find(parent, v1);
        v2 = find(parent, v2);

        if(v1 < v2) {
            parent[v2] = v1;
        } else {
            parent[v1] = v2;
        }
    }

    private static int find(int[] parent, int v) {
        if(parent[v] == v) {
            return v;
        } else {
            parent[v] = find(parent, parent[v]);
            return parent[v];
        }
    }

    private static class Edge implements Comparable<Edge> {
        private final int v1;
        private final int v2;
        private final int cost;

        public Edge(int v1, int v2, int cost) {
            this.v1 = v1;
            this.v2 = v2;
            this.cost = cost;
        }

        public int getV1() {
            return v1;
        }

        public int getV2() {
            return v2;
        }

        public int getCost() {
            return cost;
        }

        @Override
        public int compareTo(Edge e) {
            return cost - e.cost;
        }
    }
}
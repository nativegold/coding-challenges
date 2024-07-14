import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader br;
    private static BufferedWriter bw;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int K = Integer.parseInt(st.nextToken());

            if(K == 0) {
                break;
            }

            Integer[] S = new Integer[K];
            boolean[] visited = new boolean[K];

            for(int i=0; i<K; i++) {
                S[i] = Integer.parseInt(st.nextToken());
            }
            dfs(S, new ArrayList<>(), visited, 0, 0);

            bw.write("\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }

    public static void dfs(
            Integer[] S,
            List<Integer> caseOfLotto,
            boolean[] visited,
            int currentNumberIdx,
            int depth
    ) throws IOException {
        if(depth == 6) {
            for(int i=0; i<caseOfLotto.size(); i++) {
                bw.write(caseOfLotto.get(i) + " ");
            }
            bw.write("\n");
            return;
        }

        for(int i=currentNumberIdx; i<S.length; i++) {
            if(visited[i] == false) {
                visited[i] = true;
                caseOfLotto.add(S[i]);
                dfs(S, caseOfLotto, visited, i + 1, depth + 1);
                caseOfLotto.remove(caseOfLotto.size() - 1);
                visited[i] = false;
            }
        }
    }
}
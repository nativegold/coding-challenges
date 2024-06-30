import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        List<Integer> results = new ArrayList<>();

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            int[] prices = new int[n];
            for (int j = 0; j < n; j++) {
                prices[j] = Integer.parseInt(st.nextToken());
            }

            int m = Integer.parseInt(br.readLine());

            int[] cases = new int[m + 1];
            cases[0] = 1;

            for (int j = 0; j < prices.length; j++) {
                for (int k = 0; k < cases.length; k++) {
                    if (k >= prices[j]) {
                        cases[k] += cases[k - prices[j]];
                    }
                }
            }

            results.add(cases[m]);
        }

        for (Integer result : results) {
            bw.write(result + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
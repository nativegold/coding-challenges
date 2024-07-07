import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st1 = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st1.nextToken());
        int M = Integer.parseInt(st1.nextToken());

        int[][] array = new int[N][M];

        for(int i = 0; i < N; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());

            for(int j = 0; j < M; j++) {
                array[i][j] = Integer.parseInt(st2.nextToken());
            }
        }

        int K = Integer.parseInt(br.readLine());

        for(int i = 0; i < K; i++) {
            StringTokenizer st3 = new StringTokenizer(br.readLine());
            int I = Integer.parseInt(st3.nextToken()) - 1;
            int J = Integer.parseInt(st3.nextToken()) - 1;
            int X = Integer.parseInt(st3.nextToken()) - 1;
            int Y = Integer.parseInt(st3.nextToken()) - 1;

            int result = 0;
            for(int j = I; j <= X; j++) {
                for(int k = J; k <= Y; k++) {
                    result += array[j][k];
                }
            }

            bw.write(result + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
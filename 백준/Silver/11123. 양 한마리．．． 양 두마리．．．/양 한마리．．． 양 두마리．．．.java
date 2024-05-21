import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int testCaseCount = Integer.parseInt(br.readLine());
        for(int i=0; i<testCaseCount; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            String[][] matrix = new String[h][w];
            boolean[][] visited = new boolean[h][w];

            for(int j=0; j<h; j++) {
                String[] line = br.readLine().split("");
                for(int k=0; k<w; k++) {
                    matrix[j][k] = line[k];
                    visited[j][k] = false;
                }
            }

            int countSheepGroup = 0;

            for(int j=0; j<h; j++) {
                for(int k=0; k<w; k++) {
                    if(!matrix[j][k].equals(".") && !visited[j][k]) {
                        countSheepGroup += 1;
                    }
                    findSheep(matrix, visited, w, h, k, j);
                }
            }

            bw.write(countSheepGroup + "\n");
        }

        bw.flush();
        bw.close();
    }

    private static void findSheep(String[][] matrix, boolean[][] visited, int w, int h, int x, int y) {
        if(x < 0 || x >= w) {
            return;
        }

        if(y < 0 || y >= h) {
            return;
        }

        if(matrix[y][x].equals(".") || visited[y][x]) {
            return;
        }

        visited[y][x] = true;

        findSheep(matrix, visited, w, h,x + 1, y);
        findSheep(matrix, visited, w, h, x - 1, y);
        findSheep(matrix, visited, w, h, x, y - 1);
        findSheep(matrix, visited, w, h, x, y + 1);
    }
}
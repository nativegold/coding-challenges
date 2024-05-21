import java.io.*;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    private static final String[][] digitMatrix = new String[5][5];
    private static final Set<String> result = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for(int i=0; i<5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            for(int j=0; j<5; j++) {
                digitMatrix[i][j] = st.nextToken();
            }
        }

        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++) {
                findPath("", i, j);
            }
        }

        bw.write(String.valueOf(result.size()));

        bw.flush();
        bw.close();
    }

    private static void findPath(String path, int x, int y) {
        if(path.length() == 6) {
            result.add(path);
            return;
        }

        if(x < 0 || x >= 5) {
            return;
        }

        if(y < 0 || y >= 5) {
            return;
        }

        String currentPath = path + digitMatrix[y][x];

        findPath(currentPath, x + 1, y);
        findPath(currentPath, x - 1, y);
        findPath(currentPath, x, y + 1);
        findPath(currentPath, x, y - 1);
    }
}
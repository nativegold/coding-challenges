import java.io.*;

public class Main {
    private static String[][] videoBits;

    public static String makeQuardTree(int startX, int startY, int length) {
        String firstColor = videoBits[startY][startX];

        for(int i=startY; i<startY+length; i++) {
            for(int j=startX; j<startX+length; j++) {
                if(!firstColor.equals(videoBits[i][j])) {
                    int midX = startX + (length / 2);
                    int midY = startY + (length / 2);

                    return "("
                            + makeQuardTree(startX, startY, length / 2)
                            + makeQuardTree(midX, startY, length / 2)
                            + makeQuardTree(startX, midY, length / 2)
                            + makeQuardTree(midX, midY, length / 2)
                            + ")";
                }
            }
        }

        return firstColor;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        videoBits = new String[n][n];

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split("");
            for (int j = 0; j < n; j++) {
                videoBits[i][j] = line[j];
            }
        }

        bw.write(makeQuardTree(0, 0, n));

        bw.flush();
        br.close();
        bw.close();
    }
}
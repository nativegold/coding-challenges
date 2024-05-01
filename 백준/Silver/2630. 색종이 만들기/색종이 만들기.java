import java.util.Scanner;

public class Main {
    public static void makeColorPaper(int[][] paper, int[] count, int x1, int x2, int y1, int y2) {
        int firstColor = paper[x1][y1];

        for(int i=x1; i<x2; i++) {
            for(int j=y1; j<y2; j++) {
                if(firstColor != paper[i][j]) {
                    int midX = (x1 + x2) / 2;
                    int midY = (y1 + y2) / 2;
                    makeColorPaper(paper, count, x1, midX, y1, midY);
                    makeColorPaper(paper, count, midX, x2, y1, midY);
                    makeColorPaper(paper, count, x1, midX, midY, y2);
                    makeColorPaper(paper, count, midX, x2, midY, y2);
                    return;
                }
            }
        }

        if(firstColor == 0)
            count[0]++;
        else
            count[1]++;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[][] paper = new int[n][n];
        int[] count = {0, 0};

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                paper[i][j] = scanner.nextInt();
            }
        }

        makeColorPaper(paper, count, 0, n, 0, n);

        System.out.println(count[0]);
        System.out.println(count[1]);
    }
}
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        List<Long> solutions = new ArrayList<>();

        for(int i=0; i<n; i++) {
            solutions.add(Long.parseLong(st.nextToken()));
        }

        int i = 0;
        int j = n - 1;
        long result = Long.MAX_VALUE;

        while(i < j) {
            long madeValue = solutions.get(i) + solutions.get(j);

            if(madeValue == 0) {
                result = 0;
                break;
            } else if(madeValue < 0) {
                i++;
            } else {
                j--;
            }

            if(Math.abs(result) > Math.abs(madeValue))
                result = madeValue;
        }

        bw.write(String.valueOf(result));
        bw.flush();
        br.close();
        bw.close();
    }
}
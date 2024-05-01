import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        List<Integer> tastes = new ArrayList<>();

        for(int i = 0; i < n; i++) {
            tastes.add(Integer.parseInt(st.nextToken()));
        }

        int k = Integer.parseInt(br.readLine());
        int bufferSize = n / k;
        List<Integer> answer = new ArrayList<>();

        for(int i = 0; i < n; i += bufferSize) {
            List<Integer> buffer = new ArrayList<>(tastes.subList(i, i+bufferSize));
            Collections.sort(buffer);
            answer.addAll(buffer);
        }

        for(int num : answer) {
            bw.write(num + " ");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
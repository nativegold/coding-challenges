import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        List<Integer> materials = new ArrayList<>();

        for(int i=0; i<n; i++) {
            materials.add(Integer.parseInt(st.nextToken()));
        }

        materials.sort((x, y) -> x - y);

        int i = 0;
        int j = n - 1;
        int result = 0;

        while(i < j) {
            if(materials.get(i) + materials.get(j) == m) {
                result++;
                i++;
                j--;
            } else if(materials.get(i) + materials.get(j) > m) {
                j--;
            } else if(materials.get(i) + materials.get(j) < m) {
                i++;
            }
        }

        bw.write(String.valueOf(result));
        bw.flush();
        br.close();
        bw.close();
    }
}
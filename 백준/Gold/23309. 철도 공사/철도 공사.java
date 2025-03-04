import java.io.*;
import java.util.*;

class Node {
    int stationNumber;
    Node previous;
    Node next;

    Node(int stationNumber) {
        this.stationNumber = stationNumber;
    }
}

public class Main {
    static BufferedWriter write = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void bn(Node[] stationArray, int i, int j) throws IOException {
        if (stationArray[j] != null) return;

        Node nodeI = stationArray[i];
        Node nextNode = nodeI.next;

        Node newNode = new Node(j);
        newNode.next = nextNode;
        newNode.previous = nodeI;

        nodeI.next = newNode;
        nextNode.previous = newNode;

        stationArray[j] = newNode;

        write.write(nextNode.stationNumber + "\n");
    }

    public static void bp(Node[] stationArray, int i, int j) throws IOException {
        if (stationArray[j] != null) return;

        Node nodeI = stationArray[i];
        Node previousNode = nodeI.previous;

        Node newNode = new Node(j);
        newNode.previous = previousNode;
        newNode.next = nodeI;

        nodeI.previous = newNode;
        previousNode.next = newNode;

        stationArray[j] = newNode;

        write.write(previousNode.stationNumber + "\n");
    }

    public static void cn(Node[] stationArray, int i) throws IOException {
        Node nodeI = stationArray[i];

        Node nextNode = nodeI.next;

        nodeI.next = nextNode.next;
        nextNode.next.previous = nodeI;

        stationArray[nextNode.stationNumber] = null;

        write.write(nextNode.stationNumber + "\n");
    }

    public static void cp(Node[] stationArray, int i) throws IOException {
        Node nodeI = stationArray[i];

        Node previousNode = nodeI.previous;

        nodeI.previous = previousNode.previous;
        previousNode.previous.next = nodeI;

        stationArray[previousNode.stationNumber] = null;

        write.write(previousNode.stationNumber + "\n");
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        try {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            Node[] stationArray = new Node[10000001];

            st = new StringTokenizer(br.readLine());
            int firstStation = Integer.parseInt(st.nextToken());

            Node firstNode = new Node(firstStation);
            stationArray[firstStation] = firstNode;

            Node prevNode = firstNode;

            for (int i = 1; i < N; i++) {
                int stationNumber = Integer.parseInt(st.nextToken());
                Node newNode = new Node(stationNumber);
                stationArray[stationNumber] = newNode;

                prevNode.next = newNode;
                newNode.previous = prevNode;

                prevNode = newNode;
            }

            prevNode.next = firstNode;
            firstNode.previous = prevNode;

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                String constructionType = st.nextToken();

                int station = Integer.parseInt(st.nextToken());

                if (constructionType.equals("BN")) {
                    int newStation = Integer.parseInt(st.nextToken());
                    bn(stationArray, station, newStation);
                } else if (constructionType.equals("BP")) {
                    int newStation = Integer.parseInt(st.nextToken());
                    bp(stationArray, station, newStation);
                } else if (constructionType.equals("CN")) {
                    cn(stationArray, station);
                } else if (constructionType.equals("CP")) {
                    cp(stationArray, station);
                }
            }

            write.flush();
        } finally {
            br.close();
            write.close();
        }
    }
}
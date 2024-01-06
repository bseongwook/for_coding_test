class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        // 배열의 곱 -> m x n 배열(A)과 n x p 배열(B)이 곱해지면
        // A 배열의 1번째 행의 모든 요소와, B 배열의 1번째 열의 모든 요소 (n, n)
        // 얘네들을 곱해서 -> 행렬 곱을 한 1, 1 번째의 열의 값.
        // A 배열의 1번째 행의 모든 요소와, B 배열의 2번째 열의 모든 요소 (n, n)
        // -> 행렬 곱의 1, 2번째 값 (1행의 2열 값.)
        int row1 = arr1.length; // 각 배열의 행의 사이즈와 열의 사이즈
        int col1 = arr1[0].length; // 가장 먼저 요소의 길이를 검색해도...
        for (int r1 = 0; r1 < row1; r1++) {
            for (int c1 = 0; c1 < col1; c1++) {
                System.out.print(arr1[r1][c1]);
            }   
            System.out.println();
        } // 전체 2차원 배열의 탐색이 가능해짐.
        /*
        { 
            { 1, 1, 2 }, // 행렬 안의 행렬들의 갯수 r
            { 2, 3, 4 }, // 행렬 안의 행렬들의 요소 갯수 c
        }
        */
        int row2 = arr2.length; // 각 배열의 행의 사이즈와 열의 사이즈
        int col2 = arr2[0].length; // 가장 먼저 요소의 길이를 검색해도...          
        for (int r2 = 0; r2 < row2; r2++) {
            for (int c2 = 0; c2 < col2; c2++) {
                System.out.print(arr2[r2][c2]);
            }   
            System.out.println();
        } // 전체 2차원 배열의 탐색이 가능해짐.
        int[][] answer = new int[row1][col2]; // m x n, n x p -> m x p
        for (int[] row: answer) {
            for (int col: row) { // 향상된 for문
                System.out.print(col);
            }
            System.out.println();
        }
        
        // row1 (m) col2(p) / col1, row1 (n)
        for (int r1 = 0; r1 < row1; r1++) { // 0 ~ m 
            for (int c2 =0; c2 < col2; c2++) { // 0 ~ p
                int sum = 0; // 행렬 간 곱셈 결과를 누적하는 수
                for (int v = 0; v < col1; v++) { // 0 ~ n
                    sum += arr1[r1][v] * arr2[v][c2];
                }
                answer[r1][c2] = sum; // 결과를 answer 배열에 넣어줌
            }
        }
        for (int[] row: answer) {
            for (int col: row) { // 향상된 for문
                System.out.print(col);
            }
            System.out.println();
        }
        return answer;
    }
}
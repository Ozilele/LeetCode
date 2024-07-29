// K Closest Points to Origin Problem
// https://leetcode.com/problems/k-closest-points-to-origin/

import java.util.Arrays;

class Solution {

    class PointDistance implements Comparable<PointDistance> {
        int[] point;
        int distance;

        public PointDistance(int[] point, int distance) {
            this.point = point;
            this.distance = distance;
        }

        @Override
        public int compareTo(PointDistance other) {
            return Integer.compare(this.distance, other.distance);
        }
    }

    public int calcDistance(int x1, int y1, int x2, int y2) {
        return (int)Math.pow(x1 - x2, 2) + (int)Math.pow(y1 - y2, 2);
    }

    public int[][] kClosest(int[][] points, int k) {
        PointDistance distances[] = new PointDistance[points.length];
        for(int i = 0; i < points.length; i++) {
            int distance_power_2 = calcDistance(points[i][0], points[i][1], 0, 0);
            distances[i] = new PointDistance(points[i], distance_power_2);
        }
        Arrays.sort(distances);  

        int[][] result = new int[k][2];
        for(int i = 0; i < k; i++) {
            result[i] = distances[i].point;
        }
        return result;
    }
}

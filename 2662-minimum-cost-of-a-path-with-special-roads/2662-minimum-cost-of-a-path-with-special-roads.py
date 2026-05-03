class Solution:
    def minimumCost(self, start, target, specialRoads):
        def dist(s, t):
            return abs(s[0] - t[0]) + abs(s[1] - t[1])

        heap = [(0, start[0], start[1])]
        visited = set()
        while heap:
            curr_c, curr_x, curr_y = heapq.heappop(heap)

            if curr_x == target[0] and curr_y == target[1]:
                return curr_c

            if (curr_x, curr_y) in visited:
                continue

            visited.add((curr_x, curr_y))

            heapq.heappush(heap, (curr_c + dist([curr_x, curr_y], target), target[0], target[1]))

            for x1, y1, x2, y2, c in specialRoads:
                to_special_road = curr_c + dist([curr_x, curr_y], [x1, y1]) + c
                heapq.heappush(heap, (to_special_road, x2, y2))
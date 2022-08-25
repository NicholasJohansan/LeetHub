class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_list_length = len(firstList)
        second_list_length = len(secondList)
        first_pointer = 0
        second_pointer = 0
        intersections = []
        while first_pointer < first_list_length and second_pointer < second_list_length:
            first_start, first_end = firstList[first_pointer]
            second_start, second_end = secondList[second_pointer]
            start = max(first_start, second_start)
            end = min(first_end, second_end)
            if start <= end:
                intersections.append([start, end])
            if first_end < second_end:
                first_pointer += 1
            else:
                second_pointer += 1
        return intersections
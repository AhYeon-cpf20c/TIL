import heapq # 모듈 불러오기
from heapq import heappush, heappop, heapify # 파일 안에 클래스, 함수

heap = [4, 15, 19, 11, 20, 13]
heapify(heap)   # python은 min heap 으로 구현

while heap:
    num = heappop(heap)
    print(num)

heappush(heap, 15)
def lastStoneWeight(stones):
    while len(stones) > 1:
        stone1 = max(stones)
        stones.remove(stone1)
        stone2 = max(stones)
        stones.remove(stone2)
        if stone1 != stone2:
            stone1 -= stone2
            stones.append(stone1)
    if stones:
        return stones[0]
    return 0


stones1 = [2, 7, 4, 1, 8, 1]
stones2 = [1, 4, 19, 30, 3, 1]
print(lastStoneWeight(stones1))
print(lastStoneWeight(stones2))

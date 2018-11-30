def insertion_sort(arr):
    #思路，从左往右起，从最左边的数字开始，每个数字和自己的左边相比,找到插入的位置。（保证每个数字的左边都是排好序的）
    # a1 a2 a3 target a5 a6
    # 若左边的数字比targey大，就让左边的数字往右移动一个，左边的数字an-1比target小 就把arr中an的这个位置赋值target
    # 如 a3 > target 将arr[3]（原来target的位置） = a3; a2 > target 则 arr[2]（原来a3的位置） = a2; a1 <= target 则 arr[1] = target 因为原来
    #arr[1]是a2 现在已经到了arr[2]第三个位置了，第二个位置空出来，放target
    for i in range(len(arr)):
        #创建target
        target = arr[i]
        #创建一个移动的指针用来比较target左边的数与target的大小
        tail =i
        #当这个tail没有到最左边arr[0]时
        #并且右边的数arr[tail-1]持续比target大时（只有arr[tail-1]比target小，我们才赋值arr[tail] = target）
        while tail >0 and arr[tail-1] > target:
            #将左边的数字向右移动
            arr[tail] = arr[tail-1]
            #指针向左移动一格，用来比较再右边一个与target
            tail -= 1
        #将target移动到正确的位置，因为arr[tail-1] <= target， 所以arr[tail] = target
        arr[tail] = target
    return arr

print('===============')
import random
arr = random.sample(range(1000), 10)
print('Input :', arr)
insertion_sort(arr)
print('Output:', arr)

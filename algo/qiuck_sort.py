
#quick_sort 思路：选第一个为pivot value 一个指针从下一个值开始往右
#另一个指针从tail往左
#两个指针分别找到往右和往左的第一个比pivot value大 和 小的值，调换两这个值顺序
#一直持续这样做（调换位置），知道左往右的指针大于右往左的指针，这时将pivot value和右往左指针的值互换位置
# 然后pivot value将arr分成了两快，左边时都小于该value的，右边是都大于该value的，此时对这两部分数据依然做相同的事情
def quick_sort(arr):
    def partition(arr, head, tail):
        pivot = head
        pivot_value = arr[pivot]
        #左指针,pivot value的下一个
        head = head + 1
        #右指针
        tail = tail
        #持续调换第一个比target大的值与第一个比target小的值得位置
        while True:
            #若左指针对应的值比target小，就将左指针向右移动
            if head <= tail and arr[head]<= pivot_value:
                head += 1
            #若右指针对应的值比target大，就把右指针向左移动
            if head <= tail and arr[tail]>= pivot_value:
                tail-=1
            #如果head超过了tail 说明我们遍历完了除pivot value的所有的数字, 交换位置的过程结束，应该到了讲pivot放在中间的时候了

            if tail < head:
                break
            #若没有超过，则交换大于target的值和小于taget的值得位置

            arr[head],arr[tail] = arr[tail],arr[head]
        #当tail<head以后，tail右边就都是大于target的值，tail位置的值以及他的右边就都是小于pivot的值，这是将pivot和tail值交换

        arr[pivot],arr[tail] = arr[tail],arr[pivot]
        #返回那个将arr一切为二的seperate的点，也就是tail，右指针
        return tail
    #再写一个分组递归的方法，有点类似于mergesort的方法
    def divide(arr, head,tail):
        #若分成不能再分了，就不能做什么事情了
        if head >= tail:
            return
        seperate = partition(arr,head,tail)
        divide(arr,head,seperate)
        divide(arr,seperate+1,tail)
    #调用divide的函数
    
    divide(arr,0,len(arr)-1)


print('===============')
import random
arr = random.sample(range(1000), 10)
print('Input :', arr)
quick_sort(arr)
print('Output:', arr)

        



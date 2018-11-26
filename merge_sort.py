
##merge sort思路：先把这串array 按一半一半持续divide 到一个一个，然后在从最底层merge上来
# merge时就是创建一个新的arr（代码中成为buff） = [None] * len(arr) , 然后两两merge时一次填入arr中去
#例如[10,74]和[34,98]依次填入arr的某个四个格子中，先10和34比，填入10 然后74和34比，填34 （变成10，34）
#然后98 和74比， 变成（10，34，74） 最后把多出来的98填入，变成（10，34，74，98）


def merge_sort(arr):
    #第一个函数
    def merge(arr,buff,head,tail):
        mid = (head + tail)//2
        #设左半块的指针（该指针对应的数值在大于右边指针的时候会向右移动）
        left_index = head
        #同理设右半块的指针
        right_index = mid+1
        #设置一个用来赋值到buff中的index(从head 到 tail)
        write = head
        #开始比较左右两边的数值(条件是指针都没有超过mid或tail)
        while left_index <= mid and right_index <= tail:
            if arr[left_index]<= arr[right_index]:
                #将较小的写入buff中
                buff[write] = arr[left_index]
                #移动index和左指针
                write += 1
                left_index += 1
            else:
                buff[write] = arr[right_index]
                #移动右指针
                write += 1
                right_index += 1
        #有可能左半块都填进去了,但是右半块还有东西
        if right_index <= tail:
            buff[write:tail+1] = arr[right_index:tail+1]
        #也有可能左半块还有东西
        elif left_index <= mid:
            buff[write:mid+1] = arr[left_index:mid+1]
        #将buff的值复制到arr中
        arr[head:tail+1] = buff[head:tail+1]
    
    #第二个函数:这是一个递归函数，一直分割arr直到head>= tail， 然后再从最底层一步步merge上来
    def divide(arr,buff,head,tail):
        if head >= tail:
            #不做任何事情
            return
        mid = (head+tail)//2
        #持续分割
        divide(arr,buff,head,mid)
        divide(arr,buff,mid+1,tail)
        #分到分不下去了（上面的divide(arr,buff,head,mid)）做不了事情return空值时，回来merge
        merge(arr,buff,head,tail)
    #最后创建新的空arr 也就是buff，然后call divide函数来操作arr
    buff = [None] * len(arr)
    #因为arr是list，在函数里对arr做的操作，函数外也会有改变
    divide(arr,buff,0,len(arr)-1)


print('===============')
import random
arr = random.sample(range(1000), 1)
print('Input :', arr)
merge_sort(arr)
print('Output:', arr)


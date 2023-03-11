# https://www.codingninjas.com/codestudio/problems/615?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1
def getInversions(nums, n):
    global_inversion = 0

    def merge(nums, left, mid, right):
        nonlocal global_inversion
        temp = list()
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                global_inversion += (mid - i + 1)
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

        for i in range(len(temp)):
            nums[left + i] = temp[i]

    def merge_sort(nums, left, right):
        if left >= right:
            return

        mid = left + (right - left) // 2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)
        merge(nums, left, mid, right)

    merge_sort(nums, 0, n - 1)
    return global_inversion

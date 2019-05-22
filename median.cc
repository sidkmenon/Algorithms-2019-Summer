#include <stdio.h>
#include <stdlib.h>


// ignore -- wrong algorithm!

double findMedianSortedArray(int* nums1, int nums1Size, int* nums2, int nums2Size);

int main()
{
  int* nums1 = (int*)malloc(2 * sizeof(int));
  nums1[0] = 1;
  nums1[1] = 2;
  int* nums2 = (int*)malloc(2 * sizeof(int));
  nums2[0] = 3;
  nums2[1] = 4;
  printf("%lf\n", findMedianSortedArray(nums1, 2, nums2, 2));
}


double findMedian(int* nums, int numsSize)
{
  if (numsSize % 2 == 0)
    return (double)(nums[numsSize/2 - 1] + nums[numsSize/2])/2;
  else
    return (double)nums[numsSize/2];
}
int half(int sz)
{
  return sz/2;
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
  if (nums1Size == 1 && nums2Size == 1)
    return (double)(*nums1 + *nums2)/2;
  else if (nums1Size > 0 && nums2Size > 0)
  {
    double med_1 = findMedian(nums1, nums1Size);
    double med_2 = findMedian(nums2, nums2Size);
    if (nums1Size == 2 && nums2Size == 2)
    {
      if (*nums1 <= *nums2 && *(nums1 + 1) >= *(nums2 + 1))
        return med_2;
      else if (*nums2 <= *nums1 && *(nums2 + 1) >= *(nums1 + 1))
        return med_1;
    }
    if (med_1 == med_2)
      return med_1;
    else if (med_1 > med_2)  // last half of 2, first half of 1
      return findMedianSortedArrays(nums1, half(nums1Size), nums2 + nums2Size/2 + nums2Size%2, half(nums2Size));
    else
      return findMedianSortedArrays(nums1 + nums1Size/2 + nums1Size%2, half(nums1Size), nums2, half(nums2Size));
  }
  else if (nums1Size > 0 && nums2Size <= 0)
    return findMedian(nums1, nums1Size);
  else if (nums1Size <= 0 && nums2Size > 0)
    return findMedian(nums2, nums2Size);
  else
    return - (double)1;
}

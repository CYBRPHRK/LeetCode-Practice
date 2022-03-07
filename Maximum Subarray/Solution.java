class Solution {
    public int maxSubArray(int[] nums) {
        int largest = nums[0];
        int sum = nums[0];
        for (int i=1; i<nums.length; i++){
            sum = Math.max(nums[i], nums[i] + sum);
            largest = Math.max(largest, sum);
        }
        return largest;
    }
}
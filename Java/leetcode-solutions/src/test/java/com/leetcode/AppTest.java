package com.leetcode;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

public class AppTest {
    @Test
    public void testTwoSum() {
        Solution solution = new Solution();
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        int[] result = solution.twoSum(nums, target);
        assertArrayEquals(new int[] { 0, 1 }, result);
    }
}
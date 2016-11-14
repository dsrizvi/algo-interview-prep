# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) < 1:
            return None
        return self.sortedArrayToBSTHelper(num, 0, len(num)-1)

    def sortedArrayToBSTHelper(self, num, start, end):
        if start > end:
            return None
        mid = (start+end)/2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBSTHelper(num, start, mid-1)
        root.right = self.sortedArrayToBSTHelper(num, mid+1, end)

        return root
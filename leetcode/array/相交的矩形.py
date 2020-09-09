# 836. Rectangle Overlap


class Solution:

    def isRectangleOverlap(self, rec1, rec2):

        #先判断不想交的情况：
        # rec1的x2小于rec2的x1；此时rec1在rec2的左边。
        # rec1的y2小于rec2的y1；此时rec1在rec2的下边。
        # rec2的x2小于rec1的x1；此时rec1在rec2的右边
        # rec2的y2小于rec1的y1；此时rec1在rec2的上边。
        # 取not代表相交的情况。
        
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2
        return not (rec1_x1 >= rec2_x2 or rec1_x2 <= rec2_x1 or rec1_y1 >= rec2_y2 or rec1_y2 <= rec2_y1)
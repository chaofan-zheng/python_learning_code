"""
数独是一个我们都非常熟悉的经典游戏，运用计算机我们可以很快地解开数独难题，现在有一些简单的数独题目，请编写一个程序求解。
如有多解，输出一个解
输入描述:
输入9行，每行为空格隔开的9个数字，为0的地方就是需要填充的。
输出描述:
输出九行，每行九个空格隔开的数字，为解出的答案。
"""
shudu01=list(input())
shudu02=list(input())
shudu03=list(input())
shudu04=list(input())
shudu05=list(input())
shudu06=list(input())
shudu07=list(input())
shudu08=list(input())
shudu09=list(input())
shudu = [shudu01,shudu02,shudu03,shudu04,shudu05,shudu06,shudu07,shudu08,shudu09]
"""
链接：https://www.nowcoder.com/questionTerminal/2b8fa028f136425a94e1a733e92f60dd?answerType=1&f=discussion
来源：牛客网

数独问题，可以拆分成两个子问题，一个是放置数字，一个是校验九宫格是否合法。
后者比较简单，对于前者这种穷举类的问题，一般采用回溯法来解决。

对于每一个待放置数字的位置，我们从1到9挨个往里面放，如果1-9以有一个数字合法的话，就移动到下一个待放置数字的位置，如果不合法，就回退到上一个待放置的位置。
具体操作代码解释的很清楚了。"""

# public class shudu {
#     /*
#     * 5 3 0 0 7 0 0 0 0
# 6 0 0 1 9 5 0 0 0
# 0 9 8 0 0 0 0 6 0
# 8 0 0 0 6 0 0 0 3
# 4 0 0 8 0 3 0 0 1
# 7 0 0 0 2 0 0 0 6
# 0 6 0 0 0 0 2 8 0
# 0 0 0 4 1 9 0 0 5
# 0 0 0 0 8 0 0 7 9
#     * */
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         //初始化数组
#         int[][] board = new int[9][9];
#         for (int i = 0; i < 9; i++) {
#             for (int j = 0; j < 9; j++) {
#                 board[i][j] = sc.nextInt();
#             }
#         }
#         solve(board);
#         //按要求输出结果
#         for (int[] i : board) {
#             for (int m = 0; m < 9; m++) {
#                 if (m == 8) {
#                     System.out.println(i[m]);
#                 } else {
#                     System.out.print(i[m] + " ");
#                 }
#             }
#         }
#     }
#
#     public static void solve(int[][] board) {
#         backtrack(board, 0, 0);
#     }
#
#     public static boolean backtrack(int[][] board, int i, int j) {
#         //走到了这一行的末尾，换行
#         if (j == 9) {
#             return backtrack(board, i + 1, 0);
#         }
#         //走到了第十行，说明前9行匹配成功，返回true。
#         if (i == 9) return true;
#         //如果这个数字不是0，跳过。
#         if (board[i][j] != 0) return backtrack(board, i, j + 1);
#
#         //在这个位置挨个放数字
#         for (int num = 1; num <= 9; num++) {
#             //如果这个位置放num不合法，就继续。
#             if (!check(board, i, j, num)) continue;
#
#             board[i][j] = num;
#             //如果接下来都合法，就返回true。
#             if (backtrack(board, i, j + 1)) return true;
#             //恢复现场
#             board[i][j] = 0;
#         }
#         //1-9都不行。
#         return false;
#     }
#
#     public static boolean check(int[][] board, int r, int c, int num) {
#         //检验当前位置如果放上num这个数字是不是合法的。
#         for (int i = 0; i < 9; i++) {
#             if (board[i][c] == num) return false;
#             if (board[r][i] == num) return false;
#             //判断小九宫格
#             if (board[(r / 3) * 3 + i / 3][(c / 3) * 3 + i % 3] == num) return false;
#         }
#         return true;
#     }
# }

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    bool checkMirror(TreeNode* ch1,TreeNode* ch2){
        if(ch1==nullptr && ch2==nullptr){
            return true;
        }
        else if(ch1 ==nullptr || ch2== nullptr){
            return false;
        }
        else{
            return ch1->val==ch2->val && checkMirror(ch1->left,ch2->right) && checkMirror(ch1->right,ch2->left); 
        }
    }
public:
    bool isSymmetric(TreeNode* root) {
        return checkMirror(root->left,root->right);
    }
};
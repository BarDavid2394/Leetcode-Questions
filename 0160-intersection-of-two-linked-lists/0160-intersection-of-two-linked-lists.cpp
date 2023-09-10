/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
       ListNode *res = 0;
       ListNode *A = headA;
       ListNode *B = headB;
       unordered_map <ListNode*, int > mapA;
       while(A){
           mapA[A] = 1;
           A = A->next;
       }
       while(B){
           if(mapA.count(B)){
               res = B;
               cout <<"Intersected at " << res->val;
               return res;
           }
           B = B->next;  
       }
        cout <<"No Intersection ";
        return res;
    }
};
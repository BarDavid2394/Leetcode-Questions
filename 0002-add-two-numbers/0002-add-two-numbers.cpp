/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sum_head = new ListNode(0);
        ListNode* sum_tail = sum_head;
        if(l1 == NULL)
            return l2;
        if(l2 == NULL)
            return l1;
        int carry = 0;
        int node_sum = 0;
        while(l1 && l2){
            node_sum = l1->val + l2->val + carry;
            if(node_sum >= 10){
                carry = 1;
                node_sum -=10;
            } else {
                carry = 0;
            }
            sum_tail->next = new ListNode(node_sum);
            
            sum_tail = sum_tail->next;
            l1 = l1->next;
            l2 = l2->next;
        }
       while(l1){
            node_sum = l1->val + carry;
            if(node_sum >= 10){
                carry = 1;
                node_sum -=10;
            } else {
                carry = 0;
            }
            sum_tail->next = new ListNode(node_sum);
            sum_tail = sum_tail->next;
            l1 = l1->next;  
        }
        while(l2){
            node_sum = l2->val + carry;
            if(node_sum >= 10){
                carry = 1;
                node_sum -=10;
            } else {
                carry = 0;
            }
            sum_tail->next = new ListNode(node_sum);
            sum_tail = sum_tail->next;
            l2 = l2->next;  
        }
    if (carry){
        sum_tail->next = new ListNode(carry);
    }
    return sum_head->next;
    }
};
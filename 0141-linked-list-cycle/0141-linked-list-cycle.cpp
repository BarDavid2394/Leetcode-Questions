/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 //pointers approach
// class Solution {
// public:
//     bool hasCycle(ListNode *head) {
//       ListNode *slow = head;
//       ListNode *fast = head; 
//       while (fast && slow && fast->next){
//           slow = slow->next;
//           fast = fast->next->next;
//           if(fast == slow){
//               return true;
//           }
//       }
//       return false;
//     }
// };
//hastable

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL)
            return false;
        unordered_map<ListNode*, int> map;
        while(head != NULL){
            if(map.count(head)>0)
                return true;
            else{
                map[head] = 1;
                head = head->next;
            }
        
        }
        return false;
    }
};
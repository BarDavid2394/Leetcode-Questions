class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
     for(int i=0;i<nums.size();i++){
         for(int j=1;j<nums.size();j++){
             if(nums[i]+nums[j] == target && i != j){
                 return {i,j};
             }
         }
     }  
     return {}; 
    }
};      

//two while loops on the vector elements. when target is met, pushing the 2 indexes/
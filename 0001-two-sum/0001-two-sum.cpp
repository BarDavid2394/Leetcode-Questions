class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
     vector<int> Sum;
     for(int i=0;i<nums.size();i++){
         for(int j=1;j<nums.size();j++){
             if(nums[i]+nums[j] == target && i != j){
                 Sum.push_back(i);
                 Sum.push_back(j);
                 return Sum;
             }
         }
     }  
     return Sum; 
    }
};      

//two while loops on the vector elements. when target is met, pushing the 2 indexes/
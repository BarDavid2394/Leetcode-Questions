class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
      int i= n-1;
      int j = m-1;
      int real_size1 =(m+n)-1;
      while(i>=0 && j>=0){
          if(nums1[j] > nums2[i]){
              nums1[real_size1] = nums1[j];
              j--;
              real_size1--;
          }
            else{
              nums1[real_size1] = nums2[i];
              i--;
              real_size1--;
          }
      }
    while(j>=0){
        nums1[real_size1] = nums1[j];
        real_size1--;
        j--;
    } 
    while(i>=0){
        nums1[real_size1] = nums2[i];
        real_size1--;
        i--;
    }   
    }
};
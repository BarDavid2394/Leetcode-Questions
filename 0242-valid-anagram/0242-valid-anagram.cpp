class Solution {
public:
    bool isAnagram(string s, string t) {
        int hist_s[123] = {0};
        int hist_t[123] = {0};
        for(int i = 0;i<s.length();i++){
            hist_s[s[i]]++;
        }
        for(int j = 0;j<t.length();j++){
            hist_t[t[j]]++;
        }
        for(int k=0;k<123;k++){
            if(hist_t[k] != hist_s[k]){
                return false;
            }
        }
        return true;
    }
};

//naive solution - histogram for each string, o(1) space, then adding each letter via ascii value to the arraym, then comparing each cell. o(max{s.length,t.length})

//condition for different len.
//hashtable 
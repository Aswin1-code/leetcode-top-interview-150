class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int c=0,maj=0;
        for(int i:nums){
            if(c==0){ maj=i; }
            if(maj==i){
                c+=1;
            }
            else{
                c-=1;
            }
        }
    return maj;
    }
};
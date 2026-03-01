class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minP=INT_MAX;
        int maxP=0;
        for(int i=0;i<prices.size();i++){
            if(prices[i]<minP){
                minP=prices[i];
            }
            else{
                int prft=prices[i]-minP;
                if(prft>maxP){
                    maxP=prft;
                }
            }
        }
        return maxP;
    }
};
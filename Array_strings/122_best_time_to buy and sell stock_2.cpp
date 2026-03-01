class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minP=INT_MAX;
        int prft=0;
        for(int i=0;i<prices.size();i++){
            if(prices[i]<minP){
                minP=prices[i];
            }
            else{
                prft=prft+prices[i]-minP;
                minP=prices[i];
            }
        }
            return prft;
    }

};
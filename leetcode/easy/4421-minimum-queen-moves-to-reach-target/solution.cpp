
class Solution {
public:
    int minQueenMoves(vector<int>& source, vector<int>& target) {
        int sr =source[0];
        int sc =source[1];
        int tr =target[0];
        int  tc=target[1];
        if(sr==tr && sc==tc){
            return 0;
            
        }
        if(sr==tr||sc==tc){
            return 1;
        }
        int dr=sr-tr;
        int dc=sc-tc;
        if(dr==dc||dr==-dc){
            return 1;
        }
        return 2;
    }
};
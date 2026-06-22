class Solution {
    public boolean isPalindrome(int x) {
        int temp=x, rev=0;
        while(temp>0){
            int r= temp%10;
            rev=rev*10+r;
            temp/=10;
        }
        if(rev==x)
            return true;
        else
            return false;
    }
}
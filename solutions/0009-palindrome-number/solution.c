bool isPalindrome(int x) {
    long int r,s=0,p;
    p=x;
    while (x>0)
    {
        r = x%10;
        s = s*10 + r;
        x = x/10;
    }
    if (s == p)
    {
        return true;
    }
    else
    {
        return false;
    }
}

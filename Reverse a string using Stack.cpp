// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
void reverse(char *str, int len);
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        char str[10000];
        cin>>str;
        long long int len=strlen(str);
        reverse(str,len);
        cout<<str;
        cout<<endl;
    }
        return 0;
}
// } Driver Code Ends
void reverse(char *str, int len)
{

stack<char> s;
// int l=sizeof(str);
for(int i=0;i<len;i++)
{
    s.push(str[i]);
}
// char *new_str='';
for(int i=0;i<len&&!s.empty();i++)
{
    str[i]=s.top();
    s.pop();
}

}

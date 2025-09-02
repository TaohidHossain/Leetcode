#include<bits/stdc++.h>
using namespace std;

#define ll long long

int firstUniqChar(string s) {
    unordered_map<char, int> mp;
    for(char c: s){
        mp[c]++;
    }
    for(int i=0; i<s.size(); i++){
        if(mp[s[i]] == 1 ) return i;
    }
    return -1;
}

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    cin >> t;
    while(t--){
            string s;
            cin >> s;
            cout << firstUniqChar(s) << "\n";
    }
    return 0;
}

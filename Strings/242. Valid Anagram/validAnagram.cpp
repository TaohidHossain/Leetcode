#include<bits/stdc++.h>
using namespace std;

#define ll long long

void valid_anagram(string s, string t){
    if(s.length() != t.length()){
        cout << "NO\n";
        return;
    }

    vector<int> count(26, 0);
    for(int i = 0; i < s.length(); i++){
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }
    for(int i = 0; i < 26; i++){
        if(count[i] != 0){
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
}


int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    cin >> t;
    while(t--){
            string s, t;
            cin >> s >> t;
            valid_anagram(s, t);
    }
    return 0;
}

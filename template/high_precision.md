# 高精度模板

## 加
```c++
// from acwing C = A + B, A >= 0, B >= 0 
vector<int> add(vector<int> &A, vector<int> &B)  
{
    if (A.size() < B.size()) return add(B, A);

    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i ++ )
    {
        t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }

    if (t) C.push_back(t);
    return C;
}

for(int i=a.size()-1;i>=0;i--)A.push_back(a[i]-'0');
for(int i=b.size()-1;i>=0;i--)B.push_back(b[i]-'0');
auto C=add(A,B);
for(int i=C.size()-1;i>=0;i--)cout<<C[i];
```

## 减

```c++
bool cmp(vector<int> &A,vector<int> &B)
{
    if(A.size()!=B.size())return A.size()>B.size();
    else{ for(int i=A.size()-1;i>=0;i--)
            if(A[i]!=B[i])return A[i]>B[i];
          return 1;}
}

// from acwing C = A - B, 满足A >= B, A >= 0, B >= 0
vector<int> sub(vector<int> &A, vector<int> &B)  
{
    vector<int> C;
    for (int i = 0, t = 0; i < A.size(); i ++ )
    {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        if (t < 0) t = 1; else t = 0;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

if(cmp(A,B)){
    auto C=subtraction(A,B);
    for(int i=C.size()-1;i>=0;i--)cout<<C[i];
} else {
    auto C=subtraction(B,A); cout<<"-";
    for(int i=C.size()-1;i>=0;i--)cout<<C[i];
}

```

## 乘

```c++
// 高精度乘低精度 from acwing 
// C = A * b, A >= 0, b >= 0
vector<int> mul(vector<int> &A, int b)
{
    vector<int> C;

    int t = 0;
    for (int i = 0; i < A.size() || t; i ++ )
    {
        if (i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

for(int i=a.size()-1;i>=0;i--)A.push_back(a[i]-'0');
auto C=multiplication(A,b);
for(int i=C.size()-1;i>=0;i--)cout<<C[i];
```

## 除

```c++
// 高精度除以低精度 from acwing 
// A / b = C ... r, A >= 0, b > 0
vector<int> div(vector<int> &A, int b, int &r)
{
    vector<int> C;
    r = 0;
    for (int i = A.size() - 1; i >= 0; i -- )
    {
        r = r * 10 + A[i];
        C.push_back(r / b);
        r %= b;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

for(int i=a.size()-1;i>=0;i--)A.push_back(a[i]-'0');
int r=0; auto C=division(A,b,r);
for(int i=C.size()-1;i>=0;i--)cout<<C[i];

```
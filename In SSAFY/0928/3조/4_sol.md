## 2 번

- `T(0) = 1`로 설정하고 진행

T(n) = T(n - 1) + n

= T(n-2) + n +n -1

=T(1) + n + n-1 + n-2 + ... + 1

n이 n개 있으므로 O(n^2)



## 4번

- `T(1) = 1`로 설정하고 진행





T(n) = T(n/2^k) + k

n/2^k = 1이 되게 하는 값 k = logn

T(n) = T(1) + logn

O(log(n))




## 6번

![Image](https://media.discordapp.net/attachments/892228429292904531/892276813420703794/unknown.png?width=330&height=300)

O(nlog(n))






## 8번

T(1) = T(0) + 1

T(2) = T(1) + 1/2

T(3) = T(2) + 1/3
$$
T(n) = T(0) + \sum_{k=1}^n {1 \over k}
$$
∑ k=1 부터 n까지 1/n 

= 1+∫1부터 k까지 1/k dk

= 1 + log(n) - log1

= 1 + log(n)

O(log(n))


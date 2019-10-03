作者：争渡
链接：https: // www.nowcoder.com / discuss / 253361?type = post & order = create & pos = & page = 1
来源：牛客网

import java.util. *;

public


class Main{
public static void main(String[] args)throws Exception{
Scanner sc=new Scanner(System.in );
String[] s=sc.nextLine().split(":");
char[] a=s[0].toCharArray();
char[] b=s[1].toCharArray();
int l=a.length;
int r=b.length;
int[] z=new int[l];
int[] x=new int[r];
for (int i=0;i < l;i++){
if (a[i] <= '9'){
z[i]=(int)a[i];
} else {
z[i]=(int)(a[i]-'A')+10;
}
}
for (int i=0;i < r;i++){
if (b[i] <= '9'){
x[i]=(int)b[i];
} else {
x[i]=(int)(b[i]-'A')+10;
}
}
int m=0;
int[] a1=z;
Arrays.sort(a1);

int c=a1[l-1]+1;

int n=0;
int[] b1=x;
Arrays.sort(b1);
int d=b1[r-1]+1;
int q=Math.max(c, d);
if ((z[l-1] < 24 & & pas(z)) & & (pas(x))){
System.out.print(0);
}


while (m < 24){
m=0;
int j=0;
for (int i=l-1;i >= 0;i--){
m += z[i] * Math.pow(c, j);
j++;
}
c++;
}

while (n < 60){
n=0;
int p=0;
for (int i=r-1;i >= 0;i--){
n += x[i] * Math.pow(d, p);
p++;
}
d++;
}
int
sum = Math.min(c - 2, d - 2);

for (int i=q;i < sum;i++){
    System.out.print(i + " ");
}
System.out.print(sum);
}
public
static
boolean
pas(int[]
a){
int
m = a.length;
for (int i=0;i < m-1;i++){
if (a[i] != 0){
return false;
}
}
return true;
}
}

import java.util.Set;
import java.util.HashSet;
import java.util.Scanner;



public class Main {

    public static Set<Integer> s = new HashSet<>();
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt(), m = in.nextInt();
        int[] d = new int[m];
        for (int i = 0; i < m; i++) {
            d[i] = in.nextInt();
        }

        for (int i = 0; i < n; i++) {
            helper(d, 0, i, n, i);
        }
        System.out.println(s.size());
    }

    private static void helper(int[] d, int idx, int p, int n, int f) {
        if (idx >= d.length && p >= 0 && p <= n) {
            s.add(pos);
            return;
        }
        if (d[idx] <= p) {
            helper(d, idx + 1, p - d[idx], n, f);
        }

        if (d[idx] <= n - p - 1) {
            helper(d, idx + 1, p + d[idx], n, f);
        }
    }
}

s = set()
for i in range(n)
    dfs(kkk, 0, i, n, i);
}
def helper(d,index,pos,n,flag):
    if index>=len(d) and pos>=0 and pos<=n:
        s.add(pos)
        return
    if d[index]<=pos:
        helper(d, index + 1, pos - d[index], n, flag)

    if (d[index] <= n - pos - 1):
        helper(d, index + 1, pos + d[index], n, flag)

    private static void helper(int[] d, int index, int pos, int n, int flag) {
        if (index >= d.length && pos >= 0 && pos <= n) {
            s.add(pos);
            return;
        }
        if (d[index] <= pos) {
            helper(d, index + 1, pos - d[index], n, flag);
        }

        if (d[index] <= n - pos - 1) {
            helper(d, index + 1, pos + d[index], n, flag);
        }
    }
}
import java.util.Set;
import java.util.HashSet;
import java.util.Scanner;



public class Main {

    public static Set<Integer> set = new HashSet<>();
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt(), m = in.nextInt();
        int[] d = new int[m];
        for (int i = 0; i < m; i++) {
            d[i] = in.nextInt();
        }

        for (int i = 0; i < n; i++) {
            dfs(d, 0, i, n, i);
        }
        System.out.println(set.size());
    }

    private static void dfs(int[] d, int idx, int pos, int n, int fa) {
        if (idx >= d.length && pos >= 0 && pos <= n) {
            set.add(pos);
            return;
        }
        if (d[idx] <= pos) {
            dfs(d, idx + 1, pos - d[idx], n, fa);
        }

        if (d[idx] <= n - pos - 1) {
            dfs(d, idx + 1, pos + d[idx], n, fa);
        }
    }
}
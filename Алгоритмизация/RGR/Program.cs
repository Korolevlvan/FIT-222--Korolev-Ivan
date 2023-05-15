Boolean P(int a)
{
    if(a>2)
    {
        if(a%2==0)return P(a/2);
        else return false;
    }
    else if(a == 2)return true;
    else return false;
}
Boolean chech(int a, int b)
{
    string g = Convert.ToString(a, 2);
    if(g.Length < b)return false;
    //if(b==3){Console.Write(g[g.Length-b]);Console.Write("  ");Console.WriteLine(g);}
    if(g[g.Length-b] == '1'){return true;}
    return false;
}
Boolean flag = true;
int n;
while(flag)
{
    Console.WriteLine("1 - Зашифровать");
    Console.WriteLine("2 - Дешифровать");
    int k = Convert.ToInt16(Console.ReadLine());

    if(k==1)
    {
        Console.Clear();
        Console.WriteLine("Введите длинну кода");
        n = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Вводите построчно двухзначные числа формата XY(X - часть двоичного кода, Y - часть ключа, ключ тоже в виде двоичного кода)");
        int r = 0;
        for(int i = 1; i <= n;i++ )if((Math.Pow(2, i) >= (n + i + 1)) && (r == 0))r = i;
        int[] enc = new int[n+r+1];
        for(int i = 1; i <= (n+r); i++)
        {
            if((P(i) != true) && (i!=1))
            {
                int a = Convert.ToInt32(Console.ReadLine());
                if(a%10 == 1)enc[i] = Math.Abs((a/10)-1);
                else enc[i] = a/10;
            }
        }
        int h = 1;
        for(int i = 1; i <= (n+r); i = i*2)
        {
            int ri = 0;
            for(int j = 1; j <= (n+r);j++)
            {
                //if(chech(j, h))Console.Write("AAA ");
                if((j!=i) && (chech(j, h))){ri = ri + enc[j];}
            }
            ri = ri % 2;
            enc[i] = ri;
            h++;
        }
        Console.WriteLine("Зашифрованные Данные:");
        for(int i = 1; i <=(n+r); i++)
        {
            Console.WriteLine(enc[i]);
        }
        Console.WriteLine("Введите любое число для продолжения");
        string cash = Convert.ToString(Console.ReadLine());
        Console.Clear();
    }
    if(k==2)
    {
        Console.Clear();
        Console.WriteLine("Введите длинну кода");
        int n1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Вводите построчно двухзначные числа формата XY(X - часть двоичного кода, Y - часть ключа)");
        Console.WriteLine("Ключ для дишефровки является ключом шифровки изменненый следующим образом:");
        Console.WriteLine("перед каждым 2^n(n = 0, 1, 2 , ...) поставить ноль");
        int[] enc1 = new int[n1+1];
        int[] key = new int[n1+1];
        int r = 0;
        for(int i = 1; i <= n1;i++ )if((Math.Pow(2, i) >= (n1 + 1)) && (r == 0))r = i;
        int h1 = 1;
        int c = 0;
        int[] ci = new int[r+1];
        for(int i = 1; i <= (n1); i++)
        {
                int a = Convert.ToInt32(Console.ReadLine());
                if(a%10 == 1)enc1[i] = Math.Abs((a/10)-1);
                else enc1[i] = a/10;
                key[i] = a%10;
        }
        for(int i = 1; i <= (n1); i = i*2)
        {
            int ri1 = 0;
            int rik = 0;
            for(int j = 1; j <= (n1);j++)
            {
                //if(chech(j, h))Console.Write("AAA ");
                if((chech(j, h1))){ri1 = ri1 + enc1[j];}
                if((chech(j, h1)) && (j != i)){rik = rik + key[j];}
            }
            ci[h1] = (ri1 + rik) % 2;
            h1++;
        }
        for(int i = r;i >= 1; i--)
        {
            c = (c*2) + ci[i];
        }
        if(c != 0)enc1[c] = Math.Abs(enc1[c]-1);
        Console.WriteLine("Данные:");
        for(int i = 1; i<=(n1);i++)
        {
           if((P(i) != true) && (i!=1))Console.WriteLine(enc1[i]);
        }
        Console.WriteLine("Введите любое число для продолжения");
        string cash = Convert.ToString(Console.ReadLine());
        Console.Clear();
    }
}
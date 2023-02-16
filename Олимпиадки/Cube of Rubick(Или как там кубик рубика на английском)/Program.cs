
void pov(ref int x, ref int y, int d, int n)
{
    x = x - 1;
    y = y - 1;
    d= d - 1;
    int t = 0;
    int n2 = d/2;
    if(n == -1)
    {
        t = x; x = d-y; y = t;
    } else
    {
        t = y; y = d - x; x = t;
    }
    x = x + 1;
    y = y + 1;
}

StreamReader sr = new StreamReader("input_s1_20.txt");
int n, m;
string st1= Convert.ToString(sr.ReadLine());
string[] sst1 = st1.Split();
n = int.Parse(sst1[0]);
m = int.Parse(sst1[1]);
int x, y, z;
st1= Convert.ToString(sr.ReadLine());
sst1 = st1.Split();
x = int.Parse(sst1[0]);
y = int.Parse(sst1[1]);
z = int.Parse(sst1[2]);
char a;
int k, s;
for(int i = 0; i<m; i++)
{
   // Console.WriteLine($"{x} {y} {z}");
    st1= Convert.ToString(sr.ReadLine());
    sst1 = st1.Split();
    a = char.Parse(sst1[0]);
    k = int.Parse(sst1[1]);
    s = int.Parse(sst1[2]);
    if((a == 'X') && (x == k)){pov(ref y, ref z, n, s);}
    if((a == 'Y') && (y == k)){pov(ref x, ref z, n, s);}
    if((a == 'Z') && (z == k)){pov(ref x, ref y, n, s);}
}
Console.WriteLine($"{x} {y} {z}");

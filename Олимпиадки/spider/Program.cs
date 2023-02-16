
float x, y, z, sx, sy, sz, fx, fy, fz;
StreamReader sr = new StreamReader("input_s1_01.txt");
//ввод
if(true)
{
string st1= Convert.ToString(sr.ReadLine());
string[] sst1 = st1.Split();
x = float.Parse(sst1[0]);
y = float.Parse(sst1[1]);
z = float.Parse(sst1[2]);
st1= Convert.ToString(sr.ReadLine());
sst1 = st1.Split();
sx = float.Parse(sst1[0]);
sy = float.Parse(sst1[1]);
sz = float.Parse(sst1[2]);
st1= Convert.ToString(sr.ReadLine());
sst1 = st1.Split();
fx = float.Parse(sst1[0]);
fy = float.Parse(sst1[1]);
fz = float.Parse(sst1[2]);
}

static float put(float x,float y,float z,float sx,float sy,float sz,float fx,float fy,float fz)
{
    float a, b, c;
    a = 0;
    b = 0;
    c = 0;
    if(fx == x)a = x - sx;
    if(fy == y)a = y - sy;
    if(fz == z)a = z - sz;
    if(fx == (float)0)a = sx;
    if(fy == (float)0)a = sy;
    if(fz == (float)0)a = sz;
    if(sx == x)b = x - fx;
    if(sy == y)b = y - fy;
    if(sz == z)b = z - fz;
    if(sx == (float)0)b = fx;
    if(sy == (float)0)b = fy;
    if(sz == (float)0)b = fz;
    if(((fx != x) || (fx != (float)0)) && ((sx != x) || (sx != (float)0)))c = Math.Abs(fx - sx)/2;
    if(((fy != y) || (fy != (float)0)) && ((sy != y) || (sy != (float)0)))c = Math.Abs(fy - sy)/2;
    if(((fz != z) || (fz != (float)0)) && ((sz != z) || (sz != (float)0)))c = Math.Abs(fz - sz)/2;
    return (float)(Math.Sqrt((a*a) + (c*c)) + Math.Sqrt((b*b) + (c*c)));
}
float a = put(x, y, z, sx, sy, sz, fx, fy, fz);
Console.WriteLine(a);
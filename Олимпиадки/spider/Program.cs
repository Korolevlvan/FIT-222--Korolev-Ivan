
float x, y, z, sx, sy, sz, fx, fy, fz;
StreamReader sr = new StreamReader("input_s1_19.txt");
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
float a;
static float put1(float n,float x,float y,float sx,float sy,float fx,float fy)
{
    float a, b, a1, b1;
    if((sx + fx)>=((2*x)-sx-fx)){a = sx; b = fx;}
    else{a = x - sx; b = x - fx;}
    if((sy + fy)>=((2*y)-sy-fy)){a1 = sy; b1 = fy;}
    else{a1 = y -sy; b1 = y - fy;} 
    if((a1 + b1)>=(a + b)){x = Math.Abs(fx-sx)/2; a= (float)(Math.Sqrt((a1*a1) + (x*x)) + Math.Sqrt((b1*b1) + (x*x))) + n;}
    else {y = Math.Abs(fy-sy)/2; a= (float)(Math.Sqrt((a*a) + (y*y)) + Math.Sqrt((b*b) + (y*y))) + n;}
    return a;
}
static float put2(float x,float y,float z,float sx,float sy,float sz,float fx,float fy,float fz)
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
//на одной стороне
if(((sx == x) && (fx == x)) || ((sy == y) && (fy == y)) || ((sz == z) && (fz == z))||
((sx == 0) && (fx == 0)) || ((sy == 0) && (fy == 0))|| ((sz == 0) && (fz == 0)))
{sx = Math.Abs(sx - fx); sy = Math.Abs(sy - fy); sz = Math.Abs(sz - fz);
 a = (float)(Math.Sqrt((sx * sx) + (sy * sy)+(sz*sz)));}
//на противоположных сторонах
else if(((sx == x)&&(fx == 0)) || ((sx == 0)&&(fx == x)))a = put1(x,y,z,sy,sz,fy,fz);
else if(((sy == y)&&(fy == 0)) || ((sy == 0)&&(fy == y)))a = put1(y,x,z,sx,sz,fx,fz);
else if(((sz == z)&&(fz == 0)) || ((sz == 0)&&(fz == z)))a = put1(z,y,x,sy,sx,fy,fx);
else a = put2(x, y, z, sx, sy, sz, fx, fy, fz);
Console.WriteLine((float)a);
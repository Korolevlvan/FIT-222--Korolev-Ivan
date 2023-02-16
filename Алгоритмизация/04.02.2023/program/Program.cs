bool marker = true; 
int numCar = 0;
car[] m = new car[0];
while(marker)
{
Console.Clear();
Console.WriteLine("1 - ввод");
Console.WriteLine("2 - выборка машин с единственным владельцем");
Console.WriteLine("3 - выборка машин моложе X года");
Console.WriteLine("4 - Выборка машин заданной марки");
Console.WriteLine("5 - Выход");
int way = Convert.ToInt32(Console.ReadLine());
Console.Clear();
string kast;
if(way == 1)//ввод
{
    Console.WriteLine("Введите количество машин");
    int n = Convert.ToInt32(Console.ReadLine());
    numCar = n;
    string mar, col;
    int age, man;
    m = new car[n];
    for(int i = 0; i<n;i++)
    {
    Console.WriteLine($"марка машины №{i+1}");
    mar = Convert.ToString(Console.ReadLine());
    Console.WriteLine($"цвет машины №{i+1}");
    col = Convert.ToString(Console.ReadLine());
    Console.WriteLine($"Год выпуска машины №{i+1}");
    age = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine($"Количество владельцев №{i+1}");
    man = Convert.ToInt32(Console.ReadLine());
    Console.Clear();
    m[i] = new car(mar, col, age, man);
    }

}
if(way == 2)if(numCar == 0){Console.WriteLine("Введите тачки"); kast = Convert.ToString(Console.ReadLine());} else
{
    bool flag = false;
    for(int i = 0; i<numCar; i++)
    {
        if(m[i].num == 1){Console.WriteLine($"Марка{m[i].mar} Год{m[i].age}"); flag = true;}
    }
    if(flag == false)Console.WriteLine("Нету таких");
    kast = Convert.ToString(Console.ReadLine());
    Console.Clear();
}
if(way == 3)if(numCar == 0){Console.WriteLine("Введите тачки"); kast = Convert.ToString(Console.ReadLine());} else
{
    bool falg = false;
    Console.WriteLine("ВВедите год");
    int agev = 0;
    agev = Convert.ToInt32(Console.ReadLine());
    Console.Clear();
    for(int i = 0; i<numCar; i++)
    {
        if(m[i].age < agev){Console.WriteLine($"Марка{m[i].mar} Год{m[i].age}"); falg = true;}
        if(falg == false)Console.WriteLine("Нету таких");
    }
    kast = Convert.ToString(Console.ReadLine());
    Console.Clear();
}
if(way == 4)if(numCar == 0){Console.WriteLine("Введите тачки"); kast = Convert.ToString(Console.ReadLine());} else
{
    bool falg = false;
    Console.WriteLine("ВВедите марку");
    string agev;
    agev = Convert.ToString(Console.ReadLine());
    Console.Clear();
    for(int i = 0; i<numCar; i++)
    {
        if(m[i].mar == agev){Console.WriteLine($"Марка{m[i].mar} Год{m[i].age}"); falg = true;}
        if(falg == false)Console.WriteLine("Нету таких");
    }
    kast = Convert.ToString(Console.ReadLine());
    Console.Clear();
}
if(way == 5){Console.Clear(); marker = false;}
Console.Clear();
}

//класс описывает машину(марка, цвет, год выпуска, владелец(фио, год покупки, ког продажи))
//1 ввод
// выборка машин с одним владельцем
//3 выборка машин моложе x года
//4 выборка машин заданной марки
//5 выход
public class Master
{
    public string FIO;
    public int ageb;
    public int ages;
    
    public Master(string a, int aa, int aaa)
    {
        FIO = a;
        ageb = aa;
        ages = aaa;
    }
    public Master()
    {
    }
}

public class car
{
    public string mar;
    public string col;
    public int age;
    public int num;
    Master[] m;
    public car( string mmar, string ccol, int aage,int n)
    {
        mar = mmar;
        col = ccol;
        age = aage;
        num = n;
        string FIO;
        int gb, gs;
        m = new Master[n];
        for(int i = 0; i<n;i++)
        {
        Console.WriteLine($"ФИО владельца №{i+1}");
        FIO = Convert.ToString(Console.ReadLine());
        Console.WriteLine($"ГОД покупки владельцем №{i+1}");
        gb = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine($"ГОД продажи владельцем №{i+1}");
        gs = Convert.ToInt32(Console.ReadLine());
        Console.Clear();
        m[i] = new Master(FIO, gb, gs);
        }
    }
}

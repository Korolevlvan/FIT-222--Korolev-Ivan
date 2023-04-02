/*Институт, класс управляющий(приказы, с префексами о том, для кого приказ. ФИО , др, должность), п
преподаватели(дисциплины,ФИО,кафедра )
\ студенты(оценки по предметам и предподователи, ФИО)
 вспомогательный, 
 класс стстав(фио, др).
1 выборка по приказам.
2 выборка по фио определить должников.
3 долги студента*/
bool flag = true;
while(flag)
{
    Console.WriteLine("1 ввод данных");
    Console.WriteLine("2 Выборка по приказам");
    Console.WriteLine("3 Выборка должников по фио");
    Console.WriteLine("4 Долги студента");
    int j = Convert.ToInt32(Console.ReadLine());
}



public class student
{   
    public string fio = " ";
    public string[] algebra = new string[2];
    public string[] biology = new string[2];
    public string[] drawing = new string[2];
    public string[] chemistry = new string[2];
    public string[] geography = new string[2];
    public string[] geometry = new string[2];
    public string[] history = new string[2];
    public string[] literature = new string[2];
    public student(){}
    public student(string fi, string[] alg, string[] bio, string[] draw, string[] che,
    string[] geog, string[] geom, string[] his, string[] lit)
    {
        fio = fi;
        algebra = alg;
        biology = bio;
        drawing = draw;
        chemistry = che;
        geography = geog;
        geometry = geom;
        history = his;
        literature = lit;
    }

}
public class teacher
{
    public string fio;
    List<student> students = new List<student>();
    public teacher()
    {
        
    }
    public student find_a_kid(string f)
    {
        foreach(var j in students)
        {
            if(j.fio == f) return j;
        }
        return null;
    }
    public teacher(string fioo, List<teacher> teachers)
    {
        fio = fioo;
        Console.WriteLine("Напишите количество учеников");
        int n = Convert.ToInt32(Console.ReadLine());
        for(int i = 1; i<=n;i++)
        {
            string sfio = Convert.ToString(Console.ReadLine());
            foreach(var j in teachers)
            {

            }
        }
    }
}
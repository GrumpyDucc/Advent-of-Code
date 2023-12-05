namespace Day1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int endValue = 0;
            string[] Values = File.ReadAllLines("\\\\SYNOLOGY-NAS\\Jan\\Code\\AOC\\2023\\Day 1\\input.txt");
            for (int i = 0; i < Values.Length; i++)
            {
                string line = Values[i].Replace("oneight", "18").Replace("twone", "21").Replace("threeight", "38").Replace("fiveight", "58").Replace("sevenine", "79").Replace("eighthree", "83").Replace("eightwo", "82").Replace("nineight", "98").Replace("one", "1").Replace("two", "2").Replace("three", "3").Replace("four", "4").Replace("five", "5").Replace("six", "6").Replace("seven", "7").Replace("eight", "8").Replace("nine", "9");
                char firstNum = '-';
                char lastNum = '-';
                for (int j = 0; j < line.Length; j++)
                {
                    if (char.IsNumber(line[j]))
                    {
                        firstNum = line[j];
                        break;
                    }
                }
                for (int j = line.Length-1; j >= 0; j--)
                {
                    if (char.IsNumber(line[j]))
                    {
                        lastNum = line[j];
                        break;
                    }
                }
                endValue += Convert.ToInt32($"{firstNum}{lastNum}");                
            }
            Console.WriteLine(endValue);
        }
    }
}
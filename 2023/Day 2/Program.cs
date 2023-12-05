using System.Numerics;

string[] games = File.ReadAllLines("\\\\SYNOLOGY-NAS\\Jan\\Code\\AOC\\2023\\Day 2\\input.txt");
int endValue = 0;

for (int i = 0; i < games.Length; i++)
{
    string[] game = games[i].Split(':');
    int index = Convert.ToInt32(game[0].Split(' ')[1]);
    string[] draws = game.Skip(1).ToArray()[0].Split(';');
    int red = 0, green = 0, blue = 0;
    for (int j = 0; j < draws.Length; j++)
    {
        string[] draw = draws[j].Split(',');
        for (int k = 0; k < draw.Length; k++)
        {
            string[] cubes = draw[k].Split(" ").Skip(1).ToArray();
            int cubeCount = Convert.ToInt32(cubes[0]);
            if (cubes[1] == "red" && cubeCount > red){
                red = cubeCount;
            }
            else if (cubes[1] == "green" && cubeCount > green){
                green = cubeCount;
            }
            else if (cubes[1] == "blue" && cubeCount > blue){
                blue = cubeCount;
            }
        }
    }
    endValue += red * blue * green;
}

Console.WriteLine(endValue);
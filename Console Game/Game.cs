using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string key, out int xChange, out int yChange) {
      xChange = 0;
      yChange = 0;
      switch(key) {
        case "LeftArrow":
        xChange -= 1;
        break;
        case "RightArrow":
        xChange += 1;
        break;
        case "UpArrow":
        yChange -= 1;
        break;
        case "DownArrow":
        yChange += 1;
        break;
      }
    }
    
    public new static char UpdateCursor(string key) {
      if (key == "LeftArrow") {
        return '<';
      } else if (key == "RightArrow") {
        return '>';
      } else if (key == "UpArrow") {
        return '^';
      } else {
        return 'v';
      }
    }
    
    public new static int KeepInBounds(int coor, int max) {
      int maxRange = max - 1;
      if (coor < 0) {
      coor = 0;
      } else if (coor >= max) {
        coor = maxRange;
      }
      
      return coor;
    }
    
    public new static bool DidScore(int charX, int charY, int fruitX, int fruitY) {
      if (charX == fruitX && charY == fruitY) {
      return true;
      } else {
      return false;
      }
    }
  }
}

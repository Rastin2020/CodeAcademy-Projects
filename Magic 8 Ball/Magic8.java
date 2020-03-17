class Magic8 {
  public static void main(String[] args) {
  int randomNum = (int)Math.round(Math.random()*12);
  
  switch(randomNum) {
    case 0:
      System.out.println("Doubt it.");
      break;
    case 1:
      System.out.println("It looks doubtful...");
      break;
    case 2:
      System.out.println("There might be hope yet.");
      break;
    case 3:
      System.out.println("It think so!");
      break;
    case 4:
      System.out.println("I don't think so...");
      break;
    case 5:
      System.out.println("The stars say yes!");
      break;
    case 6:
      System.out.println("The stars say no...");
      break;
    case 7:
      System.out.println("I'd rather not answer...");
      break;
    case 8:
      System.out.println("Most certainly!");
      break;
    case 9:
      System.out.println("Hell naw!");
      break;
    case 10:
      System.out.println("In all honesty, yes.");
      break;
    case 11:
      System.out.println("Can't predict now, my head hurts...");
      break;
    case 12:
      System.out.println("I don't have an answer for this one.");
      break;
  }
  }
}

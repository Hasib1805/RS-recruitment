int channels[8];

void readChannel(){
  static bool readingStat = false;
  static int channelIndex = 0;
  static int currentValue = 0;

  while (Serial1.available() > 0){
    char ch = Serial1.read(); 

    if (ch == '<'){
      readingStat = true;
      channelIndex = 0;
      currentValue = 0;
    }
    else if (ch == '>'){
      if (channelIndex < 8){
        channels[channelIndex] = currentValue;
      }

      readingStat = false;
    }
    else if (readingStat) {
      if (ch >= '0' && ch <= '9'){
        currentValue = currentValue * 10 + (ch - '0');
      }
      else if (ch == ' '){
        if (channelIndex < 8){
          channels[channelIndex++] = currentValue;
          currentValue = 0;
        }
      }
    }
  }
}
#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

SoftwareSerial mp3Serial(10, 11);
DFRobotDFPlayerMini mp3;

void setup() {
  mp3Serial.begin(9600);
  Serial.begin(9600);

  if (!mp3.begin(mp3Serial)) {
    Serial.println("MP3 모듈 연결 실패");
    while (true);
  }

  mp3.volume(25);
  Serial.println("MP3 모듈 연결 성공");
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\\n');
    cmd.trim();

    if (cmd == "RED") {
      mp3.play(1);  // 0001.mp3
    } else if (cmd == "GREEN") {
      mp3.play(2);  // 0002.mp3
    }
  }
}

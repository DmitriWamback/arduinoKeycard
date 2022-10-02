#include <MFRC522.h>
#include <SPI.h>

MFRC522 rfid(10, 9);
String current;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    Serial.println("Here");
    SPI.begin();
    rfid.PCD_Init();
}

void loop() {
  // put your main code here, to run repeatedly:

    if (!rfid.PICC_IsNewCardPresent()) { Serial.println("no card"); return; }
    if (!rfid.PICC_ReadCardSerial()) return;

    String content;
    byte letter;

    for (byte i = 0; i < rfid.uid.size; i++) {
        content.concat(String(rfid.uid.uidByte[i], HEX));
    }

    content.toUpperCase();
    Serial.println(content);
}

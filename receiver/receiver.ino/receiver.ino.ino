#include <WiFi.h>

const char* ssid = "Device-Northwestern";
const char* password = "";
const int serverPort = 8888;

WiFiServer server(serverPort);
WiFiClient client;

void setup() {
    Serial.begin(115200);
    delay(10);
    pinMode(18, OUTPUT);  // Set the pin as an output

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
    }
    Serial.println("Connected to WiFi");

    server.begin();
    Serial.println("Server started: ");
    Serial.println(WiFi.localIP());
}

void loop() {
    client = server.available();
    if (client) {
        Serial.println("Client connected");

        while (client.connected()) {
            if (client.available() > 0) {
                byte byte_received = client.read();
                Serial.println("Received byte: " + String(byte_received));
                digitalWrite(18, HIGH);  // Set the pin high (3.3V or logic level HIGH)
                delay(1000);  // Wait for 1 second
                digitalWrite(18, LOW);
            }
        }
    }
}

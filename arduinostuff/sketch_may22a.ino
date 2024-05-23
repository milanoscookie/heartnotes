// // Define the GPIO pin for PWM output
// const int pwmPin = 18;

// #include <WiFi.h>


// // Define PWM properties
// const int pwmFreq = 5000;
// const int pwmChannel = 0;
// const int pwmResolution = 8; // 8-bit resolution, values from 0 to 255

// void setup() {
//   // Set up the PWM functionality
//   ledcSetup(pwmChannel, pwmFreq, pwmResolution);

//   // Attach the PWM channel to the GPIO pin
//   ledcAttachPin(pwmPin, pwmChannel);

//   // Initialize serial communication for debugging
//   Serial.begin(115200);
//   WiFi.begin("Device-Northwestern");

//   while ( WiFi.status() != WL_CONNECTED) { 
//     Serial.print(".");
//     delay(500);
//   }

//   Serial.println("Connected to Wifi");
// }

// void loop() {
//   // Define the PWM duty cycle (0-255)
//   int dutyCycle = 128; // 50% duty cycle

//   // Write the PWM signal to the motor
//   ledcWrite(pwmChannel, dutyCycle);

//   Serial.println(WiFi.localIP());
// }
#include <WiFi.h>
#include <ESPAsyncWebServer.h>

const char* ssid = "Device-Northwestern";
const char* password = "";
AsyncWebServer server(80);

void setup() {
  Serial.begin(115200);
 
  // Connect to Wi-Fi
  WiFi.begin(ssid);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");

  // Define the /data endpoint
  server.on("/data", HTTP_POST, [](AsyncWebServerRequest *request){
    int params = request->params();
    for(int i=0;i<params;i++){
      AsyncWebParameter* p = request->getParam(i);
      Serial.printf("Parameter: %s = %s\n", p->name().c_str(), p->value().c_str());
    }
    request->send(200, "text/plain", "Data received");
  });

  // Start the server
  server.begin();
}

void loop() {
  // Put your main code here, to run repeatedly:
}
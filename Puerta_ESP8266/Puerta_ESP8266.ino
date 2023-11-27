#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>

const char* ssid = "MEGACABLE_2.4G_43F4";
const char* password = "Z6D8M3N3Z4Q4J6h9a2a2";

ESP8266WebServer server(80);

const int ledPin = 2; // Pin donde está conectado el LED
Servo myservo;
int servoPin = D1; // Pin D1 del ESP8266

void setup() {
  Serial.begin(115200);

  myservo.attach(servoPin); // Adjunta el servo al pin correspondiente
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(ledPin, LOW);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  server.on("/encender", []() {
    digitalWrite(LED_BUILTIN, LOW);
    myservo.write(0);
    delay(1000); // Esperar un segundo
    server.send(200, "text/plain", "LED encendido");
    Serial.println("Encendido");
  });

  server.on("/apagar", []() {
    digitalWrite(LED_BUILTIN, HIGH);
    myservo.write(180);
    delay(1000); // Esperar un segundo
    server.send(200, "text/plain", "LED apagado");
    Serial.println("Apagado");
  });

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}

#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h> // Include the ArduinoJson library for JSON parsing

const char* ssid = "prejita@ClassicTech";
const char* password = "Prejita@123";
const char* serverUrl = "http://192.168.254.4:8000/api/dustbin_data_receiver";
const char* worldTimeApiUrl = "http://worldtimeapi.org/api/timezone/Asia/Kathmandu"; // URL for Kathmandu time

// const char* ssid = "HCK Connect";
// const char* password = "#erald77";
// const char* serverUrl = "http://10.22.57.17:8000/api/dustbin_data_receiver";
// const char* worldTimeApiUrl = "http://worldtimeapi.org/api/timezone/Asia/Kathmandu"; // URL for Kathmandu time

const int triggerPin = 22;
const int echoPin = 23;

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

float getDistance() {
  long duration;
  float distance;

  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  return distance;
}

String checkDustbinStatus() {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  unsigned long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2; // Convert duration to distance in cm

  String dustbinStatus;
  if (distance < 5) {
    dustbinStatus = "Full"; // If distance less than 4cm, consider it full
  } else {
    dustbinStatus = "Empty"; // If distance greater than or equal to 4cm, consider it empty
  }

  return dustbinStatus;
}

String getCurrentKathmanduTime() {
  WiFiClient client;
  HTTPClient http;

  if (WiFi.status() == WL_CONNECTED) {
    http.begin(client, worldTimeApiUrl);
    int httpResponseCode = http.GET();

    if (httpResponseCode > 0) {
      String payload = http.getString();
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, payload);
      
      const char* time = doc["datetime"];
      // Extracting only date, hour, and minute
      String formattedTime = time;
      formattedTime.remove(formattedTime.indexOf('T') + 6); // Remove seconds and milliseconds
      return formattedTime;
    } else {
      Serial.printf("Error fetching Kathmandu time, error: %s\n", http.errorToString(httpResponseCode).c_str());
    }

    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  return "";
}

void sendDataToDjango(float distance, String status, String kathmanduTime, String location) {
  WiFiClient client;
  HTTPClient http;

  if (WiFi.status() == WL_CONNECTED) {
    http.begin(client, serverUrl);
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{\"distance\": " + String(distance) + ", \"status\": \"" + status + "\", \"kathmandu_time\": \"" + kathmanduTime + "\", \"location\": \"" + location + "\"}";
    int httpResponseCode = http.POST(jsonData);

    if (httpResponseCode > 0) {
      Serial.printf("HTTP Response code: %d\n", httpResponseCode);
    } else {
      Serial.printf("Error sending POST request, error: %s\n", http.errorToString(httpResponseCode).c_str());
    }

    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }
}

void loop() {
  float distance = getDistance();
  String status = checkDustbinStatus();
  String kathmanduTime = getCurrentKathmanduTime();
  String location = "Herald College Kathmandu"; 

  sendDataToDjango(distance, status, kathmanduTime, location);

  Serial.print("Distance: ");
  Serial.println(distance);
  Serial.print("Status: ");
  Serial.println(status);
  Serial.print("Kathmandu Time: ");
  Serial.println(kathmanduTime);
  Serial.print("Location: ");
  Serial.println(location);

  delay(5000);
}

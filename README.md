# IoT Network Guide Wiki (LLM-Wiki)

이 저장소는 **IoT Network 강의 자료**를 LLM(Large Language Model) 기반의 지식 관리 시스템인 **LLM-Wiki** 형식으로 분석하고 정리한 결과물입니다. 

IoT 서비스 구현을 위한 기초부터 실전 프로젝트까지, 센서 장치, 서버, 모바일, 네트워크의 4대 요소를 중심으로 체계적인 지식을 제공합니다.

---

## 📂 Wiki 구조 및 내용

본 위키는 Obsidian(옵시디언)과 호환되는 Markdown 형식으로 구성되어 있으며, 다음과 같은 폴더 구조를 가집니다:

### 1. [Overview](wiki/overview.md)
*   IoT 네트워크 지식의 종합 요약 및 핵심 통신 계층(유선, Bluetooth, BLE, WiFi)에 대한 개요를 담고 있습니다.

### 2. [Sources](wiki/sources/) (강의 자료 요약)
*   **1장. 사물인터넷과 네트워크**: IoT 입문 및 통신 기술 개요
*   **2장. 유선통신**: 시리얼 통신 기초 및 실습
*   **3장. 블루투스**: Classic BT(SPP) 및 BLE(GATT, iBeacon) 상세 분석
*   **4장. WiFi**: ESP32를 활용한 HTTP 통신, 웹 서버, 웹 소켓 실습
*   **5장. 통합 서비스**: Node.js, MQTT, Telegram 봇 연동
*   **7장. 홈 오토메이션**: 실전 프로젝트 구현 가이드

### 3. [Entities](wiki/entities/) (주요 장치 및 도구)
*   **Hardware**: Arduino, Raspberry Pi, ESP32, ESP8266, HC-06, HM-10, DHT11 등
*   **Software/Library**: Node.js, Express, Mosquitto(MQTT), MariaDB, ArduinoJson 등

### 4. [Concepts](wiki/concepts/) (핵심 개념)
*   통신 규격: Serial, Bluetooth, BLE, GATT, WiFi, MQTT, WebSocket 등
*   기술 개념: SmartConfig, SoftAP, JSON, QoS, Home-Automation 등

### 5. [Originals](wiki/originals/)
*   분석에 사용된 원본 문서들의 텍스트 데이터가 보관되어 있습니다.

---

## 🛠️ 사용 도구 및 기술

*   **LLM-Wiki**: LLM을 활용한 지식 수집, 요약, 연결 시스템
*   **Obsidian**: 로컬 Markdown 기반의 지식 관리 도구 (위키 시각화 및 편집)
*   **Git/GitHub**: 버전 관리 및 협업

---

## 📝 관리 규칙 (LLM-Wiki 스킬)

*   `wiki/index.md`: 모든 페이지의 카탈로그 (자동 업데이트)
*   `wiki/log.md`: 변경 이력 기록 (로컬 전용, .gitignore에 포함됨)
*   `wiki/overview.md`: 전체 지식의 실시간 종합 요약

이 위키는 IoT 개발자들이 기술적 연결 고리를 쉽게 이해하고 필요한 정보를 빠르게 찾을 수 있도록 돕기 위해 제작되었습니다.

---
title: "IoT Network Knowledge Overview"
type: synthesis
last_updated: 2026-04-19
---

# IoT Network Knowledge Overview

이 위키는 IoT 네트워크 및 서비스 구현을 위한 기술적 지식을 정리합니다. 주요 주제는 유선 통신(시리얼)과 무선 통신(블루투스, WiFi, 저전력 통신 등)을 포함합니다.

## IoT의 4대 요소
성공적인 IoT 서비스 구현을 위해서는 다음 4가지 요소의 통합이 필요합니다:
- **센서 장치**: 실시간 데이터 수집 ([[Arduino]], [[ESP32]], [[ESP8266]])
- **서버**: 데이터 처리 및 통합 관리 ([[RaspberryPi]])
- **모바일**: 사용자 인터페이스 및 원격 제어
- **네트워크**: 장치 간 연결 규약 ([[SerialCommunication]], [[WiFi]], [[Bluetooth]] 등)

## 핵심 통신 계층
1. **유선 통신**: 아두이노와 라즈베리파이, 모바일 기기 간의 시리얼 연결을 통해 기초적인 데이터 송수신을 구현합니다. [[SerialCommunication]] 참조.
2. **블루투스**:
   - **클래식 블루투스**: 기존의 블루투스 표준을 사용하여 SPP(Serial Port Profile) 기반의 스트림 통신을 수행합니다. [[ClassicBT]], [[HC-06]] 참조.
   - **BLE (Bluetooth Low Energy)**: 저전력 특성을 활용하여 Advertising/Scanning 및 GATT 기반의 계층적 데이터 통신을 구현합니다. [[BLE]], [[GATT]], [[HM-10]] 참조.
3. **WiFi**: 인터넷 직접 연결 및 로컬 네트워크 구성을 위해 사용됩니다. [[WiFi]], [[ESP32]] 참조.
4. **저전력/장거리 무선**: [[LoRa]], [[Zigbee]], [[RF-Communication]] 등을 통해 특수 목적의 무선 네트워크를 구축합니다.

## 주요 장치 역할
- **센서 장치 (Peripheral/Slave)**: [[Arduino]], [[ESP32]] 등을 사용하여 데이터를 수집하고 방송하거나 요청에 응답합니다.
- **홈 서버 (Central/Master)**: [[RaspberryPi]]를 사용하여 여러 센서 장치를 관리하고 데이터를 통합 처리합니다.
- **모바일**: 사용자 인터페이스 제공 및 실시간 데이터 모니터링, 게이트웨이 역할을 수행합니다.

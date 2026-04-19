---
title: "7장. 홈 오토메이션 구현"
type: source
tags: [IoT, HomeAutomation, Node.js, MariaDB, DHT11, MQTT, Course]
sources: [chap7-home-automation]
source_file: wiki/originals/chap7-home-automation.md
last_updated: 2026-04-19
---

# 7장. 홈 오토메이션 구현
[[사물인터넷과 네트워크 강의]]의 하위 과정입니다.

## 개요
[[ESP32]] 센서 장치, [[Node.js]] 서버, [[MariaDB]] 데이터베이스, 그리고 [[MQTT]]를 통합하여 실전 홈 오토메이션 서비스를 구축하는 과정을 다룹니다.

## 서비스 기획 및 시나리오
- **채널 기반 관리**: 각 센서 장치는 하나의 채널로 관리되며, 채널 생성 시 발급되는 [[Auth-Code]]를 통해 보안을 유지합니다.
- **데이터 흐름**:
    1. 센서 장치가 [[DHT11]]로 온도를 측정.
    2. [[HTTP-POST]]를 통해 [[JSON]] 포맷으로 서버 API에 데이터 전송.
    3. 서버는 수신한 데이터를 [[MariaDB]]에 저장.
    4. 사용자는 웹 대시보드([[CoreUI]], [[Chart.js]])를 통해 실시간 그래프 확인.
    5. 사용자가 웹에서 제어 버튼을 누르면 [[MQTT]]를 통해 장치로 명령([[Publish]]) 전송.

## 서버 구현 ([[Node.js]] & [[MariaDB]])
- **데이터베이스 설계**:
    - `channel_table`: 채널 정보 및 인증 코드 저장.
    - `data_table`: 수집된 센서 데이터와 시간 정보 저장.
- **API 개발**: 데이터 입력 API 및 외부 조회를 위한 [[Data-Query-API]] 구축.
- **푸시 제어**: [[Mosquitto]] 브로커를 통해 장치의 상태(`status`)를 제어하는 MQTT 로직 포함.

## 센서 장치 구현 ([[ESP32]])
- **데이터 업로드**: 측정된 데이터를 서버 주소로 주기적 전송.
- **원격 제어 수신**: MQTT 토픽(예: `채널번호/status`)을 구독([[Subscribe]])하여 '0'(OFF) 또는 '1'(ON) 명령어에 따라 동작 제어.

## 특징 및 장점
- **확장성**: 채널 시스템을 통해 다수의 센서 장치를 유연하게 관리 가능.
- **시각화**: [[Chart.js]]를 활용하여 데이터 변화 추이를 직관적으로 파악.
- **상호 연동**: 웹, 모바일(음성 인식 등), 임베디드 장치가 유기적으로 결합된 [[Home-Automation]] 시스템 구현.

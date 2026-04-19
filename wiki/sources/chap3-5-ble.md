---
title: "3장. Part2. BLE"
type: source
tags: [iot, bluetooth, ble, esp32, beacon, gatt, Course]
date: 2026-04-19
source_file: wiki/originals/chap3-5-ble.md
sources: [chap3-5-ble]
last_updated: 2026-04-19
---

# 3장. Part2. BLE
[[사물인터넷과 네트워크 강의]]의 하위 과정입니다.

## Summary
저전력 블루투스(BLE) 프로토콜의 핵심 개념과 ESP32를 이용한 실습을 다룹니다. Advertising/Scanning 과정, iBeacon 설정, GATT 구조(Service/Characteristic), 그리고 모바일 및 라즈베리파이와의 연결 방법을 설명합니다.

## Key Claims
- BLE는 Advertising(게시)과 Scanning(스캔) 과정을 통해 장치를 인식하며, 연결 후에는 GATT 프로토콜을 사용합니다.
- GATT 구조는 Profile, Service, Characteristic으로 구성되며, 이는 컴퓨터의 폴더/파일 구조와 유사합니다.
- iBeacon은 Advertising 데이터를 특정 규격(UUID, Major, Minor)에 맞춰 방송하는 장치입니다.
- ESP32는 BLE 라이브러리를 통해 GATT Server 또는 Client 역할을 수행할 수 있습니다.
- GATT Client는 Polling 방식 외에도 Notify/Indicate 설정을 통해 Server의 데이터 변경 알림을 받을 수 있습니다.

## Key Quotes
> "BLE 에서는 센서 데이터에 접근하는 체계화 된 방법을 사용  GATT (Generic Attribute Profile)" — Slide 10
> "GATT 구조 Profile – Service – Characteristic 구조  컴퓨터 – 폴더 – 파일 구조와 유사" — Slide 13

## Connections
- [[BLE]] — 핵심 기술
- [[GATT]] — 데이터 통신 프로토콜
- [[iBeacon]] — 위치 기반 서비스 표준
- [[ESP32]] — 하드웨어 모듈
- [[GAP]] — 연결 관리 프로파일

## Contradictions
- 없음.

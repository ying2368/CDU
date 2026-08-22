# GPU Cooling SCADA

GPU 液冷監控 SCADA 系統，使用 **Python + MQTT + ThingsBoard** 建立 GPU Cooling Monitoring Dashboard。

本專案主要用 Python 模擬 GPU 液冷系統的感測器資料，透過 MQTT 傳送至 ThingsBoard，再利用 ThingsBoard SCADA Dashboard 進行即時資料視覺化。

---

## ✨ Features

本專案提供以下功能：

- 🌡️ GPU 溫度監控
- 🚀 GPU GFLOPS 監控
- ⚡ GPU Frequency / Power 監控
- 💧 Water Block（水冷板）溫度監控
- 🔵 Electronic Valve（電子水閥）流量監控
- 🚰 Water Pump（幫浦）流量、電壓、電流與功率監控
- ❄️ Radiator（冷排）進出水溫度監控
- ⚡ System Power 系統總功率監控
- 📈 PUE 能源效率監控
- 🚀 GFLOPS/W GPU 能源效率監控
- 📡 MQTT Telemetry 資料傳輸
- 📊 ThingsBoard SCADA Dashboard
- 🧪 Python Fake Sensor 模擬液冷設備資料

---

## 🏗️ System Architecture

```text
┌───────────────────────┐
│    fake_sensor.py     │
│                       │
│  Generate Fake Data   │
└───────────┬───────────┘
            │
            │ MQTT
            ▼
┌───────────────────────┐
│      ThingsBoard      │
│                       │
│   MQTT / Device       │
└───────────┬───────────┘
            │
            │ Telemetry
            ▼
┌───────────────────────┐
│ GPU Cooling SCADA     │
│                       │
│     Dashboard         │
├───────────────────────┤
│ GPU Monitoring        │
│ Water Block           │
│ Valve                 │
│ Pump                  │
│ Radiator              │
│ System Power          │
│ PUE                   │
│ GFLOPS/W              │
└───────────────────────┘
```

---

## 📌 Project Overview

本專案的資料流程如下：

```text
Python Fake Sensor
        │
        │ MQTT
        ▼
ThingsBoard Device
        │
        │ Telemetry
        ▼
GPU Cooling SCADA Dashboard
```

系統可以模擬以下設備與監控資訊：

- GPU
- Water Block（水冷板）
- Electronic Valve（電子水閥）
- Water Pump（幫浦）
- Radiator（冷排）
- System Power（系統功率）
- PUE
- GFLOPS/W

---

## 📁 Repository Structure

```text
GPU-Cooling-SCADA/
│
├── fake_sensor.py
│   └── Python MQTT 模擬感測器
│
├── gpu_cooling_scada.json
│   └── ThingsBoard GPU Cooling SCADA Dashboard 設定
│
├── requirements.txt
│   └── Python 套件相依性
│
├── .env
│   └── ThingsBoard MQTT 設定與 Device Token
│
├── .gitignore
│   └── Git 忽略設定
│
└── README.md
    └── 專案使用說明
```

> `.venv/` 為本機 Python Virtual Environment，不需要提交至 Git Repository。

### `fake_sensor.py`

負責產生 GPU 液冷系統的模擬 Telemetry 資料，並透過 MQTT 傳送至 ThingsBoard。

程式使用 `paho-mqtt` 建立 MQTT Client，並連線至 ThingsBoard MQTT Server。

### `gpu_cooling_scada.json`

ThingsBoard Dashboard 匯出檔。

匯入 ThingsBoard 後，可以建立 GPU Cooling SCADA 視覺化介面，包含 GPU、水冷板、管路、幫浦等監控元件。

### `requirements.txt`

列出 Python 執行程式所需要安裝的第三方套件。

---

# 🛠️ Requirements

啟動本專案前，需要先安裝以下軟體：

| Software | 建議版本 | 用途 |
|---|---|---|
| Python | 3.10+ | 執行 `fake_sensor.py` |
| pip | 最新版本 | 安裝 Python dependencies |
| Git | 最新版本 | Clone Repository |
| ThingsBoard | Cloud | MQTT Server / Dashboard |

## 🚀 Quick Start

如果是第一次使用本專案，可以依照以下步驟快速啟動。

### 1. Clone Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

### 2. 建立 Virtual Environment

Windows：

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

啟用成功後，Terminal 通常會顯示：

```text
(.venv)
```

### 3. 安裝 Python Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# ☁️ ThingsBoard Setup

本專案使用 ThingsBoard 接收 MQTT Telemetry。

啟動 Python Sensor 前，需要先在 ThingsBoard 建立一個 Device。

## 1. 建立 Device

登入 ThingsBoard Cloud。

建立一個新的 Device，例如：

```text
Device Name:
GPU Cooling SCADA
```

建立完成後取得該 Device 的 Access Token。

---

## 2. MQTT Connection

Python Sensor 使用 MQTT 連接 ThingsBoard。

主要設定：

```text
MQTT Host:
mqtt.thingsboard.cloud

MQTT Port:
1883
```

Telemetry 使用 ThingsBoard MQTT API：

```text
v1/devices/me/telemetry
```

---

# 🔐 Environment Variables

本專案使用 `python-dotenv` 讀取 `.env`，將 ThingsBoard Device Token、MQTT Host 與 MQTT Port 放在環境變數中。

在專案根目錄建立：

```text
.env
```

內容：

```env
THINGSBOARD_TOKEN=YOUR_DEVICE_TOKEN
MQTT_HOST=YOUR_MQTT_HOST
MQTT_PORT=YOUR_MQTT_PORT
```

例如：
```env
THINGSBOARD_TOKEN=xxxxxxxxxxxxxxxxxxxx
MQTT_HOST=mqtt.thingsboard.cloud
MQTT_PORT=1883
```

---

# ▶️ Run Fake Sensor

完成以下設定後：

1. Python 安裝
2. Virtual Environment
3. Python Dependencies
4. ThingsBoard Device
5. `.env` 設定

即可啟動 Fake Sensor：

```bash
python fake_sensor.py
```

如果連線成功，Terminal 會開始顯示資料傳送訊息。

程式會持續產生 GPU Cooling 系統的模擬資料，並透過 MQTT 傳送至 ThingsBoard。

停止程式：

```text
Ctrl + C
```

---

# 📊 Telemetry Data

## GPU

本專案模擬 4 顆 GPU。

每顆 GPU 包含：

| Telemetry Key | 說明 | Unit |
|---|---|---|
| `gpu1_temp` ~ `gpu4_temp` | GPU 晶片溫度 | °C |
| `gpu1_gflops` ~ `gpu4_gflops` | GPU 算力 | GFLOPS |
| `gpu1_freq` ~ `gpu4_freq` | GPU 核心頻率 | MHz |
| `gpu1_power` ~ `gpu4_power` | GPU 功率 | W |

另外會計算：

```text
total_gflops
total_gpu_power
```

---

## 💧 Water Block

每顆 GPU 對應一組水冷板資料：

| Telemetry Key | 說明 | Unit |
|---|---|---|
| `water_block1_temp` ~ `water_block4_temp` | 水冷板溫度 | °C |
| `inlet1_temp` ~ `inlet4_temp` | 水冷板入水溫度 | °C |
| `outlet1_temp` ~ `outlet4_temp` | 水冷板出水溫度 | °C |

---

## 🔵 Electronic Valve

4 路電子水閥：

| Telemetry Key | 說明 | Unit |
|---|---|---|
| `valve1_flow` ~ `valve4_flow` | 各路流量 | L/min |

---

## 🚰 Water Pump

幫浦資料：

| Telemetry Key | 說明 | Unit |
|---|---|---|
| `pump_flow` | 幫浦流量 | L/min |
| `pump_voltage` | 幫浦電壓 | V |
| `pump_current` | 幫浦電流 | A |
| `pump_power` | 幫浦功率 | W |

幫浦功率由以下公式計算：

```text
pump_power = pump_voltage × pump_current
```

---

## ❄️ Radiator

冷排資料：

| Telemetry Key | 說明 | Unit |
|---|---|---|
| `radiator_inlet_temp` | 冷排入水溫度 | °C |
| `radiator_outlet_temp` | 冷排出水溫度 | °C |

---

## ⚡ System Power

系統總功率：

```text
system_power
```

Unit：

```text
W
```

---

## 📈 PUE

Power Usage Effectiveness：

```text
pue
```

目前 Fake Sensor 使用：

```text
PUE = system_power / total_gpu_power
```

---

## 🚀 GFLOPS/W

GPU 能源效率：

```text
gflops_per_w
```

用於觀察 GPU 算力與功耗之間的效率。

---

# 📊 ThingsBoard Dashboard

Dashboard 設定檔：

```text
gpu_cooling_scada.json
```

可以透過 ThingsBoard Dashboard Import 功能匯入。

基本流程：

```text
ThingsBoard
    │
    ├── Dashboards
    │
    ├── Import Dashboard
    │
    └── gpu_cooling_scada.json
```

匯入完成後，確認 Dashboard 的 Entity Alias 指向目前使用的 GPU Cooling Device。

---

# 🖥️ Dashboard Functions

Dashboard 主要提供 GPU 液冷系統的即時監控。

包含：

### GPU Monitoring

- GPU Temperature
- GPU GFLOPS
- GPU Frequency
- GPU Power
- Total GPU Power
- Total GFLOPS

### Cooling System

- Water Block Temperature
- Inlet Temperature
- Outlet Temperature
- Valve Flow
- Pump Flow
- Pump Voltage
- Pump Current
- Pump Power
- Radiator Temperature

### Energy Monitoring

- System Power
- PUE
- GFLOPS/W

---

# 🔍 Troubleshooting

## Dashboard 沒有資料

依序確認：

```text
1. fake_sensor.py 是否正常執行
        ↓
2. MQTT 是否成功連線
        ↓
3. ThingsBoard Device 是否收到 Telemetry
        ↓
4. Dashboard Entity Alias 是否指向正確 Device
        ↓
5. Dashboard Data Key 是否與 Telemetry Key 相同
```

例如 Dashboard 使用：

```text
water_block1_temp
```

則 ThingsBoard Device 必須存在完全相同的 Telemetry Key。

## Device 有 Telemetry，但 Dashboard 沒資料

優先檢查 Dashboard 的 Entity Alias。確認 Dashboard 所選的 Device 是目前 Fake Sensor 使用的 Device。

同時確認 Dashboard Widget 使用的 Data Key 與 Fake Sensor 傳送的 Telemetry Key 完全一致。

## `ModuleNotFoundError`

如果出現：

```text
ModuleNotFoundError
```

請確認 Virtual Environment 已啟用。

Windows：

```powershell
.venv\Scripts\activate
```

然後重新安裝：

```bash
python -m pip install -r requirements.txt
```

## MQTT 無法連線

確認以下設定是否正確：

```text
THINGSBOARD_HOST
THINGSBOARD_PORT
THINGSBOARD_TOKEN
```

並確認 ThingsBoard Device 已建立且 Token 有效。

---

# 📌 Development Notes

本專案目前的 Sensor Data 為 **模擬資料**，主要用於：

- GPU Cooling SCADA Dashboard Demo
- MQTT 通訊測試
- ThingsBoard IoT Dashboard
- 液冷系統監控概念驗證
- 專題展示與測試

實際部署時，可以將 `fake_sensor.py` 替換為實體 GPU、溫度感測器、流量計、電壓/電流感測器等設備的資料來源。

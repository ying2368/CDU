import paho.mqtt.client as mqtt
import json
import random
import time
import os  
from dotenv import load_dotenv  

load_dotenv()

# =====================================
# ThingsBoard MQTT 設定
# =====================================
TOKEN = os.getenv("THINGSBOARD_TOKEN")

if not TOKEN:
    raise ValueError("錯誤：找不到 ThingsBoard Token，請確認是否已設定！")

MQTT_HOST = "mqtt.thingsboard.cloud"
MQTT_PORT = 1883

client = mqtt.Client()
client.username_pw_set(TOKEN)
client.connect(MQTT_HOST, MQTT_PORT, 60)

print("開始發送 GPU 液冷監控模擬資料...")

try:
    while True:

        # 儲存所有 Telemetry 資料
        data = {}

        # =====================================================
        # 1. GPU 資訊
        # =====================================================
        total_gflops = 0          # 總算力
        total_gpu_power = 0       # GPU總功率

        for i in range(1, 5):

            # -------- GPU晶片溫度(°C) --------
            temp = random.randint(45, 80)

            # -------- GPU算力(GFLOPS) --------
            gflops = random.randint(450, 650)

            # -------- GPU核心頻率(MHz) --------
            freq = random.randint(1500, 2100)

            # -------- GPU功率(W) --------
            power = round(random.uniform(180, 320), 2)

            data[f"gpu{i}_temp"] = temp
            data[f"gpu{i}_gflops"] = gflops
            data[f"gpu{i}_freq"] = freq
            data[f"gpu{i}_power"] = power

            total_gflops += gflops
            total_gpu_power += power

        # -------- 總GPU算力 --------
        data["total_gflops"] = total_gflops

        # -------- 總GPU功率 --------
        data["total_gpu_power"] = round(total_gpu_power, 2)

        # =====================================================
        # 2. 水冷板資訊
        # =====================================================
        for i in range(1, 5):

            # 入水口溫度
            inlet = round(random.uniform(25, 30), 2)

            # 出水口溫度
            outlet = round(inlet + random.uniform(3, 8), 2)

            # 水冷板平均溫度
            block = round((inlet + outlet) / 2 + random.uniform(3, 5), 2)

            # 水冷板溫度
            data[f"water_block{i}_temp"] = block

            # 入水溫
            data[f"inlet{i}_temp"] = inlet

            # 出水溫
            data[f"outlet{i}_temp"] = outlet

        # =====================================================
        # 3. 電子水閥流量
        # =====================================================
        total_flow = 0

        for i in range(1, 5):

            # 每一路流量(L/min)
            flow = round(random.uniform(2.0, 4.0), 2)

            data[f"valve{i}_flow"] = flow

            total_flow += flow

        # =====================================================
        # 4. 幫浦
        # =====================================================

        # 幫浦電壓(V)
        pump_voltage = round(random.uniform(11.8, 12.2), 2)

        # 幫浦電流(A)
        pump_current = round(random.uniform(1.8, 3.2), 2)

        # 幫浦流量(L/min)
        data["pump_flow"] = round(total_flow, 2)

        # 幫浦電壓
        data["pump_voltage"] = pump_voltage

        # 幫浦電流
        data["pump_current"] = pump_current

        # 幫浦功率(W)
        data["pump_power"] = round(pump_voltage * pump_current, 2)

       
        # =====================================================
        # 5. 冷排溫度
        # =====================================================

        # 冷排入水溫
        data["radiator_inlet_temp"] = round(random.uniform(34, 38), 2)

        # 冷排出水溫
        data["radiator_outlet_temp"] = round(random.uniform(26, 30), 2)

        # =====================================================
        # 6. 系統功率
        # =====================================================

        # 系統總功率
        system_power = (
            total_gpu_power
            + data["pump_power"]
            + random.uniform(20, 60)
        )

        data["system_power"] = round(system_power, 2)

        # =====================================================
        # 7. PUE (Power Usage Effectiveness)
        # =====================================================

        data["pue"] = round(system_power / total_gpu_power, 2)

        # =====================================================
        # 8. GFLOPS/W (能源效率)
        # =====================================================

        data["gflops_per_w"] = round(total_gflops / system_power, 2)

        # =====================================================
        # 發送資料至 ThingsBoard
        # =====================================================

        client.publish(
            "v1/devices/me/telemetry",
            json.dumps(data)
        )

        print("=" * 60)
        print("成功送出一筆模擬資料")
        print(json.dumps(data, indent=4, ensure_ascii=False))

        # 每5秒送一次
        time.sleep(5)

except KeyboardInterrupt:
    print("程式已停止")

    client.disconnect()
# SCADA Data Dictionary
This document defines the historian data fields used in the SCADA automation scripts.

## 📌 Historian Data Fields
| Field Name   | Description                      | Example Value          |
|-------------|----------------------------------|------------------------|
| `timestamp`  | Time of the recorded data point | 2025-03-09 10:00:00    |
| `tag`        | SCADA variable name             | FlowRate               |
| `value`      | Recorded measurement            | 120                    |
| `unit`       | Measurement unit                | L/min, psi, °C         |

## 📌 Tag Descriptions
| Tag Name    | Meaning                        | Normal Range  | Unit  |
|------------|--------------------------------|--------------|------|
| `FlowRate`  | Measures the flow of liquid/gas | 100 - 180    | L/min |
| `Pressure`  | Measures system pressure       | 50 - 90      | psi  |
| `Temperature` | Measures system temperature  | 20 - 85      | °C   |

## 📌 Alert Conditions
- **High FlowRate**: Triggered if `FlowRate > 180 L/min`
- **High Temperature**: Triggered if `Temperature > 90°C`
- **Pressure Spike** (Future Implementation): If `Pressure > 100 psi`, log as a warning.

---

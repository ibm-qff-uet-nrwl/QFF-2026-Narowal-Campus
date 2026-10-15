# Qiskit Fall Fest - Grading Module (grader.py)

This folder contains the automated grading system for the Qiskit Fall Fest labs. 

**📌 Important Note for Beginners:**
The lab instructions and detailed explanations are provided in **both English and Urdu**. This is to ensure that learners without a strong background in English or quantum physics can easily understand the basic concepts.

---

## 📂 What's inside?
*   `grader.py`: The core Python script that checks student answers using Qiskit's `Statevector` simulation.

## ⚙️ How it works
Students do not need to download this file manually. In their Google Colab notebooks, the first setup cell automatically downloads this `grader.py` file directly from this repository using `wget`. 

Once downloaded, students can import the grading functions directly into their notebooks.

## 🧪 Available Grading Functions
The `grader.py` file currently supports the following labs:

| Lab No. | Function Name | Objective |
| :--- | :--- | :--- |
| Lab 1 | `grade_lab1_single_qubit` | Checks if a single qubit is in the \|+> superposition state. |
| Lab 2 | `grade_lab2_bell_state` | Checks if two qubits are correctly entangled in a Bell State. |
| Lab 3 | `grade_lab3_ghz_state` | Checks if three qubits are correctly entangled in a GHZ State. |

## 🚀 How to use (Example for Lab 1)
```python
from qiskit import QuantumCircuit
from grader import grade_lab1_single_qubit

qc = QuantumCircuit(1)
# Student writes their code here
# qc.h(0)

result = grade_lab1_single_qubit(qc)
print(f"Score: {result['score']}/{result['max']}")
print(result['msg'])
````
<div dir="rtl" align="right">
کِسکٹ فال فیسٹ - گریڈنگ ماڈیول
  
  (grader.py)
یہ فولڈر کِسکٹ فال فیسٹ کی لیبز کے لیے خودکار گریڈنگ سسٹم پر مشتمل ہے۔


📌 نئے سیکھنے والوں کے لیے اہم نوٹ:
لیبز کی ہدایات اور تفصیلی وضاحت انگریزی کے ساتھ ساتھ اردو میں بھی فراہم کی گئی ہے۔ اس کا مقصد یہ ہے کہ انگریزی یا کوانٹم فزکس میں کمزور پس منظر رکھنے والے طلباء بھی بنیادی تصورات کو آسانی سے سمجھ سکیں۔

📂 اس فولڈر میں کیا ہے؟
grader.py:

یہ بنیادی پائتھون اسکرپٹ ہے جو Qiskit کے Statevector سمولیشن کا استعمال کرتے ہوئے طلباء کے جوابات کو چیک کرتی ہے۔

⚙️ یہ کیسے کام کرتا ہے؟
طلباء کو اس فائل کو دستی طور پر ڈاؤن لوڈ کرنے کی ضرورت نہیں ہے۔ ان کے گوگل کولاب (Colab) نوٹ بک میں، پہلا سیٹ اپ سیل خود بخود wget کا استعمال کرتے ہوئے اس ریپو سے grader.py فائل ڈاؤن لوڈ کر لیتا ہے۔

ڈاؤن لوڈ ہونے کے بعد، طلباء گریڈنگ فنکشنز کو براہ راست اپنی نوٹ بک میں امپورٹ کر سکتے ہیں۔

🧪 دستیاب گریڈنگ فنکشنز
grader.py فائل فی الحال درج ذیل لیبز کو سپورٹ کرتی ہے:

لیب نمبر	فنکشن کا نام	مقصد
لیب 1	grade_lab1_single_qubit	چیک کرتا ہے کہ کیا ایک کیوبٹ صحیح طرح |+> سپر پوزیشن اسٹیٹ میں ہے۔
لیب 2	grade_lab2_bell_state	چیک کرتا ہے کہ کیا دو کیوبٹس صحیح طرح بیل اسٹیٹ میں اینٹینگل ہیں۔
لیب 3	grade_lab3_ghz_state	چیک کرتا ہے کہ کیا تین کیوبٹس صحیح طرح GHZ اسٹیٹ میں اینٹینگل ہیں۔

Prepared by Noor Ul Ain Faisal IBM Qiskit Advocate

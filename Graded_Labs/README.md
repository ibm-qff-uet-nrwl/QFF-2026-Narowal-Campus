# Qiskit Fall Fest 2026 - Graded Labs

Welcome! These are the graded labs for Qiskit Fall Fest 2026 at Narowal Campus.

There are **4 labs**. Each lab teaches one quantum computing concept using Qiskit. To pass a lab, you must score **10/10**.

---

## 📖 What Each Lab Is & How to Pass

### 🧪 Lab 1: Single Qubit State (|+>)

**What you will learn:**  
How to put a single qubit into **superposition** — the state where it is both 0 and 1 at the same time.

**How to pass:**
1. Create a `QuantumCircuit` with 1 qubit.
2. Apply a **Hadamard gate** (`qc.h(0)`) to the qubit.
3. Run the grading cell.

**Solution hint:** Uncomment the line `qc.h(0)`.

---

### 🧪 Lab 2: Multi-Qubit Gates (CNOT)

**What you will learn:**  
How to use the **CNOT gate** to make two qubits interact with each other.

**How to pass:**
1. Create a `QuantumCircuit` with 2 qubits.
2. Apply a **Hadamard gate** to qubit 0.
3. Apply a **CNOT gate** with control=0 and target=1 (`qc.cx(0, 1)`).
4. Run the grading cell.

**Solution hint:** Uncomment the lines `qc.h(0)` and `qc.cx(0, 1)`.

---

### 🧪 Lab 3: Bell State (Entanglement)

**What you will learn:**  
How to create a **Bell State** — the simplest example of quantum entanglement.

**Expected State:** (|00> + |11>) / √2

**How to pass:**
1. Create a `QuantumCircuit` with 2 qubits.
2. Apply a **Hadamard gate** to qubit 0.
3. Apply a **CNOT gate** with control=0 and target=1 (`qc.cx(0, 1)`).
4. Run the grading cell.

**Solution hint:** Uncomment the lines `qc.h(0)` and `qc.cx(0, 1)`.

---

### 🧪 Lab 4: GHZ State (Three-Qubit Entanglement)

**What you will learn:**  
How to create a **GHZ State** — a three-qubit entangled state.

**Expected State:** (|000> + |111>) / √2

**How to pass:**
1. Create a `QuantumCircuit` with 3 qubits.
2. Apply a **Hadamard gate** to qubit 0.
3. Apply a **CNOT gate** with control=0 and target=1 (`qc.cx(0, 1)`).
4. Apply a **CNOT gate** with control=1 and target=2 (`qc.cx(1, 2)`).
5. Run the grading cell.

**Solution hint:** Uncomment the lines `qc.h(0)`, `qc.cx(0, 1)`, and `qc.cx(1, 2)`.

---

## 🎯 Rules

- Each lab is worth **10 points**.
- Total: **40 points**.
- You must score **10/10** to unlock the explanation.
- The explanation is given in **English and Urdu** to help you understand.

---

## 🚀 How to Start

1. Open the notebook in **Google Colab**.
2. Run the **Setup cell** (installs Qiskit and prepares the environment).
3. Solve the lab by writing your code.
4. Run the **grading cell** to see your score.
5. Score **10/10** to unlock the explanation.

---

## 💡 Tips

- Read the instructions carefully before writing code.
- If you get a low score, read the feedback message — it tells you what is missing.
- If you are stuck, the solution is usually in the comments (just uncomment the line).

**Happy Quantum Computing!** ⚛️

---
---

<div dir="rtl" align="right">

# کِسکٹ فال فیسٹ 2026 - گریڈڈ لیبز

خوش آمدید! یہ کِسکٹ فال فیسٹ 2026 (نارووال کیمپس) کی گریڈڈ لیبز ہیں۔

کل **4 لیبز** ہیں۔ ہر لیب Qiskit کا استعمال کرتے ہوئے کوانٹم کمپیوٹنگ کا ایک تصور سکھاتی ہے۔ لیب پاس کرنے کے لیے **10/10** اسکور کرنا ضروری ہے۔

---

## 📖 ہر لیب کیا ہے اور کیسے پاس کریں

### 🧪 لیب 1: ایک کیوبٹ کی اسٹیٹ (|+>)

**آپ کیا سیکھیں گے:**  
ایک کیوبٹ کو **سپر پوزیشن** میں کیسے لانا ہے — وہ حالت جہاں وہ بیک وقت 0 اور 1 ہوتا ہے۔

**کیسے پاس کریں:**
1. `QuantumCircuit(1)` سے ایک کیوبٹ کا سرکٹ بنائیں۔
2. کیوبٹ پر **Hadamard گیٹ** (`qc.h(0)`) لگائیں۔
3. گریڈنگ سیل چلائیں۔

**حل کا اشارہ:** `qc.h(0)` والی لائن سے `#` ہٹا دیں۔

---

### 🧪 لیب 2: ملٹی کیوبٹ گیٹس (CNOT)

**آپ کیا سیکھیں گے:**  
**CNOT گیٹ** کا استعمال کرتے ہوئے دو کیوبٹس کو آپس میں کیسے جوڑنا ہے۔

**کیسے پاس کریں:**
1. `QuantumCircuit(2)` سے دو کیوبٹ کا سرکٹ بنائیں۔
2. کیوبٹ 0 پر **Hadamard گیٹ** لگائیں۔
3. **CNOT گیٹ** لگائیں جہاں کنٹرول=0 اور ٹارگٹ=1 ہو (`qc.cx(0, 1)`)۔
4. گریڈنگ سیل چلائیں۔

**حل کا اشارہ:** `qc.h(0)` اور `qc.cx(0, 1)` والی لائنوں سے `#` ہٹا دیں۔

---

### 🧪 لیب 3: بیل اسٹیٹ (اینٹینگلمنٹ)

**آپ کیا سیکھیں گے:**  
**بیل اسٹیٹ** کیسے بناتے ہیں — جو کوانٹم اینٹینگلمنٹ کی سب سے سادہ مثال ہے۔

**متوقع اسٹیٹ:** (|00> + |11>) / √2

**کیسے پاس کریں:**
1. `QuantumCircuit(2)` سے دو کیوبٹ کا سرکٹ بنائیں۔
2. کیوبٹ 0 پر **Hadamard گیٹ** لگائیں۔
3. **CNOT گیٹ** لگائیں جہاں کنٹرول=0 اور ٹارگٹ=1 ہو (`qc.cx(0, 1)`)۔
4. گریڈنگ سیل چلائیں۔

**حل کا اشارہ:** `qc.h(0)` اور `qc.cx(0, 1)` والی لائنوں سے `#` ہٹا دیں۔

---

### 🧪 لیب 4: GHZ اسٹیٹ (تین کیوبٹس کی اینٹینگلمنٹ)

**آپ کیا سیکھیں گے:**  
**GHZ اسٹیٹ** کیسے بناتے ہیں — جو تین کیوبٹس کی اینٹینگلڈ اسٹیٹ ہے۔

**متوقع اسٹیٹ:** (|000> + |111>) / √2

**کیسے پاس کریں:**
1. `QuantumCircuit(3)` سے تین کیوبٹ کا سرکٹ بنائیں۔
2. کیوبٹ 0 پر **Hadamard گیٹ** لگائیں۔
3. **CNOT گیٹ** لگائیں جہاں کنٹرول=0 اور ٹارگٹ=1 ہو (`qc.cx(0, 1)`)۔
4. **CNOT گیٹ** لگائیں جہاں کنٹرول=1 اور ٹارگٹ=2 ہو (`qc.cx(1, 2)`)۔
5. گریڈنگ سیل چلائیں۔

**حل کا اشارہ:** `qc.h(0)`، `qc.cx(0, 1)`، اور `qc.cx(1, 2)` والی لائنوں سے `#` ہٹا دیں۔

---

## 🎯 اصول

- ہر لیب **10 پوائنٹس** کی ہے۔
- کل: **40 پوائنٹس**۔
- وضاحت کھولنے کے لیے **10/10** اسکور کرنا ضروری ہے۔
- وضاحت **انگریزی اور اردو** دونوں میں دی جاتی ہے تاکہ سمجھنے میں آسانی ہو۔

---

## 🚀 کیسے شروع کریں

1. گوگل کولاب میں نوٹ بک کھولیں۔
2. **سیٹ اپ سیل** چلائیں (Qiskit انسٹال اور ماحول تیار کرتا ہے)۔
3. اپنا کوڈ لکھ کر لیب حل کریں۔
4. **گریڈنگ سیل** چلائیں تاکہ اپنا اسکور دیکھیں۔
5. **10/10** حاصل کریں تاکہ وضاحت کھل جائے۔

---

## 💡 مشورے

- کوڈ لکھنے سے پہلے ہدایات غور سے پڑھیں۔
- اگر کم اسکور آئے، تو فیڈبیک کا پیغام پڑھیں — یہ بتاتا ہے کہ کیا کمی ہے۔
- اگر پھنس جائیں، تو حل عموماً کمنٹس میں ہوتا ہے (صرف `#` ہٹا دیں)۔

**خوشگوار کوانٹم کمپیوٹنگ!** ⚛️

</div>

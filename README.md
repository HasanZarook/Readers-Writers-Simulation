# 📖 Readers–Writers Problem Simulation

This project is a Python implementation and **visualization** of the classic **Readers–Writers synchronization problem** in Operating Systems.  

It demonstrates:
- **Thread scheduling** between readers and writers  
- **Starvation avoidance mechanism**  
- **Priority switching (Reader-first or Writer-first)**  
- **Interactive configuration** (Tkinter UI)  
- **Graphical visualization** (Pygame animation)  

---

## 🛠 Features
- **Reader/Writer threads** created dynamically with random execution times.  
- **Priority switching**: user can choose `Reader` or `Writer` priority.  
- **Starvation detection & handling**: if one side monopolizes resources, scheduler balances it.  
- **Interactive controls**:
  - Tkinter GUI to configure:
    - `lamGen`: rate of thread generation  
    - `lamRW`: execution time distribution  
    - Priority (toggle between Reader/Writer)  
- **Visualization**:
  - Pygame-based GUI shows scheduling, waiting, and execution states of threads.  
  - Displays timing information (`Generate Time`, `Execution Time`).  

---

## 📂 Project Structure
```

Readers-Writers-Simulation/
│
├── main.py              # Entry point, starts Generator, Scheduler, GUI
├── Book.py              # Shared resource with read/write synchronization
├── Reader.py            # Reader thread implementation
├── Writer.py            # Writer thread implementation
├── SystemControl.py     # Generator & Scheduler with starvation avoidance
├── Gui.py               # Pygame-based visualization of states
├── Button.py            # Tkinter toggle for Reader/Writer priority
├── Input\_box\_lambda.py  # Tkinter input boxes for lamGen and lamRW
├── globcfg.py           # Global config and shared state variables

````

---

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install pygame
````

(Tkinter comes pre-installed with Python)

2. Run the program:

   ```bash
   python main.py
   ```

3. Controls:

   * Use Tkinter windows to set parameters (`lamGen`, `lamRW`, priority).
   * Observe scheduling & execution in the Pygame window.

---

## 🎮 Visualization

* **Scheduling Block**: threads waiting to be scheduled.
* **Writer Wait Block**: writers waiting to acquire the lock.
* **Reader Wait Block**: readers waiting to acquire the lock.
* **File Block**: threads currently reading/writing.

Each thread is labeled with:

* **W** = Writer
* **R** = Reader
* Subscript ID to identify unique threads.

---

## 📊 Concepts Demonstrated

* Readers–Writers Synchronization Problem
* Multithreading in Python (`threading.Thread`)
* Condition Variables & Locks
* Starvation and starvation-avoidance scheduling
* Random event generation (`expovariate` for realistic timings)
* GUI development with Tkinter + Pygame

---

## 👨‍💻 Author

* Hasan Zarook (2021-CE-58)

---

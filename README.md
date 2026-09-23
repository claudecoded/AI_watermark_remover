# 📸 AI & Image Watermark Remover

An open-source Python project designed to remove watermarks, text, and logos from images using digital image processing via **OpenCV (Inpainting)**.

<img width="1456" height="720" alt="image" src="https://github.com/user-attachments/assets/e89c0eef-6e05-43ab-a885-3ba4ff53d358" />

## 🛠️ Tech Stack

- **Python 3.8+**
- **OpenCV** (Image Processing)
- **NumPy** (Matrix Manipulation)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install dependencies
You can install the dependencies via requirements:
```bash
pip install -r requirements.txt
```
Or install the project locally as a package:
```bash
pip install -e .
```

### 4. Run the script
1. Create a folder named `input/` in the project root.
2. Add your watermarked image named `watermarked_image.jpg` inside it.
3. Run the following command:
```bash
python src/main.py
```
4. The output will be generated inside the `output/` folder.

## 🧠 Roadmap (AI Integration)
- [ ] Implement automatic watermark segmentation using **SAM (Segment Anything Model)**.
- [ ] Integrate deep generative inpainting models like **LaMa** or **Stable Diffusion**.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

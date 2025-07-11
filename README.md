# 🔁 Reproduction of "Revisiting Change Captioning from Self-supervised Global-Part Alignment (AAAI 2025)" based on FINER-MLLM (ACM MM 2024)

This repository provides the **reproduction of "Contrastive Change Captioning with Cross-modal Attention" (AAAI 2025)** using the codebase of **[FINER-MLLM (ACM MM 2024)](https://openreview.net/pdf/481cf588998fae1e01a42765ae7154fa08b51e85.pdf)**.

> 🛠️ This work is based on the official implementation of FINER-MLLM and modifies its structure and training procedure to align with the design in "Revisiting Change Captioning from Self-supervised Global-Part Alignment".

---

## 📄 Reference

- **Base Code**: [FINER-MLLM (ACM MM 2024)](https://github.com/izhangxian/FINER-MLLM)
- **Target Paper**: *Revisiting Change Captioning from Self-supervised Global-Part Alignment*, AAAI 2025. [[PDF Link]](https://ojs.aaai.org/index.php/AAAI/article/view/32629) 

---

## 🔧 Major Modifications

To reproduce the AAAI 2025 method, we made the following changes based on FINER-MLLM:
- Retain only the **base BLIP model** from FINER-MLLM and remove all other modules to match the settings in the AAAI 2025 paper. 
- Introduced a **Fusion Change Adapter Encoder module** to fuse visual and textual features, as described in the AAAI 2025 paper.

> Note: We keep the data preprocessing, evaluation pipeline, and overall training setup consistent with FINER-MLLM to ensure comparability.

---

## 🚀 Getting Started

### 1. Installation

We follow the same environment setup as FINER-MLLM:

	•	Python 3.9
	•	PyTorch and torchvision.
	•	huggingface
	•	lavis
	•	loralib


### 2. Data Preparation
We use the same datasets as FINER-MLLM:
	•	CLEVR-Change
	•	Spot-the-Diff
	•	Image-Editing-Request

Refer to FINER-MLLM’s data preparation instructions to download and preprocess the datasets.

Make sure the evaluation annotation files are placed under eval_data/:


### 3. Training & Evaluation
Please make sure to modify the dataset paths (clevr_path, spot_path) in the scripts to match the location of your local datasets before running.
If you want to use **ViT-extracted features** (BLIP default), please run:
```
# Train the model on CLEVR-Change
bash scripts/train_clevr.sh

# Train the model on Spot-the-diff
bash scripts/train_spot.sh
```
If you want to use **ResNet-extracted features**, please run:

```
# Train the model on CLEVR-Change
bash scripts/resnet_train__clevr.sh

# Train the model on Spot-the-diff
bash scripts/resnet_train_spot.sh
```

### 4. Citation
@inproceedings{zhang2024finermllm,
  title={Differential-Perceptive and Retrieval-Augmented {MLLM} for Change Captioning},
  author={Zhang, Xian and Wen, Haokun and Wu, Jianlong and Qin, Pengda and Xue, Hui and Nie, Liqiang},
  booktitle={ACM Multimedia},
  year={2024}
}

@inproceedings{lv2025revisiting,
  title={Revisiting Change Captioning from Self-supervised Global-Part Alignment},
  author={Feixiao Lv, Rui Wang, Lihua Jing},
  booktitle={AAAI},
  year={2025}
}
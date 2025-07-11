# 🔁 Reproduction of "Revisiting Change Captioning from Self-supervised Global-Part Alignment (AAAI 2025)"

This repository provides the **reproduction of "Contrastive Change Captioning with Cross-modal Attention" (AAAI 2025)**.

We were impressed by the outstanding performance reported in the SSGPA paper, which shows significant improvements over existing methods. However, there are some aspects in the workflow of this method that may require further clarification or refinement:
1. **Contradictory Model Structure Descriptions**: The paper presents conflicting accounts of the visual feature extraction pipeline. The architecture diagram suggests the use of a frozen ViT with a Fusion Change Adapter Encoder (similar to VIR-VLFM’s Fused Adapter), while the main text also mentions the use of ResNet followed by self-attention for global-local relation learning—closer to CNN+Transformer approaches. Moreover, the experiment section references both ResNet-101 and EVA-ViT-g/14 as backbones. These discrepancies make it unclear which pipeline was actually used.
2. **GPU Memory Usage Inconsistent with Claimed Setup**: The paper claims all experiments were run on a single RTX 3090 GPU. However, using either backbone (ResNet or EVA-ViT-g/14) with Vicuna-7B far exceeds the memory limits of a 24GB 3090, even with half-precision and memory optimizations. Our reproduction attempts required 30–70 GB of GPU memory, calling into question the feasibility of the claimed hardware configuration.
3. **Unclear Vision-Language Integration**: The model feeds image features directly into a frozen Vicuna-7B without mention of any bridging components like Q-Former, MLP projection layers, or fine-tuning. Without a cross-modal alignment module or adaptation, it is unclear how the model achieves high-quality generation, especially with significantly better CIDEr and SPICE scores than prior work.
4. **Unrealistic Visualization Quality**: The change localization visualizations in the paper exhibit highly regular, accurate contours that differ from the typical outputs seen in related works. This suggests the possible use of post-processing or heuristic refinement strategies that were not disclosed.
We initially reached out to the authors requesting access to the code implementation. However, due to certain constraints, the authors indicated that the code cannot be made publicly available at this time. Therefore, we attempted to reproduce the paper's results based on the provided descriptions. During this process, we encountered several technical details that seem challenging to reconcile with standard practices, and some key implementation parameters were missing from the paper. We filled in these gaps based on our understanding and commonly used configurations in the field
---
## Results on CLEVR-Change
| Method                        | BLEU-4                     | METEOR                     | CIDEr                      | ROUGE-L                    |
|------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| SCORER                       | 56.3                       | 41.2                       | 126.8                      | 74.5                       |
| VIR-VLFM                     | 58.2                       | 42.6                       | 153.4                      | 78.9                       |
| SSGPA (reported)             | 60.9                       | 44.2                       | 159.1                      | 80.2                       |
| Reproduction - (ViT-based)   | 33.5 **(↓44.99%)**         | 17.0 **(↓61.54%)**         | 65.3  **(↓58.74%)**        | 50.3 **(↓37.29%)**         |
| Reproduction - (ResNet + ViT)| 32.4 **(↓53.20%)**         | 14.5 **(↓67.19%)**         | 91.4  **(↓42.45%)**        | 48.9 **(↓39.01%)**         |

## Results on Spot-the-diff
| Method                        | BLEU-4                     | METEOR                     | CIDEr                      | ROUGE-L                    |
|------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| SCORER                       | 10.2                       | 12.2                       | 38.9                       | -                          |
| VIR-VLFM                     | 12.2                       | 15.3                       | 48.9                       | 36.2                       |
| SSGPA (reported)             | 13.5                       | 16.0                       | 63.4                       | 42.7                       |
| Reproduction - (ViT-based)   | 9.0  **(↓33.33%)**         | 11.7  **(↓26.88%)**        | 29.7 **(↓53.15%)**         | 30.7  **(↓28.10%)**        |
| Reproduction - (ResNet + ViT)| 9.6  **(↓28.89%)**         | 11.4  **(↓28.75%)**        | 30.5 **(↓51.89%)**         | 30.1  **(↓29.51%)**        |

---
## 📄 Reference
- **Paper**: *Revisiting Change Captioning from Self-supervised Global-Part Alignment*, AAAI 2025. [[PDF Link]](https://ojs.aaai.org/index.php/AAAI/article/view/32629) 
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
```
@inproceedings{lv2025revisiting,
  title={Revisiting Change Captioning from Self-supervised Global-Part Alignment},
  author={Feixiao Lv, Rui Wang, Lihua Jing},
  booktitle={AAAI},
  year={2025}
}
```